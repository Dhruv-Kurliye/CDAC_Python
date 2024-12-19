import requests


def fetch_paper_data(doi):
    # Unpaywall API endpoint
    url = f'https://api.unpaywall.org/v2/{doi}?email=kurliyedrk@gmail.com'  # Replace with your real email

    print(f"Request URL: {url}")  # Debugging: Print the full request URL

    # Sending request to Unpaywall API
    response = requests.get(url)

    print(f"Response Status Code: {response.status_code}")  # Debugging: Print the status code
    print(f"Response Content: {response.text}")  # Debugging: Print the raw response

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        if data.get('is_oa', False):
            # Extract relevant paper data
            paper_info = {
                'title': data.get('title', 'Title not available'),
                'doi': data.get('doi', 'DOI not available'),
                'journal': data.get('journal', 'Journal not available'),
                'oa_url': data.get('oa_url', 'OA URL not available'),
                'published_date': data.get('published_date', 'Published date not available'),
            }

            # Try fetching the full text of the paper from the OA URL
            oa_url = paper_info['oa_url']
            if oa_url != 'OA URL not available':
                full_text = fetch_full_text(oa_url)
                paper_info['full_text'] = full_text
            return paper_info
        else:
            return "No open access version available for this paper."
    else:
        return f"Error fetching data: {response.status_code} - {response.text}"


def fetch_full_text(oa_url):
    # Attempt to fetch the full text of the paper (PDF/HTML)
    try:
        response = requests.get(oa_url)

        if response.status_code == 200:
            # Check content type (it could be PDF or HTML)
            if 'pdf' in response.headers['Content-Type']:
                # Save the PDF to a file
                with open('paper.pdf', 'wb') as file:
                    file.write(response.content)
                return "Full paper is available in PDF format and has been saved as 'paper.pdf'."
            elif 'html' in response.headers['Content-Type']:
                return f"Full paper is available in HTML format: {oa_url}"
            else:
                return "Full text is available in an unknown format."
        else:
            return "Failed to fetch the full text from OA URL."
    except requests.exceptions.RequestException as e:
        return f"Error fetching full text: {e}"


# Example usage
doi = '10.1038/nature12373'  # Example DOI (make sure to replace with an actual valid DOI)
paper_data = fetch_paper_data(doi)

if isinstance(paper_data, dict):
    print("Paper Data:")
    for key, value in paper_data.items():
        print(f"{key}: {value}")
else:
    print(paper_data)
