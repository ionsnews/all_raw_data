import feedparser
import time
from datetime import datetime
import pytz
import csv

# define the time zone you want to use
tz = pytz.timezone('Asia/Kolkata')

def read_rss_urls_from_csv(filename):
    rss_urls = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rss_urls.append((row['COUNTRY'], row['CATEGORY'], row['RSS-URL']))
    return rss_urls

def process_feed(country, category, feed_url):
    last_checked = None
    printed_entries = set()
    count = 0
    
    while True:
        try:
            # fetch the feed
            feed = feedparser.parse(feed_url)

            # iterate over the entries in the feed
            for entry in feed.entries:
                # check if this entry is new and not already printed
                if (last_checked is None or entry.published_parsed > last_checked) and entry.link not in printed_entries:
                    # print the entry title, link, time, country, and category
                    published_time = getattr(entry, 'published_parsed', None)
                    if published_time:
                        published_time = datetime.fromtimestamp(time.mktime(published_time)).astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        published_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                    count += 1
                    print(f"{count} {published_time}: {country}, {category}: {entry.title}: {entry.link}")
                    # add the link to the printed_entries set
                    printed_entries.add(entry.link)

            # update the last_checked time to the latest entry
            if feed.entries:
                last_checked = feed.entries[0].published_parsed

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        # wait for a 5 mins before checking again
        #time.sleep(5*60)

if __name__ == "__main__":
    rss_urls = read_rss_urls_from_csv("rss_urls.csv")
    for country, category, url in rss_urls:
        print(f"Processing feed from Country: {country}, Category: {category}, URL: {url}")
        process_feed(country, category, url)
        # Wait for 1 second before processing the next URL
        #time.sleep(1)

