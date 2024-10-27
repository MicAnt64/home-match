"""Class to generate dummy real estate listings using an LLM and saving these listings in a Vector Database"""
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

class GenerateRealEstateListings:
    """
    Create fake real estate listings for demonstration purposes. Uses OpenAI LLM to genereate these listings. XYZ is
    used to create embeddings. The listings and embeddings are then stored in a Vector DB.
    """
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def create_real_estate_listing(self, num_listings: int) -> str:
        """
        Create real estate listing using an LLM. System prompt, listing format are hard-coded.
        :param num_listings: Number of listings to create
        :return:
        """
        system_prompt = "You are a helpful assistant that generates real estate listings."
        example_listing = """
        Neighborhood: Green Oaks
        Price: $800,000
        Bedrooms: 3
        Bathrooms: 2
        House Size: 2,000 sqft
        Description: Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.
        Neighborhood Description: Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze.
        """
        listing_format = """
                Neighborhood:
                Price:
                Bedrooms:
                Bathrooms:
                House Size:
                Description:
                Neighborhood Description:
                """
        user_prompt = (f"Please create {num_listings} real estate listings. Each listing should contain: Neighborhood,"
                       f" Price, Bedrooms, Bathrooms, House Size, Description, Neighborhood Description. Neighborhood is"
                       f" just the neighborhood name. Price is in USD, for example $345,000. Bedrooms is just and "
                       f"integer value. Bathrooms is just an integer value. House size is an integer value, in square"
                       f" feet, for example: 3,200 sqft. Description is a few sentences describing the home. "
                       f"Neighborhood Description is a few sentences describing the neighborhood. Here is an example of "
                       f"a listing: {example_listing}. Please use this format as it is {listing_format}. Seperate each new"
                       f" listing by a new line with *** New Listing ***. Now create {num_listings} listings.")

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

        return completion.choices[0].message.content


grel = GenerateRealEstateListings()
listings = grel.create_real_estate_listing(3)
listings = listings.split("*** New Listing *** ")
print(listings[1].strip())
