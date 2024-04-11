import csv
import requests
from datetime import datetime
import re

def write_to_csv(file_path, data):
    # Open a CSV file for appending
    with open(file_path, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        # If the file is empty, write the header row
        if file.tell() == 0:
            header_row = [
                'Tagging', 'rank', 'news_type', 'hash_id', 'old_hash_id', 'type', 'version', 'Author', 'Content',
                'Source URL', 'Source Name', 'Title', 'Important', 'Image URL', 'Shortened URL', 'Score', 'Categories',
                'Relevancy_tags', 'Country_code', 'Impressive_score', 'targeted_city', 'created_at',
                'position_start_time', 'position_expire_time', 'gallery_image_urls', 'full_gallery_urls', 'bottom_headline',
                'bottom_text', 'bottom_panel_link', 'dfp_tags', 'trackers'
            ]
            writer.writerow(header_row)

        # Write the extracted information to the CSV file
        writer.writerow(data)

def scrape_inshorts(page_number):
    tagging = "national"
    url = f'https://www.inshorts.com/api/en/search/trending_topics/{tagging}?page={page_number}&type=NEWS_CATEGORY'

    headers = {
        'authority': 'www.inshorts.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'referer': 'https://www.inshorts.com/en/read',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-region-id': 'IN',
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        json_response = response.json()

        # Extract information from each news item
        for news_item in json_response['data']['suggested_news']:
            news_obj = news_item.get('news_obj', {})
            rank = news_item.get('rank', {})
            news_type = news_item.get('news_type', {})
            hash_id = news_item.get('hash_id', {})
            old_hash_id = news_obj.get('old_hash_id', {})
            Type1 = news_item.get('type', {})
            version = news_item.get('version', {})
            author = news_obj.get('author_name', 'None')
            content = news_obj.get('content', 'None')
            source_url = news_obj.get('source_url', 'None')
            source_name = news_obj.get('source_name', 'None')
            title = news_obj.get('title', 'None')
            important = news_obj.get('important', 'None')
            image_url = news_obj.get('image_url', 'None')
            shortened_url = news_obj.get('shortened_url', 'None')
            score = news_obj.get('score', 'None')
            categories = ', '.join(news_obj.get('category_names', []))
            relevancy_tags = ', '.join(news_obj.get('relevancy_tags', []))
            country_code = news_obj.get('country_code', 'None')
            impressive_score = news_obj.get('impressive_score', 'None')
            targeted_city = ', '.join(news_obj.get('targeted_city', []))          
            created_at = news_obj.get('created_at', 'None')
            position_start_time = news_obj.get('position_start_time', 'None')
            position_expire_time = news_obj.get('position_expire_time', 'None')
            gallery_image_urls = news_obj.get('gallery_image_urls', 'None')
            full_gallery_urls = news_obj.get('full_gallery_urls', 'None')
            bottom_headline = news_obj.get('bottom_headline', 'None')
            bottom_text = news_obj.get('bottom_text', 'None')
            bottom_panel_link = news_obj.get('bottom_panel_link', 'None')
            dfp_tags = news_obj.get('dfp_tags', 'None')
            trackers = news_obj.get('trackers', 'None')
            
            
            # Print statements for each extracted field
            print("Tagging:", tagging)
            print("Rank:", rank)
            print("News Type:", news_type)
            print("Hash ID:", hash_id)
            print("Old Hash ID:", old_hash_id)
            print("Type:", Type1)
            print("Version:", version)
            print("Author:", author)
            print("Content:", content)
            print("Source URL:", source_url)
            print("Source Name:", source_name)
            print("Title:", title)
            print("Important:", important)
            print("Image URL:", image_url)
            print("Shortened URL:", shortened_url)
            print("Score:", score)
            print("Categories:", categories)
            print("Relevancy Tags:", relevancy_tags)
            print("Country Code:", country_code)
            print("Impressive Score:", impressive_score)
            print("Targeted City:", targeted_city)
            print("Created At:", created_at)
            print("Position Start Time:", position_start_time)
            print("Position Expire Time:", position_expire_time)
            print("Gallery Image URLs:", gallery_image_urls)
            print("Full Gallery URLs:", full_gallery_urls)
            print("Bottom Headline:", bottom_headline)
            print("Bottom Text:", bottom_text)
            print("Bottom Panel Link:", bottom_panel_link)
            print("DFP Tags:", dfp_tags)
            print("Trackers:", trackers)
            print("--------------------------------------------------")

            # Write the extracted information to the CSV file
            data_row = [
                tagging, rank, news_type, hash_id, old_hash_id, Type1, version, author, content, source_url,
                source_name, title, important, image_url, shortened_url, score, categories, relevancy_tags,
                country_code, impressive_score, targeted_city, created_at,
                position_start_time, position_expire_time, gallery_image_urls, full_gallery_urls, bottom_headline,
                bottom_text, bottom_panel_link, dfp_tags, trackers
            ]
            write_to_csv(f'{tagging}.csv', data_row)

        # print(f"Data for page {page_number} has been scraped and appended to {tagging}.csv")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {str(e)}")

# Set the range of pages you want to scrape
start_page = 1
end_page = 23335  # Change this to the desired end page

# Scraping loop
for page_number in range(start_page, end_page + 1):
    scrape_inshorts(page_number)
