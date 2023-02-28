import requests
from bs4 import BeautifulSoup
import spotipy, os
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ.get(SPOTIPY_CLIENT_ID)
SPOTIPY_CLIENT_SECRET = os.environ.get(SPOTIPY_CLIENT_SECRET)
SPOTIPY_REDIRECT_URI = "http://example.com"


date = input("What year would you like to travel to in YYYY-MM-DD?")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_list = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_list]

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    scope=scope,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)