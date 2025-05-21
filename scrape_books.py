import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book titles
books = soup.find_all('h3')

# Print book titles (optional)
for book in books:
    print(book.a['title'])

# Save to CSV file
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Book Title'])

    for book in books:
        writer.writerow([book.a['title']])
