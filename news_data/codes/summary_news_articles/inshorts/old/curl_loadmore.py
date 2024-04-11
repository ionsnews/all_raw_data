    import re
import requests
import csv
from bs4 import BeautifulSoup
import time
import requests
import html


domain = 'https://www.inshorts.com'
# Set initial offset value
offset = "l_ipbboslq-1"
count = 0

with open('all.csv', mode='a', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    print("file Opened")
    # Write the header row
    writer.writerow(['tagging','Headline', 'Author', 'Actual Time', 'Time', 'Date', 'Body', 'Source Name', 'Source Link', 'News Link'])

    while True:
        
        headers = {
            'authority': 'www.inshorts.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': '_ga=GA1.2.1151596755.1683533516; _gid=GA1.2.2071425339.1687695113; _gat=1',
            'dnt': '1',
            'origin': 'https://www.inshorts.com',
            'referer': 'https://www.inshorts.com/en/read/',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        data = {
            'category': '',
            'news_offset': offset
        }
        tagging = 'all'
        try:
            response = requests.post('https://www.inshorts.com/en/ajax/more_news', headers=headers, data=data)

        except Exception as e:
            print('An error occurred during the request:', str(e))
            break
        
        try:    
            print(f"status: {response.status_code}")    
            for_offset = response.json()
        except:
            continue
        
        try:
            offset = for_offset['min_news_id']
            data['offset'] = offset
        except KeyError:
            break
               
        print(offset)
        
        
        response_text = response.text
        response_text = re.sub(r'\\(["\'])', r'\1', response_text)
        response_text = response_text.replace('\"', '')
        response_text = response_text.replace('\n', '')

        soup = BeautifulSoup(response_text, 'html.parser')
        #print(soup)
        
        news_cards = soup.find_all('div', class_='news-card')
        #print(news_cards)
        
        for card in news_cards:
            count = count + 1
            #print(card)
            try:
                headline = card.find('span', {'itemprop': 'headline'}).text.strip()
            except:
                headline = 'none'
            try:
                author = card.find('span', {'class': 'author'}).text.strip()
            except:
                author = 'none'
            try:
                actual_time = soup.find('span', {'class': 'time'})['content']
            except:
                actual_time = 'none'
            try:
                time = card.find('span', {'class': 'time'}).text.strip()
            except:
                time = 'none'
            try:
                date = card.find('span', {'clas': 'date'}).text
            except:
                date = 'none'
            try:
                body = card.find('div', {'itemprop': 'articleBody'}).text.strip()
            except:
                body = 'none'  
            try:
                source_name = card.find('a', {'class': 'source'}).text.strip()
            except:
                source_name = 'none'
            try:
                source_link = card.find('a', {'class': 'source'})['href']
            except:
                source_link = 'none'   
            try:
                news_link = domain + card.find('a', {'class': 'clickable'})['href']
            except:
                news_link = 'none'
                
            print(count)
            '''  
            print(f"Tagging: {tagging}")
            print(f"Headline: {headline}")
            print(f"Author: {author}")
            print(f"Actual Time: {actual_time}")
            print(f"Time: {time}")
            print(f"Date: {date}")
            print(f"Body: {body}")
            print(f"Source Name: {source_name}")
            print(f"Source Link: {source_link}")
            print(f"News link: {news_link}")
            
            print("******************************************************")
            '''
                
            # Write the scraped data to the CSV file
            writer.writerow([tagging,headline, author, actual_time ,time, date, body, source_name, source_link, news_link])

        
        
        
        
        
        
