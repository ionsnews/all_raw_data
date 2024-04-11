import csv
import json
import newspaper
import requests
from PIL import Image
from io import BytesIO
from datetime import date



# read URLs from a CSV file
with open('url.csv', 'r') as f:
    reader = csv.DictReader(f)
    urls = [row['urls'] for row in reader]

articles = []
count = 0
for url in urls:
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

        # download and save the article image
        image_url = article.top_image
        
        # add article data to the list of articles
        article_data = {
            'source_url': url,
            'title': article.title,
            'publish_date': publish_date,
            'full_text': full_text,
            'image_url':image_url,
            'count' : count
            #'image_filename': image_filename
        }
        articles.append(article_data)
        print(count)

    except Exception as e:
        print(f"Error: {e}")

# write the output data to a JSON file
with open('articles.json', 'w') as f:
    json.dump(articles, f, indent=4)


'''
        
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image_filename = f"{article.title}.jpg"
        image.save(image_filename)
'''
