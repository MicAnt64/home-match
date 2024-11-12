# home-match

Receive personalized real estate listings via a tailored property search engine based on your user preferences.

This application uses LLMs and Vector Databases to build narratives around standard real estate listings to better match
your persona. 

## Examples

### Example 1
User 1 is looking for the following:

##### <u>Q & A to understand what the user is looking for</u>
AI: What neighborhood(s) do you have in mind?
Human: Some nice sounding name

AI: What is your price range?
Human: 500,000 - 550,000

AI: How many bedrooms are you looking for?
Human: 4

AI: How many bathrooms are you looking for?
Human: 3

AI: How about the house size (in square feet)?
Human: 5000

AI: What kind of home are you looking for, what amenities?
Human: A cozy home, with a backyard, a pool, a fireplace, open space kitchen, quiet neighborhood. Single story.

AI: What is your ideal neighborhood, what are you looking for?
Human: Has a lot of green, vegetation, proximity to grocery stores, quiet neighborhood, good school district.

Human: Now, I will provide you with some questions and answers that will help you guide you in understanding who I am as a person, what I like, maybe how I talk (but keep it professional - basically build a persona on how the AI personalized realtor assistant should talk to and describe the real estate listing for a home the user is looking for.
AI: To personalize your response, what is your favorite music band?
Human: The Doors

AI: What is your favorite movie?
Human: The Godfather

AI: What is the best decade in your lifetime?
Human: 1970s

##### <u>Top 3 Real estate listings based on what the user is looking for</u>
Listing Number: 1

Neighborhood: Stonebridge  
Price: $440,000  
Bedrooms: 4  
Bathrooms: 3  
House Size: 2,500 sqft  
Description: This beautiful 4-bedroom, 3-bathroom home in Stonebridge offers a spacious living area with modern amenities. The kitchen features granite countertops and stainless steel appliances. The backyard is perfect for relaxation, with a covered patio and garden area.  
Neighborhood Description: Stonebridge is a family-friendly neighborhood known for its excellent schools and community activities. Residents enjoy nearby parks, sports facilities, and local events. The area offers a suburban lifestyle with easy access to city amenities.

Listing Number: 2

Neighborhood: Willow Creek  
Price: $450,000  
Bedrooms: 4  
Bathrooms: 3  
House Size: 2,500 sqft  
Description: Discover the elegance of this spacious 4-bedroom, 3-bathroom home in Willow Creek. Featuring a modern kitchen with granite countertops and stainless steel appliances, this home offers an open floor plan perfect for entertaining. The master suite includes a walk-in closet and a luxurious en-suite bathroom. Outside, enjoy a large deck overlooking a beautifully landscaped backyard.  
Neighborhood Description: Willow Creek is a serene suburban neighborhood known for its family-friendly atmosphere and excellent schools. With numerous parks and recreational facilities, it's ideal for active families. Enjoy easy access to shopping centers and restaurants in this vibrant community.

Listing Number: 3

Neighborhood: Redwood Acres  
Price: $495,000  
Bedrooms: 4  
Bathrooms: 3  
House Size: 2,700 sqft  
Description: Nestled in Redwood Acres, this beautiful 4-bedroom, 3-bathroom home offers an open floor plan with high ceilings and hardwood floors. The kitchen features modern appliances and a large island. The backyard is a serene retreat with a deck and garden area.  
Neighborhood Description: Redwood Acres is a family-friendly neighborhood known for its excellent schools and community spirit. Residents enjoy access to parks, walking trails, and a community center. The area offers a suburban feel with easy access to city amenities.

##### <u>Recommended Real Estate Listing by AI</u>
Based on your preferences and the listings available, I have found a property that might resonate with your vision of a cozy, serene home. Let's take a closer look at this option:

**Listing Number: 3 - Redwood Acres**

Nestled in the tranquil neighborhood of Redwood Acres, this charming 4-bedroom, 3-bathroom home is priced at $495,000. With a house size of 2,700 square feet, it offers ample space for comfort and relaxation. The open floor plan, complemented by high ceilings and hardwood floors, creates a warm and inviting atmosphere reminiscent of the classic elegance you might appreciate, akin to the timeless appeal of "The Godfather."

The modern kitchen is equipped with contemporary appliances and a large island, perfect for preparing meals while enjoying the company of family and friends. The backyard serves as a serene retreat, featuring a deck and garden area where you can unwind and perhaps listen to some tunes from The Doors, surrounded by the lush greenery you desire.

Redwood Acres is known for its excellent schools and strong community spirit, making it an ideal location for families. The neighborhood offers access to parks, walking trails, and a community center, providing a peaceful suburban feel with convenient access to city amenities. This aligns well with your preference for a quiet neighborhood with plenty of vegetation and proximity to essential services.

This home embodies the cozy, single-story living you seek, with the added benefit of being in a vibrant community that values tranquility and nature. If this sounds like the perfect fit for you, I'd be delighted to assist you further in exploring this opportunity.

Process finished with exit code 0

### Example 2

##### <u>Q & A to understand what the user is looking for</u>
AI: What neighborhood(s) do you have in mind?
Human: Not Applicable

AI: What is your price range?
Human: 1,500,000 - 2,000,000

AI: How many bedrooms are you looking for?
Human: 6

AI: How many bathrooms are you looking for?
Human: 4

AI: How about the house size (in square feet)?
Human: 8000

AI: What kind of home are you looking for, what amenities?
Human: Hard wood floors, high ceilings, open kitchen, jacuzzi, large backyard, overview to the city on mountaintop, Gym at the house, 3 car garage.

AI: What is your ideal neighborhood, what are you looking for?
Human: Gate community, Clubhouse, close to stores. Good school district

Human: Now, I will provide you with some questions and answers that will help you guide you in understanding who I am as a person, what I like, maybe how I talk (but keep it professional - basically build a persona on how the AI personalized realtor assistant should talk to and describe the real estate listing for a home the user is looking for.
AI: To personalize your response, what is your favorite music band?
Human: Frank Sinatra

AI: What is your favorite movie?
Human: Citizen Kane

AI: What is the best decade in your lifetime?
Human: 1950s

##### <u>Top 3 Real estate listings based on what the user is looking for</u>
Listing Number: 1

Neighborhood: Maplewood Estates  
Price: $625,000  
Bedrooms: 5  
Bathrooms: 4  
House Size: 3,200 sqft  
Description: Situated in the prestigious Maplewood Estates, this expansive 5-bedroom, 4-bathroom home is a perfect blend of luxury and comfort. The gourmet kitchen features a large island and custom cabinetry. The spacious living room with a fireplace opens to a private patio. The master suite offers a spa-like bathroom and private balcony.  
Neighborhood Description: Maplewood Estates is a sought-after neighborhood with tree-lined streets and luxurious homes. Residents enjoy access to private parks, tennis courts, and a community clubhouse. The area is known for its tranquil atmosphere and excellent schools.

Listing Number: 2

Neighborhood: Highland View  
Price: $580,000  
Bedrooms: 4  
Bathrooms: 3  
House Size: 2,900 sqft  
Description: Discover this stunning 4-bedroom, 3-bathroom home in Highland View, featuring a spacious open floor plan and high-end finishes. The gourmet kitchen includes a large island and custom cabinetry. The living room opens to a private patio, perfect for outdoor gatherings.  
Neighborhood Description: Highland View is an upscale neighborhood known for its scenic views and luxurious homes. Residents enjoy access to parks, hiking trails, and excellent schools. The community offers a peaceful environment with convenient city access.

Listing Number: 3

Neighborhood: Aspen Woods  
Price: $485,000  
Bedrooms: 4  
Bathrooms: 3  
House Size: 2,600 sqft  
Description: Welcome to Aspen Woods, where this beautiful 4-bedroom, 3-bathroom home awaits. Featuring a modern design with an open floor plan, the home includes a stylish kitchen with stainless steel appliances and a large island. The backyard boasts a covered patio and a play area.  
Neighborhood Description: Aspen Woods is a family-friendly neighborhood known for its excellent schools and community events. Residents enjoy parks, walking trails, and a local community center. The area offers a mix of suburban charm and convenient city access.

##### <u>Recommended Real Estate Listing by AI</u>
Ah, the allure of a home that resonates with the elegance of Frank Sinatra's melodies and the timeless charm of the 1950s. Allow me to introduce you to a property that, while not precisely matching your criteria, offers a glimpse into a lifestyle of luxury and comfort reminiscent of a bygone era.

Nestled in the prestigious Maplewood Estates, this expansive 5-bedroom, 4-bathroom home is a harmonious blend of sophistication and warmth. Priced at $625,000, it offers a spacious 3,200 square feet of living space. The gourmet kitchen, with its large island and custom cabinetry, is perfect for hosting gatherings reminiscent of the grand soirées of the past. The living room, complete with a cozy fireplace, opens to a private patio, inviting you to enjoy serene evenings under the stars.

The master suite is a sanctuary of relaxation, featuring a spa-like bathroom and a private balcony, offering a personal retreat reminiscent of the elegance found in "Citizen Kane." While the home does not sit atop a mountaintop, the neighborhood's tree-lined streets and luxurious homes provide a tranquil atmosphere, akin to the peacefulness of a gated community.

Maplewood Estates offers access to private parks, tennis courts, and a community clubhouse, ensuring that leisure and recreation are always within reach. The excellent schools in the area make it an ideal choice for families seeking quality education.

While this home may not fulfill every aspect of your dream, it embodies a lifestyle of grace and refinement that echoes the best of the 1950s. I invite you to consider this property as a potential canvas for your future memories.

### Example 3

##### <u>Q & A to understand what the user is looking for</u>
##### <u>Top 3 Real estate listings based on what the user is looking for</u>
##### <u>Recommended Real Estate Listing by AI</u>


## Software Design
This repository contains the following:
- db_tools/chroma_db_tools.py

Used for connecting to a Chroma DB, creating, getting, or deleting a collection. Can also peek at the 10 first items 
obtained from a collection, and count items in a collection. You can also add documents or query a collection. The 
embeddings are created using OpenAI's <i>text-embedding-3-small</i> embedding function. We also use the cosine 
similarity metric as a distance function to obtain the most relevant results.

- db/real_estate_listings

This is the path where the Chroma DB is located for the Home Match application. It contains 20 listings that were 
generated using <i>GenerateRealEstateListings.py</i>.

To see an example of 10 listings that are in the database, please refer to the file located at: 
<i>db/example_listings.txt</i>. You can use the peek method in the <i>ChromaDatabaseCollection</i> class under the
<i>chroma_db_tools.py</i> file.

- listings/GenerateRealEstateListings.py

Is used to create real estate listings using OpenAI's <i>gpt-4o</i> model. Listings are then inserted into the Chroma DB 
under the <i>home_match</i> collection.

- requirements.txt

Contains libraries/packages needed to run this application.

- HomeMatch.py

Contains the logic that asks the user what they are looking for in their new home, and minor questions to 
personalize the response, then it queries the Chroma DB for the top 3 results that are closest to what the user is 
looking for. Finally, the Real Estate AI recommender picks one of the three real estate listings, and suggests the 
listing in a conversation-like format while personalizing it based on the user's questions.

- db/ten_listings_from_db.txt

Contains code on how to peek at the database and get 10 listings. Also contains 10 listings obtained from the database.

- .env

You will need a .env file that contains and OPENAI_API_KEY, OPENAI_API_BASE, and you'll need to modify the 
PATH_TO_CHROMA_DB.