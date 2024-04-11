import requests

def get_pagespeed_data(url):
    api_key = "AIzaSyBM83_ATgn9YUCNKcVTFwUwSycp3X68BOU"  # Replace with your actual API key

    params = {
        'url': url,
        'key': api_key,
    }

    api_url = "https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed"

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad responses

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def print_pagespeed_data(data):
    print(data)
    if data:
        # Extract and print the relevant information from the API response
        lighthouse_data = data.get('lighthouse', {})
        categories = lighthouse_data.get('categories', {})

        for category_name, category_data in categories.items():
            print(f"{category_name}: {category_data['score']}")

        # Additional information you may want to extract
        # Uncomment the lines below if needed
        # performance_score = lighthouse_data.get('audits', {}).get('performance', {}).get('score')
        # print(f"Performance Score: {performance_score}")

        # more_info = lighthouse_data.get('audits', {}).get('metrics', {}).get('details', {})
        # print(f"More Info: {more_info}")

if __name__ == "__main__":
    website_url = "https://samyakk.com"  # Replace with your website URL
    pagespeed_data = get_pagespeed_data(website_url)

    if pagespeed_data:
        print_pagespeed_data(pagespeed_data)
