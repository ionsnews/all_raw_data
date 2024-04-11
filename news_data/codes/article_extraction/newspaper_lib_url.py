import csv
import json
import newspaper
import requests
from PIL import Image
from io import BytesIO
from datetime import date

url = "https://whdh.com/news/just-one-station-pembroke-firefighters-help-deliver-baby-in-station-parking-lot/"

one_articles = []

count = 0


# download and parse the article
try:
    count = count + 1
    article = newspaper.Article(url)
    article.download()
    article.parse()

    # get the article publish date
    if article.publish_date:
        publish_date = article.publish_date.strftime('%Y-%m-%d')
    else:
        publish_date = date.today()
    
    # get the full text of the article
    full_text = article.text
    
    # download the article image
    image_url = article.top_image


    # add article data to the list of articles

    print('\n')
    print(url)
    print('\n')
    print(article.title)
    print('\n')
    print(publish_date)
    print('\n')
    print(image_url)
    print('\n')
    print(full_text)
        
except Exception as e:
    print(f"Error: {e}")



'''
        # download and save the article image
        image_url = article.top_image
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image_filename = f"{article.title}.jpg"
        image.save(image_filename)
'''
