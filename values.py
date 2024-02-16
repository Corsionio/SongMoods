from dotenv import load_dotenv
import os
import base64
from requests import post
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization" : "Bearer " + token}

"""def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1" #can do something like &type=artist,track if searching for artist and track
    
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No Artist with this name exists")
        return None
    
    return json_result[0]"""
    
def search_for_song(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    
    if(results['tracks']['items']):
        track = results['tracks']['items'][0]
        id = track['id']
        return id
    else:
        print("No results found for the track:", song_name)
        return None
    
def get_valence(song_name):
    id = search_for_song(song_name)
    if(id != 0):
        audio_features = sp.audio_features([id])
        
        if(audio_features and audio_features[0]):
            valence = audio_features[0]['valence']
            return valence
        
def get_time_signature(song_name):
    id = search_for_song(song_name)
    if(id != 0):
        audio_features = sp.audio_features([id])
        
        if(audio_features and audio_features[0]):
            time_signature = audio_features[0]['time_signature']
            return time_signature

def get_tempo(song_name):
    id = search_for_song(song_name)
    if(id != 0):
        audio_features = sp.audio_features([id])
        
        if(audio_features and audio_features[0]):
            tempo = audio_features[0]['tempo']
            return tempo
        
def get_instrumentalness(song_name):
    id = search_for_song(song_name)
    if(id != 0):
        audio_features = sp.audio_features([id])
        
        if(audio_features and audio_features[0]):
            instrumentalness = audio_features[0]['instrumentalness']
            return instrumentalness
        
def get_energy(song_name):
    id = search_for_song(song_name)
    if(id != 0):
        audio_features = sp.audio_features([id])
        
        if(audio_features and audio_features[0]):
            energy = audio_features[0]['energy']
            return energy

def get_danceability(song_name):
    id = search_for_song(song_name)
    if(id != 0):
        audio_features = sp.audio_features([id])
        
        if(audio_features and audio_features[0]):
            danceability = audio_features[0]['danceability']
            return danceability
        
def get_spotify_image_url(song_name):
    id = search_for_song(song_name)
    if(id != 0):
        track_info = sp.track(id)
        images = track_info['album']['images']
        if(images != 0):
            image_url = images[0]['url']
            return image_url
    
    print("ERROR: No image found for track")
    return None
