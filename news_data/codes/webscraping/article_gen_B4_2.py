import requests
from bs4 import BeautifulSoup
import csv
import json
import xml.etree.ElementTree as ET


output_file = 'articles.json'

articles = []

with open('url.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    urls = [row['urls'] for row in reader]

for url in urls:

    try:
    
        response = requests.get(url)
        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
        
        
        allNews = soup.find('div', {'class': 'lhs__section'})
                    
       
        header1 = allNews.find("h1", {'class' : "jsx-99cc083358cc2e2d Story_strytitle__MYXmR"})
        
        if header1:
            header1 = header1.text
        else:
            header1 = 'N/A'

        header2 = allNews.find("h2", {'class' : "jsx-99cc083358cc2e2d"})
        if header2:
            header2 = header2.text
        else:
            header2 = 'N/A'

        authorName = allNews.find("div",{'class' : "jsx-99cc083358cc2e2d Story_story__author__cJoes"}).find("a")
        if authorName:
            authorName = authorName.text
        else:
            authorName = 'N/A'

        place = allNews.find("span",{'class' : "jsx-99cc083358cc2e2d Story_stryloction__IUgpi"})
        if place:
            place = place.text
        else:
            place = 'N/A'

        timeDate = allNews.find("span",{'class' : "jsx-99cc083358cc2e2d strydate"})
        if timeDate:
            timeDate = timeDate.text
        else:
            timeDate = 'N/A'
        	      
         
        article = {
            'header1': header1,
            'header2': header2,
            'authorName': authorName,
            'place': place,
            'timeDate': timeDate,
            'content': []
        }
        
        
        
        paragraph = allNews.find("div", {'class': "jsx-99cc083358cc2e2d Story_description__fq_4S description"}).findAll("p")

        for p_tag in paragraph:
            if not p_tag.find('strong'):
                if not p_tag.find("div", {'class': "tab-link"}):
                    if not p_tag.find("div",{'class':"embedcode"}):
                        p_text = p_tag.get_text(strip=True)
                        article['content'].append(p_text)
             


        articles.append(article)
        
        
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
 

        
# Save the articles in a JSON file
with open(output_file, 'w',encoding='utf-8') as f:
    json.dump(articles, f, indent=4, ensure_ascii=False)
