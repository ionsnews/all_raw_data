import csv
import json
import newspaper
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup


# read URLs from a CSV file
with open('url.csv', 'r') as f:
    reader = csv.DictReader(f)
    urls = [row['urls'] for row in reader]

articles = []

count = 0
for url in urls:
    # download and parse the article
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')

        allNews = soup.find('div', {'class': 'lhs__section'})

        header1 = allNews.find("h1", {'class': "jsx-99cc083358cc2e2d Story_strytitle__MYXmR"}).text

        header2 = allNews.find("h2", {'class': "jsx-99cc083358cc2e2d"}).text

        authorName = allNews.find("div", {'class': "jsx-99cc083358cc2e2d Story_story__author__cJoes"}).find("a").text

        place = allNews.find("span", {'class': "jsx-99cc083358cc2e2d Story_stryloction__IUgpi"}).text

        timeDate = allNews.find("span", {'class': "jsx-99cc083358cc2e2d strydate"}).text

        paragraph = allNews.find("div", {'class': "jsx-99cc083358cc2e2d Story_description__fq_4S description"}).findAll("p")

        article = {
            'header1': header1,
            'header2': header2,
            'authorName': authorName,
            'place': place,
            'timeDate': timeDate,
            'content': []
        }

        for p_tag in paragraph:
            if not p_tag.find('strong'):
                if not p_tag.find("div", {'class': "tab-link"}):
                    p_text = p_tag.get_text(strip=True)
                    article['content'].append(p_text)

        articles.append(article)
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# write the output data to a JSON file
with open('articles.json', 'w') as f:
    json.dump(articles, f, indent=4)


'''
        # download and save the article image
        image_url = article.top_image
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image_filename = f"{article.title}.jpg"
        image.save(image_filename)
'''
