import feedparser
import time
from datetime import datetime
import pytz

# define the time zone you want to use
tz = pytz.timezone('Asia/Kolkata')

feed_url = "https://news.google.com/rss/search?q=ndtv&hl=en-IN&gl=IN&ceid=IN:en"
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
                # print the entry title, link, and time
                published_time = getattr(entry, 'published_parsed', None)
                if published_time:
                    published_time = datetime.fromtimestamp(time.mktime(published_time)).astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")
                else:
                    published_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                count += 1
                print(f"{count} {published_time}: {entry.title}: {entry.link}")
                # add the link to the printed_entries set
                printed_entries.add(entry.link)

        # update the last_checked time to the latest entry
        if feed.entries:
            last_checked = feed.entries[0].published_parsed

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # wait for a minute before checking again
    time.sleep(60)


