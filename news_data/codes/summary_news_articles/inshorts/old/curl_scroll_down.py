import re
import requests
import csv
from bs4 import BeautifulSoup
import time
import html
from unidecode import unidecode
import json


domain = 'https://www.aadhan.in'
# Set initial offset value
offset = 0
count = 0

with open('a_world.csv', mode='a', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    print("file Opened")
    # Write the header row
    writer.writerow(['data_source', 'tagging', 'Headline', 'Author', 'Actual Time', 'Time', 'Date', 'Body', 'Source Name', 'Source Link', 'News Link'])

    while True:
        
        headers = {
            'authority': 'www.aadhan.in',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/json; charset=UTF-8',
            'cookie': 'HXIdentity=e17142bc-4212-40b7-a5ae-384e64b51a2a; HXCountry=IN; HXLanguage=english; _ga=GA1.1.342558056.1683555484; ASP.NET_SessionId=xoxuqtm21ypdq21gzp4rwmlx; __cf_bm=ITTLh3_22wNR3A4WN2rX83xv7qUOSXDukufprF6fN2I-1688793200-0-AZmw+lIVe1ED9Lrto5zd69u5F1dWqTQIW8FUqY/jNlcXS375tOu7qtNdXiLLlVq8JfEiCC4yChaPl7fS2Wiai/I=; _ga_WZRSDPR8MW=GS1.1.1688793202.7.1.1688793371.58.0.0',
            'dnt': '1',
            'origin': 'https://www.aadhan.in',
            'referer': 'https://www.aadhan.in/c/world',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
              
        data = {
            'cat': 'world',
            'eInd': offset,
            'lang': 'english'
        }
        
        json_string = json.dumps(data)

        tagging = 'world'
        data_source = 'Aadhan'
        try:
            response = requests.post('https://www.aadhan.in/data.aspx/GetNewShortCategory', headers=headers, data=json_string)

        except Exception as e:
            print('An error occurred during the request:', str(e))
            break
        

        print(offset)
        
        
        #response_json = json.loads(response.text)
        response_json = response.json()
        html_content = response_json['d'][0]

        
        #response_text = unidecode(response_text)
        #print(response_text)

        soup = BeautifulSoup(html_content, 'html.parser')
        #print(soup)
        soup_length = len(str(soup))
        
        if soup_length < 30:
            break
        
        
        news_cards = soup.find_all('div', class_='panel bdr-0')
        #print(news_cards)
        
        offset = offset + 20
        
        for card in news_cards:
            count = count + 1
            #print(card)
            try:
                headline = card.find('h3', {'class': 'more-feed-heading'}).text.strip()
            except:
                headline = 'none'
            try:
            
                author_element = soup.find('div', class_='article_redir').find('span')
                author = author_element.next_sibling.strip().split('/')[0].strip() if author_element else 'none'

            except:
                author = 'none'
            try:
                actual_time = 'none'
            except:
                actual_time = 'none'
                
            date_time_element = soup.find('div', class_='article_redir').find('p')
            date_time_text = date_time_element.text.strip() if date_time_element else ''
            date1, time1 = date_time_text.split('/', 1)[-1].split(' at ')
            
            try:
                time = time1.strip()
            except:
                time = 'none'
            try:
                date = date1.strip().rstrip(',')
            except:
                date = 'none'
            try:
                body = card.find('p', {'class': 'more-feed-description'}).text.strip()
            except:
                body = 'none'  
            try:
                source_name = card.find('a', {'class': 'link-urlred'}).text.strip().replace('read more at ', '')
            except:
                source_name = 'none'
            try:
                source_link = card.find('a', {'class': 'link-urlred'})['data-href']
            except:
                source_link = 'none'   
            try:
                news_link = domain + card.find('a', {'data-type': 'Short'})['href']
            except:
                news_link = 'none'
                
            print(count)
            
            print(f"Data Source: {data_source}")             
            print(f"Tagging: {tagging}")
            print(f"Headline: {headline}")
            print(f"Author: {author}")
            print(f"Actual Time: {actual_time}")
            print(f"Time: {time}")
            print(f"Date: {date}")
            print(f"Body: {body}")
            print(f"Source Name: {source_name}")
            print(f"Source Link: {source_link}")
            print(f"News Link: {news_link}")
            
            print("******************************************************")
            
                
            # Write the scraped data to the CSV file
            writer.writerow([data_source,tagging,headline, author, actual_time ,time, date, body, source_name, source_link, news_link])

     
      
        #offset = offset + 1         
        
        
        
        
