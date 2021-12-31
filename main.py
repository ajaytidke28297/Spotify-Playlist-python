from bs4 import BeautifulSoup
import requests
from requests.models import Response

# Billboard URL
BILL_BOARD_URL = 'https://www.billboard.com/charts/hot-100/'

date = input("What year would you like to travel to in YYYY-MM-DD: ")

BILL_BOARD_DATE_URL = f"{BILL_BOARD_URL}{date}"

response = requests.get(BILL_BOARD_URL)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_titles = soup.select("h3.a-no-trucate.a-font-primary-bold-s")
song_names = [title.getText().strip() for title in all_titles]
print(song_names)
