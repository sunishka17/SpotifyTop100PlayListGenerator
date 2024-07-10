import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth

date = input("Enter the date you want to go back to (YYYY-MM-DD): ")

sp_oauth = spotipy.Spotify(
    auth_manager=SpotifyOAuth
    (scope="my scope",
     redirect_uri="my uri",
     client_id='my client id',
     client_secret='my client secret'
     )
)

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")
songs_all = [song.getText().strip() for song in soup.select("li ul li h3")]

user = sp_oauth.current_user()['id']  # Get the current user's Spotify ID

songs = []
year = date.split('-')[0]
for item in songs_all:
    result = sp_oauth.search(q=f"track:{item} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs.append(uri)
    except IndexError:
        print(f'{item} doesnt exists')

# Create a new playlist with the collected URIs
p_id = sp_oauth.user_playlist_create(user=user, name=f"Taking you back to {date}", public=False)
sp_oauth.playlist_add_items(playlist_id=p_id['id'],items=songs)
