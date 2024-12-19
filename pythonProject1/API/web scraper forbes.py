import requests
from bs4 import BeautifulSoup
import csv

# URL of Forbes Global 2000 page
url = "https://www.forbes.com/global2000/"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Parse company names (this selector might need to be updated based on Forbes' HTML structure)
companies = []
for item in soup.find_all("div", class_="company-name"):
    companies.append(item.text.strip())

# Save to CSV
output_file = "forbes_global_2000_companies.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Company Name"])
    for company in companies:
        writer.writerow([company])

print(f"Extracted {len(companies)} companies. Saved to {output_file}.")
