import values
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

#result = values.search_for_artist(token, "Radiohead")
#print(result["name"])
#artist_id = result["id"]
#songs = values.get_songs_by_artist(token, artist_id)

#print(songs)

"""for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")"""
    
@app.route('/', methods =["GET", "POST"])
def home():
            

    #return render_template('index.html', valence = song_valence)
    return render_template('index.html')

@app.route('/song', methods=["GET", "POST"])
def song():
    song = None
    image_url = None
    red = 0
    green = 0
    blue = 0
    if request.method=="POST":
        song = request.form.get("song")
    
    if(song != None):
        print("song name is " + song)

        track_info = values.search_for_song("Riff 2")
        token = values.get_token()
        song_valence = values.get_valence(song)
        song_time_signature = values.get_time_signature(song)
        song_tempo = values.get_tempo(song)
        song_instrumentalness = values.get_instrumentalness(song)
        song_energy = values.get_energy(song)
        song_danceability = values.get_danceability(song)
        
        # SONG VALENCE #
        # Song valence RGB value changes
        green += song_valence * 2
        red -= song_valence
        
        # TIME SIGNATURE #
        # input time signature here after understanding it
        
        # SONG TEMPO #
        # Song tempo edits and rgb value changes
        song_tempo / 100
        print("new song tempo", song_tempo)
        if(song_tempo > 0.80):
            blue -= song_tempo
            red += song_tempo / 2
            green += song_tempo
        elif(song_tempo < 0.80):
            blue += song_tempo * 1.2
            red -= song_tempo
        
        
        # SONG INSTRUMENTALNESS #
        # Song instrumentalness RGB changes
        blue += song_instrumentalness * 2
        green += song_instrumentalness
        
        # SONG ENERGY #
        # Song energy edits and RGB changes
        if(song_energy >= 0.6 and song_valence <= 0.3):
            # accounts for metal or rock
            red += song_energy * 3
        elif(song_energy >= 0.6 and song_valence <= 0.4):
            red += song_energy * 2
        elif(song_energy <= 0.6):
            green += song_energy
            blue += song_energy / 2
            red += song_energy / 2
        
        # SONG DANCEABILITY # 
        # Song energy and RGB changes
        green += song_danceability * 2
        blue += song_danceability

        print(track_info)
        print(token)
        print(song_valence)
        print(song_time_signature)
        print(song_tempo)
        print(song_instrumentalness)
        print(song_energy)
        print(song_danceability)
        
        image_url = values.get_spotify_image_url(song)


    return render_template('song.html',  image_url=image_url, red = red, green = green, blue = blue)

 
if __name__ == '__main__':
   app.run(debug=True)
