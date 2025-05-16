import os
import random
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv

# Load .env
load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("b99300717b104e2c940f4284dcc541cc"),
    client_secret=os.getenv("ff431dd1919943f886627c4b305f7fb7"),
    redirect_uri=os.getenv("http://127.0.0.1:8899/callback"),
    scope="user-library-read playlist-read-private"
))

def get_playlist_tracks(sp, playlist_id):
    results = sp.playlist_items(playlist_id)
    tracks = results["items"]
    return [t["track"]["name"] for t in tracks if t["track"]]

def play_game():
    print("🎵 Welcome to Spotify Game Show! 🎵")
    playlist_id = input("Paste a public Spotify playlist ID (not link): ").strip()
    tracks = get_playlist_tracks(sp, playlist_id)

    if len(tracks) < 4:
        print("Not enough tracks for the game.")
        return

    options = random.sample(tracks, 4)
    answer = random.choice(options)

    print("\nGuess which of these songs is randomly picked:")
    for i, song in enumerate(options, 1):
        print(f"{i}. {song}")

    guess = input("Your choice (1-4): ").strip()
    if options[int(guess) - 1] == answer:
        print("✅ Correct!")
    else:
        print(f"❌ Nope! It was: {answer}")

if __name__ == "__main__":
    play_game()
# This is a simple game where the user guesses the artist of a song from a Spotify playlist.