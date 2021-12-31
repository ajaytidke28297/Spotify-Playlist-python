from bs4 import BeautifulSoup
import requests
from requests.models import Response
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

print(f"Client: {SPOTIFY_CLIENT_ID}\nSecret: {SPOTIFY_CLIENT_SECRET}")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()['id']

print(f"User id: {user_id}")

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
