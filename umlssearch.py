import requests

# Replace 'YOUR_APIKEY' with your actual UMLS API key
UMLS_API_KEY = 'YOURAPIKEY'

version = 'current'  # version can be 'current' or a specific version
search_term = 'Gonadal dysgenesis'  # the term you want to search
source = 'C0018051' # the cui you want to search


# use this url if searching by term
# url = f"https://uts-ws.nlm.nih.gov/rest/search/current?string={search_term}&apiKey={UMLS_API_KEY}"

#use this if searching by cui code
url =   f"https://uts-ws.nlm.nih.gov/rest/content/current/CUI/{source}/definitions?apiKey={UMLS_API_KEY}"

# check https://documentation.uts.nlm.nih.gov/rest/search/ for more search options

def search_cui(url):
    response = requests.get(url)
    
    # print the status code and the response text for debugging
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Search Results:\n {data)
        
    else:
        print("Failed to retrieve the data.")
        print("Response Text:", response.text)

search_cui(url)
