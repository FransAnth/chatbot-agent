import requests
from bs4 import BeautifulSoup

url = 'https://billease.ph/faq/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raises an exception for HTTP errors

    soup = BeautifulSoup(response.text, 'html.parser')
    page_content = soup.prettify()

    with open("billease_faq.html", "w", encoding="utf-8") as file:
        file.write(page_content)

    print("Page content saved successfully.")

except requests.RequestException as e:
    print(f"Request failed: {e}")
