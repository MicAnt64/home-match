import os
from typing import Any, Dict

from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import CombinedMemory
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory
from langchain_chroma import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

load_dotenv()

model_name = "gpt-4o"
temperature = 0.1

llm = ChatOpenAI(model_name=model_name, temperature=temperature, max_tokens=1000)

# Generate a set of questions and answers to assess what the user is looking for in a home
personal_real_estate_questions = [
    "What neighborhood(s) do you have in mind?",
    "What is your price range?",
    "How many bedrooms are you looking for?",
    "How many bathrooms are you looking for?",
    "How about the house size (in square feet)?",
    "What kind of home are you looking for, what amenities?",
    "What is your ideal neighborhood, what are you looking for?"
]

personal_real_estate_answers = [
    "I don't know",
    "300,000 - 400,000",
    "2",
    "2",
    "2000",
    "Hard wood floors, high ceilings, a porch",
    "Close to a community pool, in a safe neighbourhood."
]


# Generate a set of questions and answers to get some understanding about the user
preference_questions = [
    "To personalize your response, what is your favorite music band?",
    "What is your favorite movie?",
    "What is the best decade in your lifetime?"
]

preference_answers = [
    "Taylor Swift",
    "The Notebook",
    "2010s"
]



# for q in personal_real_estate_questions:
#     print(q)
#     a = input("Please respond here: ")
#     personal_real_estate_answers.append(a)
#
# for q in preference_questions:
#     print(q)
#     a = input("Please respond here: ")
#     preference_answers.append(a)


history = ChatMessageHistory()
history.add_user_message(
    f"You are a personalized Realtor assistant that will recommend Real Estate listings based on the user's preference."
    f"The following questions are asked by the AI assistant, to better understand what the user is looking for.")

for q, a in zip(personal_real_estate_questions, personal_real_estate_answers):
    history.add_ai_message(q)
    history.add_user_message(a)

history.add_user_message(
    "Now, I will provide you with some questions and answers that will help you guide you in understanding who I am as "
    "a person, what I like, and maybe how I talk (but keep it professional - basically build a persona on how the AI "
    "personalized realtor assistant should talk to and describe the real estate listing for a home the user is looking"
    "for."
)

for q, a in zip(preference_questions, preference_answers):
    history.add_ai_message(q)
    history.add_user_message(a)

# Retrieve the closest real estate listings based on what the user is looking for
PATH_TO_CHROMA_DB = os.getenv("PATH_TO_CHROMA_DB")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    collection_name="home_match",
    embedding_function=embeddings,
    persist_directory=f"{PATH_TO_CHROMA_DB}/real_estate_listings"
)

listing_entry_template = [
    "Neighborhood:", "Price:", "Bedrooms:", "Bathrooms:", "House Size:", "Description:", "Neighborhood Description:"
]

# Generate the query and retrieve top 3 closest listings
num_listings = 3
user_dream_listing = []

for item, answer in zip(listing_entry_template, personal_real_estate_answers):
    user_dream_listing.append(f"{item} {answer}")

user_dream_query = "\n".join(user_dream_listing)

results = vector_store.similarity_search(user_dream_query, k=num_listings)

l = [f"Listing Number: {idx + 1}\n{listing.page_content}" for idx, listing in enumerate(results)]
listings_result = "\n\n".join(l)
# print(listings_result)

summary_memory = ConversationSummaryMemory(
    llm=llm,
    memory_key="recommendation_summary",
    input_key="input",
    buffer=f"The human answered and provided what he is looking for in his future home. The human also provided some "
           f"answers regarding their personality so the AI real estate agent can create a persona that can speak and "
           f"describe the listing in a personalized manner. Also, use the answers provided in what the human is looking"
           f" for so you can understand the language the human uses when you build the persona. Always keep the "
           f"language professional meaning, no toxicity, no foul language, nothing offensive.",
    return_messages=True)

class MementoBufferMemory(ConversationBufferMemory):
    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        input_str, output_str = self._get_input_output(inputs, outputs)
        self.chat_memory.add_ai_message(output_str)

conversational_memory = MementoBufferMemory(
    chat_memory=history,
    memory_key="questions_and_answers",
    input_key="input"
)

memory = CombinedMemory(memories=[conversational_memory, summary_memory])
RECOMMENDER_TEMPLATE = """The following is a friendly conversation between a human and an AI Real Estate Agent 
                        Recommender. The AI follows human instructions and provides real estate listings for a human, 
                        based listings provided as context and the human's persona derived from their answers to 
                        questions.
#
# Summary of Recommendations:
# {recommendation_summary}
# Personal Questions and Answers:
# {questions_and_answers}
# Human: {input}
# AI:"""

PROMPT = PromptTemplate(
    input_variables=["recommendation_summary", "input", "questions_and_answers"],
    template=RECOMMENDER_TEMPLATE
)
recommender = ConversationChain(llm=llm, verbose=True, memory=memory, prompt=PROMPT)

real_estate_instructions = f"""
=====================================
=== CLOSEST REAL ESTATE LISTINGS ===
{listings_result}
=== END OF REAL ESTATE LISTINGS ===
=====================================
AI will provide a highly personalized real estate listing based on what the human is looking for in the human provided
answers to questions included with the context. The listings retrieved from the database are the {num_listings}
closest listings based on what the human may be looking for.
AI should be very sensible to human personal preferences captured in the answers to personal questions,
and should not be influenced by anything else.
AI will also build a persona for the human based on the human's answers to questions, and use this persona to a provide
real estate listings. Keep the listings factual. Do not hallucinate.
OUTPUT FORMAT:
FOLLOW THE INSTRUCTIONS STRICTLY, OTHERWISE HUMAN WILL NOT BE ABLE TO UNDERSTAND YOUR REVIEW. OUTPUT THE LISTING AS A
TEXT DESCRIPTION OF THE LISTING emphasizing aspects of the property that align with what the buyer is looking for. 
Maintain Factual Integrity. Do not hallucinate. Ensure that the augmentation process enhances the appeal of the 
listing without altering factual info. Propose the listing in text-like format as if it were a human describing the 
property. Ensure you incorporate answers to personal questions to make the listing more personal. Just pick 1 listing.
"""

# Get AI Recommendation
prediction = recommender.predict(input=real_estate_instructions)
print(prediction)


