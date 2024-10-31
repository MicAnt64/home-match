"""Class to generate dummy real estate listings using an LLM and saving these listings in a Vector Database"""
from dotenv import load_dotenv
from openai import OpenAI
from typing import List
from db_tools.chroma_db_tools import ChromaDatabaseCollection
import os

load_dotenv()
PATH_TO_CHROMA_DB = os.getenv("PATH_TO_CHROMA_DB")

client = OpenAI()

class GenerateRealEstateListings:
    """
    Create fake real estate listings for demonstration purposes. Uses OpenAI LLM to generate listings. The listings are
    then stored in a Vector DB. Embeddings are created by the Vector DB.
    """
    def __init__(self, model:str = "gpt-4o", num_listings:int = 20):
        """
        Class constructor
        :param model: OpenAI model name
        :param num_listings: number of listings to generate
        """
        self.model = model
        self.num_listings = num_listings

    def create_real_estate_listing(self) -> List[str]:
        """
        Create real estate listing using an LLM. System prompt, listing format are hard-coded.
        :return: A string of multiple listings
        """
        system_prompt = "You are a helpful assistant that generates real estate listings."
        example_listing = """Neighborhood: Green Oaks \nPrice: $800,000 \nBedrooms: 3 \nBathrooms: 2 \nHouse Size: 2,000 sqft \nDescription: Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem. \nNeighborhood Description: Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze.*** New Listing ***"""
        listing_format = """Neighborhood: \nPrice: \nBedrooms: \nBathrooms: \nHouse Size: \nDescription: \nNeighborhood Description: *** New Listing ***"""
        user_prompt = (f"Please create {self.num_listings} real estate listings. Each listing should contain: Neighborhood,"
                       f" Price, Bedrooms, Bathrooms, House Size, Description, Neighborhood Description. Neighborhood is"
                       f" just the neighborhood name. Price is in USD, for example $345,000. Bedrooms is just and "
                       f"integer value. Bathrooms is just an integer value. House size is an integer value, in square"
                       f" feet, for example: 3,200 sqft. Description is a few sentences describing the home. "
                       f"Neighborhood Description is a few sentences describing the neighborhood. Here is an example of "
                       f"a listing: {example_listing}. Please use this format as it is {listing_format}. Separate each new"
                       f" listing by adding ***New Listing*** indicator and ensure you don't add new lines and don't add"
                       f" a leading nor a trailing delimiter to the beginning of your response or at the very end. "
                       f"There must be {self.num_listings} listings.")

        completion = client.chat.completions.create(
            model=self.model,
            temperature=0.7,
            top_p=1,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        listings_str = completion.choices[0].message.content
        listings_list = listings_str.split("***New Listing***")

        if len(listings_list) < self.num_listings:
            raise NotImplementedError(f"The AI Model did not generate {self.num_listings}. {len(listings_list)} "
                                      f"listings were generated. Please try again.")

        clean_listings_list = [i.strip() for i in listings_list if i]

        return clean_listings_list

    def create_and_store_real_estate_listings(self):
        """
        Obtains generated real estate listings, connects to DB client, creates a collection called 'home_match' and then
        adds real_estate listings to the collection.
        """

        real_estate_listings = self.create_real_estate_listing()
        chroma_db_tools = ChromaDatabaseCollection(f"{PATH_TO_CHROMA_DB}/real_estate_listings")
        chroma_db_tools.connect_to_client()
        chroma_db_tools.create_collection("home_match")
        chroma_db_tools.add_entries(real_estate_listings)
        print(f"{len(real_estate_listings)} have been added to the database.")


if __name__ == "__main__":
    grel = GenerateRealEstateListings()
    grel.create_and_store_real_estate_listings()