from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load .env file in current directory
load_dotenv()

# Print environment variables to verify they're loaded
print("Client ID:", os.getenv("SPOTIPY_CLIENT_ID"))
print("Client Secret:", os.getenv("SPOTIPY_CLIENT_SECRET"))
print("Redirect URI:", os.getenv("SPOTIPY_REDIRECT_URI"))

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-library-read"
))

# Test request: Get current user’s saved tracks count
results = sp.current_user_saved_tracks(limit=1)
print("Number of saved tracks (sample):", results['total'])
