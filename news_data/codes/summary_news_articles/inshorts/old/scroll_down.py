import csv
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import requests


try:
# Set Chrome options to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--window-size=800,600')


    # Initialize the web driver
    driver = webdriver.Chrome(options=chrome_options)

    #caps = DesiredCapabilities().CHROME.copy()
    #caps['acceptInsecureCerts'] = True
    #driver = webdriver.Chrome(desired_capabilities=caps,options=chrome_options)

    # Navigate to the initial page with the "load more" button
    #https://www.aadhan.in/feed?gclid=Cj0KCQjwu-KiBhCsARIsAPztUF1FyEjN694FEvub6UT7Zl-sKkzNSz2kwNhrVsLPXySFg4veITECqooaAtIHEALw_wcB
    driver.get('https://www.aadhan.in/feed')
    taging = "feeds"

    # Define a function to check if the "load more" button is visible
    '''def is_button_visible():
        start_time = time.time()
        end_time = None
    '''
    '''
        try:

            button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'panel bdr-0')))
            end_time = time.time()
            print("__________________________________________________")
            print("Button Visible")
            print("button check Time waited: {:.4f} seconds".format(end_time - start_time))
            return button.is_displayed()
        except Exception as e:
            if end_time is not None:
                print("Time waited(button check error): {:.4f} seconds".format(end_time - start_time))
            return False
            print(f"Error: {e}")
    '''
    count = 0
    # Keep track of the number of news cards before and after clicking the "load more" button
    num_cards_before = len(driver.find_elements(By.CLASS_NAME, 'panel.bdr-0'))
    num_consecutive_same_card_counts = 0
    print(num_cards_before)
    try:
        while True:
            start_time = time.time()
            end_time = None
            print("entered while loop")
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #num_cards_after = len(WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'panel bdr-0'))))
            num_cards_after = len(driver.find_elements(By.CLASS_NAME, 'panel.bdr-0'))
            print(num_cards_after)
            end_time = time.time()
            print("while loop Time waited: {:.4f} seconds".format(end_time - start_time))
            count = count + 1
            print(count)
            # Wait for the news cards to load
            time.sleep(2)


            


    except Exception as e:
        print("end")
        if end_time is not None:
            print("Time waited(while loop error): {:.4f} seconds".format(end_time - start_time))
        print(f"Error: {e}")
    """
    # Get the page source after all "load more" buttons have been clicked
    print("transfer")
    page_source = driver.page_source

    # Parse the page source using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all the news cards
    news_cards = soup.find_all('div', {'class': 'news-card'})

    # Create a CSV file to store the scraped data
    with open('news.csv', mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        print("file Opened")
        # Write the header row
        writer.writerow(['taging','Headline', 'Author', 'actual_time','Time', 'Date', 'Body', 'Source Name', 'Source Link'])
        # Extract the headline, author, time, date, body, source name, and source link for each news card
        print("scraping Started")
        for card in news_cards:
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
            # Write the scraped data to the CSV file
            writer.writerow([taging,headline, author, actual_time ,time, date, body, source_name, source_link])

    # Close the web driver
    driver.quit()
"""
except Exception as e:
    print(f"Error: {e}")
