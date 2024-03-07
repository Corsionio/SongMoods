#   Author: Corso Montuori
#   Date: 3/4/2024
#   Version: 1.1

import values
import songColor
from flask import Flask, request, render_template

app = Flask(__name__)

# Route to the home page, renders the home page
@app.route('/', methods =["GET", "POST"])
def home():
    return render_template('index.html')

# Route to the song page, sends RGB values to song page 
@app.route('/song', methods=["GET", "POST"])
def song():
    
    # values
    song = None
    image_url = None
    red = 0
    green = 0
    blue = 0
    
    
    if request.method=="POST":
        song = request.form.get("song")
    
    if(song != None):
        # Gets all song values from the back-end values.py 
        # files and assigns them
        track_info = values.search_for_song(song)
        token = values.get_token()
        song_name = values.get_song_name(song)
        song_valence = values.get_valence(song)
        song_tempo = values.get_tempo(song)
        song_instrumentalness = values.get_instrumentalness(song)
        song_energy = values.get_energy(song)
        song_danceability = values.get_danceability(song)
        song_mode = values.get_mode(song)
        
        # Converst the values to RGB values through the algorithm in songColor.py
        red, green, blue = songColor.songAlgo(song_valence, song_tempo, song_instrumentalness, 
                                              song_energy, song_danceability, song_mode)
        
        # Gets image_url
        image_url = values.get_spotify_image_url(song)


    return render_template('song.html', song=song_name,  image_url=image_url, red = red, green = green, blue = blue)
 
if __name__ == '__main__':
   app.run(debug=True)
