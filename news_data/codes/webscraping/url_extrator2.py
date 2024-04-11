import csv
import os
import requests
from bs4 import BeautifulSoup

url = "https://blog.feedspot.com/yahoo_rss_feeds/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

catagory = soup.find("h2", {"id": "rssfsbhead"}).text.strip()
print(catagory)

alldata = soup.find('div', {'class': 'fsb v4 fsbbr_new'})
feed_headings = alldata.findAll("h3", {'class': 'feed_heading'})

# Check if the CSV file already exists
csv_file_exists = os.path.isfile('feeds.csv')

# Open the CSV file in append mode, creating it if necessary
with open('feeds.csv', mode='a', newline='') as csv_file:
    # Define the column names to be written to the CSV file
    fieldnames = ['catagory','Feed Name', 'Location', 'Feed URL', 'Site URL', 'Facebook Followers', 'Twitter Followers', 'Instagram Followers','post count', 'Description']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # If the CSV file doesn't exist yet, write the column names as the header row
    if not csv_file_exists:
        writer.writeheader()
    
    # Iterate over each feed and write its data to the CSV file
    for feed in feed_headings:
        # Extract the Name
        feed_name = feed.find("a").text.strip()

        # Extract other details (location,feed_url, site_url, twitter_follow, instagram_follow, instagram_follow)
        detail = feed.find_next("p")
        location = detail.find("span",class_ = "location_new")
        if location is not None:
            location = location.text
        else:
            location = "N/A"
            
        feed_url = detail.find("a",class_ = "ext")["href"] if detail.find("a",class_ = "ext") else "N/A"
        site_url = detail.find("a",class_ = "extdomain")["href"] if detail.find("a",class_ = "extdomain") else "N/A"
        fb_follow  = detail.find("span", class_ ="fs-facebook")
        fb_follow = fb_follow.text.strip() if fb_follow else "N/A"
        twitter_follow = detail.find("span", class_ ="fs-twitter")
        twitter_follow = twitter_follow.text.strip() if twitter_follow else "N/A"
        instagram_follow = detail.find("span", class_ ="fs-instagram")
        instagram_follow = instagram_follow.text.strip() if instagram_follow else "N/A"
        post_count = detail.find("span", class_ ="fs-frequency")
        post_count = post_count.text.strip() if post_count else "N/A"
        discription = detail.find('a', class_= "extdomain ext").next_sibling.next_sibling.strip() if detail.find('a', class_= "extdomain ext") else "N/A"

        # Write the data to the CSV file
        writer.writerow({
            'catagory': catagory,
            'Feed Name': feed_name,
            'Location': location,
            'Feed URL': feed_url,
            'Site URL': site_url,
            'Facebook Followers': fb_follow,
            'Twitter Followers': twitter_follow,
            'Instagram Followers': instagram_follow,
            'post count' : post_count,
            'Description': discription
        })


