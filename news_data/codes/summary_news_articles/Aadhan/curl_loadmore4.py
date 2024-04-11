import csv
import logging
import requests
from datetime import datetime

logging.basicConfig(filename='scraping_log.txt', level=logging.ERROR)

header_row = [
    'Tagging', 'rank', 'news_type', 'hash_id', 'old_hash_id', 'type', 'version', 'Author', 'Content',
    'Source URL', 'Source Name', 'Title', 'Important', 'Image URL', 'Shortened URL', 'Score', 'Categories',
    'Relevancy_tags', 'Country_code', 'Impressive_score', 'targeted_city', 'created_at',
    'position_start_time', 'position_expire_time', 'gallery_image_urls', 'full_gallery_urls', 'bottom_headline',
    'bottom_text', 'bottom_panel_link', 'dfp_tags', 'trackers'
]

def write_to_csv(file_path, data):
    # Open a CSV file for appending
    with open(file_path, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header_row)

        # If the file is empty, write the header row
        if file.tell() == 0:
            writer.writeheader()

        # Write the extracted information to the CSV file
        writer.writerow(dict(zip(header_row, data)))

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
            
            # Ensure required fields are present
            if all(field in news_obj for field in ['rank', 'news_type', 'hash_id']):
                # Extract relevant information
                rank = news_item['rank']
                news_type = news_item['news_type']
                hash_id = news_item['hash_id']
                old_hash_id = news_obj.get('old_hash_id', {})
                Type = news_item.get('type', {})
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
                logging.info("Tagging: %s", tagging)
                logging.info("Rank: %s", rank)
                logging.info("News Type: %s", news_type)
                logging.info("Hash ID: %s", hash_id)
                logging.info("Old Hash ID: %s", old_hash_id)
                logging.info("Type: %s", Type)
                logging.info("Version: %s", version)
                logging.info("Author: %s", author)
                logging.info("Content: %s", content)
                logging.info("Source URL: %s", source_url)
                logging.info("Source Name: %s", source_name)
                logging.info("Title: %s", title)
                logging.info("Important: %s", important)
                logging.info("Image URL: %s", image_url)
                logging.info("Shortened URL: %s", shortened_url)
                logging.info("Score: %s", score)
                logging.info("Categories: %s", categories)
                logging.info("Relevancy Tags: %s", relevancy_tags)
                logging.info("Country Code: %s", country_code)
                logging.info("Impressive Score: %s", impressive_score)
                logging.info("Targeted City: %s", targeted_city)
                logging.info("Created At: %s", created_at)
                logging.info("Position Start Time: %s", position_start_time)
                logging.info("Position Expire Time: %s", position_expire_time)
                logging.info("Gallery Image URLs: %s", gallery_image_urls)
                logging.info("Full Gallery URLs: %s", full_gallery_urls)
                logging.info("Bottom Headline: %s", bottom_headline)
                logging.info("Bottom Text: %s", bottom_text)
                logging.info("Bottom Panel Link: %s", bottom_panel_link)
                logging.info("DFP Tags: %s", dfp_tags)
                logging.info("Trackers: %s", trackers)
                logging.info("--------------------------------------------------")

                # Write the extracted information to the CSV file
                data_row = [
                    tagging, rank, news_type, hash_id, old_hash_id, Type, version, author, content, source_url,
                    source_name, title, important, image_url, shortened_url, score, categories, relevancy_tags,
                    country_code, impressive_score, targeted_city, created_at,
                    position_start_time, position_expire_time, gallery_image_urls, full_gallery_urls, bottom_headline,
                    bottom_text, bottom_panel_link, dfp_tags, trackers
                ]
                write_to_csv(f'{tagging}.csv', data_row)

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the request: {str(e)}")

# Set the range of pages you want to scrape
start_page = 1
end_page = 23335  # Change this to the desired end page

# Scraping loop
for page_number in range(start_page, end_page + 1):
    scrape_inshorts(page_number)

