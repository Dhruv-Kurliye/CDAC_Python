import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# URL of the page where the PDF is available
url = 'https://arxiv.org/abs/quant-ph/0201082v1'

# Send a GET request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the link to the PDF file by searching for the correct tag and attribute
pdf_link_tag = soup.find('a', {'href': True, 'title': 'Download PDF'})

# If the PDF link is found, extract the href attribute (URL of the PDF)
if pdf_link_tag:
    pdf_url = pdf_link_tag['href']
    # Join the base URL with the relative URL to get the absolute URL
    pdf_url = urljoin(url, pdf_url)

    # Send a GET request to download the PDF
    pdf_response = requests.get(pdf_url)

    # Extract the PDF file name from the URL (you can change the file name as needed)
    pdf_file_name = pdf_url.split('/')[-1]

    # Save the PDF to a local file
    with open(pdf_file_name, 'wb') as file:
        file.write(pdf_response.content)

    print(f"Downloaded: {pdf_file_name}")
else:
    print("PDF link not found on the page.")
