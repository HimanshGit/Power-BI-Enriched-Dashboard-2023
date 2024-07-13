import pandas as pd
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Replace these with your Spotify API credentials
CLIENT_ID = '86743976a6cd49fbb9838e2907969b33'
CLIENT_SECRET = '839eea6ead6e4b78bef5f6ef3db57625'

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Load the dataset
file_path = 'spotify-2023.csv'  # Adjust the path as necessary
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Function to get album cover URL
def get_album_cover_url(track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    result = sp.search(q=query, type='track', limit=1)
    if result['tracks']['items']:
        return result['tracks']['items'][0]['album']['images'][0]['url']
    return None

# Add a new column for album cover URLs
spotify_data['album_cover_url'] = spotify_data.apply(
    lambda row: get_album_cover_url(row['track_name'], row['artist(s)_name']), axis=1)

# Save the updated dataset to a new CSV file
spotify_data.to_csv('spotify-2023-with-covers.csv', index=False)

print("Album cover URLs have been added to the dataset.")
