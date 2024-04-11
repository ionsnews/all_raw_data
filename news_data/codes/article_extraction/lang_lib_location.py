import spacy
import newspaper
from bs4 import BeautifulSoup
import requests

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Set the article URL
url = 'https://whdh.com/news/just-one-station-pembroke-firefighters-help-deliver-baby-in-station-parking-lot/'

# Download the article
article = newspaper.Article(url)

# Parse the article
article.download()
article.parse()

# Extract the author name and remove duplicates
authors = list([author.strip() for author in article.authors])
# Convert the author list to a string separated by comma
authors_str = authors[0]

# Extract the headline, date, and full article
headline = article.title
date = article.publish_date.strftime('%Y-%m-%d') if article.publish_date else None
full_article = article.text

# Extract the locations from the article using spaCy
doc = nlp(full_article)
locations = list([ent.text for ent in doc.ents if ent.label_ == 'GPE'])

# Extract all images related to the article
image = ''.join(article.top_image)

# Extract the main image related to the article
#main_image = images[0] if len(images) > 0 else None

# Print the extracted information
print('Main Image:', image)
print('Author:', authors_str)
print('Headline:', headline)
print('Date:', date)
print('Locations:', locations[0])
print('Full Article:', full_article)




