from datetime import date as d
import requests as r
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import dotenv
from pathlib import Path


# Environment variables
dotenv.load_dotenv(
    Path("path to .env"))
spotify_id = os.environ["SPOTIFY_ID"]
spotify_secret = os.environ["SPOTIFY_SECRET"]
spotify_uri = os.environ["SPOTIFY_URI"]
spotify_userid = os.environ["SPOTIFY_USERID"]


# Date input
def get_date(msg="Which year do you want to travel to?(YYYY-MM-DD) "):
    while True:
        try:
            return d.fromisoformat(f"{input(msg)}")
        except ValueError:
            print("Be sure the date is in the correct format.")
            continue


date = get_date()
# print(date)


# Billboard 100
def get_billboard_data(date):
    billboard_data = []
    billboard_soup = BeautifulSoup(
        r.get(f"https://www.billboard.com/charts/hot-100/{date}/").text, "html.parser")
    for track in billboard_soup.find_all(name="h3", class_="a-no-trucate"):
        billboard_data.append({
            "track": f"{track.getText().strip()}",
            "artist": f"{track.find_next_sibling('span').getText().strip()}"}
        )
    return billboard_data


playlist_data = get_billboard_data(date)
# print(playlist_data)


# Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_id,
    client_secret=spotify_secret,
    redirect_uri=spotify_uri,
    scope="playlist-modify-private",
    cache_path="path to token.txt"
))


# Get Spotify tracks' uri
def get_spotify_track_uri(item, year=date.year):
    uri_search = sp.search(
        type="track", q=f"track: {item['track']} year: {year}")
    return {"uri": uri_search["tracks"]["items"][0]["uri"].split(":")[-1]}


for _ in playlist_data:
    try:
        _.update(get_spotify_track_uri(_))
    except IndexError:
        print(f"{_['track']} not found")
# print(playlist_data)


# Create Spotify playlist
def create_spotify_playlist(name, user=spotify_userid):
    playlist = sp.user_playlist_create(user=user, name=name, public=False)
    return playlist["id"]


# Add tracks into the new playlist
def add_tracks_spotify_playlist(user=spotify_userid, playlist=create_spotify_playlist(name="Billboard 100"), tracks_uri=[item["uri"] for item in playlist_data if "uri" in item.keys()]):
    sp.user_playlist_add_tracks(
        user=user, playlist_id=playlist, tracks=tracks_uri)


add_tracks_spotify_playlist()
