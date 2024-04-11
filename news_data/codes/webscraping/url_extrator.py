import requests
from bs4 import BeautifulSoup
import csv
import xml.etree.ElementTree as ET
import os


home = 'https://www.indiatoday.in/'
india = 'https://www.indiatoday.in/india/'
world = 'https://www.indiatoday.in/world/'
business = 'https://www.indiatoday.in/business/'
technology = 'https://www.indiatoday.in/technology/'
showbuzz = 'https://www.indiatoday.in/showbuzz/'
sports = 'https://www.indiatoday.in/sports/'
science = 'https://www.indiatoday.in/science/'
health = 'https://www.indiatoday.in/health/'
trending = 'https://www.indiatoday.in/trending-news/'
lifestyle = 'https://www.indiatoday.in/lifestyle/'
education = 'https://www.indiatoday.in/education-today/'
auto = 'https://www.indiatoday.in/auto/'
environment = 'https://www.indiatoday.in/environment/'
lawToday = 'https://www.indiatoday.in/law-today/'
newsAnalysis = 'https://www.indiatoday.in/news-analysis/'
cities = 'https://www.indiatoday.in/cities/'
crime = 'https://www.indiatoday.in/crime/'
opinion = 'https://www.indiatoday.in/opinion-columns/'
crypto = 'https://www.indiatoday.in/cryptocurrency/'
#diu = 'https://www.indiatoday.in/data-intelligence-unit/'


urls = [home, india, world, business, technology, showbuzz, sports, science, health, trending, lifestyle, education, auto, environment, lawToday, newsAnalysis, cities, crime, opinion, crypto] #diu]

count = 0

subUrls = set()
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    allNews = soup.findAll('div', {'class': 'lhs__section'})

    for news in allNews:
        headNews = news.findAll("div", {'class' : "B1S3_B1__s3__widget__lSl3T"})
        for block in headNews:
            blockNews = block.findAll("article", {'class' : "B1S3_story__card__A_fhi"})
            for link in blockNews:
                newsLink = "https://www.indiatoday.in" + link.find("a").get("href")
                count = count + 1
                subUrls.add(newsLink)

print(count)
print(len(subUrls))


file_path = os.path.join(os.path.dirname(__file__), 'url.csv')
if os.path.isfile(file_path):
    # Read the existing URLs from the CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        existing_urls = [row[0] for row in reader]
else:
    existing_urls = []

# Open the CSV file in append mode and write the new URLs that don't already exist
with open(file_path, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Add header if file is empty
    if os.stat(file_path).st_size == 0:
        writer.writerow(['urls'])

    for url in subUrls:
        if url not in existing_urls:
            writer.writerow([url])
            existing_urls.append(url)
            
'''

file_path = os.path.join(os.path.dirname(__file__), 'url.xml')
if os.path.exists(file_path):
    # Parse the existing XML file and get the root element
    tree = ET.parse(file_path)
    root = tree.getroot()
else:
    # Create a new XML file and add the root element
    root = ET.Element('urls')
    tree = ET.ElementTree(root)

# Add new URLs to the XML file
for url in subUrls:
    # Check if the URL already exists in the XML file
    if root.find("./url[@value='{}']".format(url)) is None:
        # Add the new URL as a child element of the root
        url_elem = ET.SubElement(root, 'url', {'value': url})

# Write the updated XML file
tree.write(file_path)

'''
