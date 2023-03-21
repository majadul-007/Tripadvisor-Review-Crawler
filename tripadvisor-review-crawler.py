
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL and user agent

base_url = 'https://www.tripadvisor.com/Attraction_Review-g667467-d1177582-Reviews-';

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Create an empty list to store the reviews.
all_reviews = []

# Loop over the page numbers.
for page_number in range(0, 600, 10):
    # Construct the URL for the current page.
    url = base_url + 'or' + str(page_number) + '-Cox_s_Bazar_Beach-Cox_s_Bazar_Chittagong_Division.html'
    
    # Send a request to the URL and create a BeautifulSoup object.
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all review elements and extract the text.
    reviews = []
    for review in soup.find_all('div', {'class': '_T FKffI bmUTE'}):
        reviews.append(review.text.strip())

    # Add the reviews to the list of all reviews.
    all_reviews.extend(reviews)

# Create a dictionary and a dataframe from the reviews.
data = {'Reviews': all_reviews}
df = pd.DataFrame(data)

# Save the dataframe to a CSV file.
df.to_csv('coxs-bazar-reviews.csv', index=False)
print('Reviews saved to u3-last-coxsbazar-reviews.csv')



























# worked

