import requests
from bs4 import BeautifulSoup

# Define the URL of the API endpoint
url = 'http://127.0.0.1:5000'

# Prepare the files to upload
files = {
    'file1': open('C:/Users/91720/Downloads/dumy1.txt', 'r',encoding='utf-8'),
    'file2': open('C:/Users/91720/Downloads/dumy1.txt', 'r',encoding='utf-8')
}

# Make a POST request to the API endpoint with the files
response = requests.post(url, files=files)

# # Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON response
    data = response.content
    # Parse HTML content

    soup = BeautifulSoup(data, 'html.parser')

    # Extract tag data
    tag_divs = soup.find_all('div', class_='card5 section')  # Assuming you want data from this specific div

    # Loop through tag divs and extract the similarity score
    for div in tag_divs:
        similarity_score = div.find('h2').text.strip().split(':')[-1].strip()
        print("Similarity Score:", similarity_score)
else:
    print('Error:', response.text)
