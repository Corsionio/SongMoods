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

        track_info = values.search_for_song(song)
        token = values.get_token()
        song_name = values.get_song_name(song)
        song_valence = values.get_valence(song)
        song_time_signature = values.get_time_signature(song)
        song_tempo = values.get_tempo(song)
        song_instrumentalness = values.get_instrumentalness(song)
        song_energy = values.get_energy(song)
        song_danceability = values.get_danceability(song)
        song_mode = values.get_mode(song)
        
        #######################################
        #             RGB ALGORITHM           #
        #######################################

        # SONG VALENCE #
        # Song valence RGB value changes
        song_valence *= 100
        if(song_valence <= 60):
            blue += 100 + song_valence
        elif(song_valence >= 60):
            green += song_valence
            blue += song_valence / 2
            green += song_valence
        elif(song_valence >= 85):
            green += song_valence * 1.2
            red += song_valence / 3
        
        # TIME SIGNATURE #
        # input time signature here after understanding it
        
        # SONG TEMPO #
        # Song tempo edits and rgb value changes
        print("new song tempo", song_tempo)
        if(song_tempo >= 120):
            blue -= song_tempo
            red += song_tempo
            green -= song_tempo
        elif(song_tempo >= 80):
            blue -= song_tempo
            red += song_tempo
            green += song_tempo / 2
        elif(song_tempo <= 80):
            blue += song_tempo * 2
            red += song_tempo
        
        
        # SONG INSTRUMENTALNESS #
        # Song instrumentalness RGB changes
        song_instrumentalness *= 100
        blue += song_instrumentalness * 2
        green += song_instrumentalness
        
        # SONG ENERGY #
        # Song energy edits and RGB changes
        song_energy *= 100
        if(song_energy >= 60 and song_valence <= 28):
            # For cases when a song is faster and very sad
            # accounts for metal or rock
            red += song_energy * 2
            blue += song_energy * 3
        elif(song_energy >= 60 and song_valence <= 40):
            # For cases when a song is faster and sad
            red += song_energy * 2
            blue += song_energy * 2
        elif(song_energy <= 60 and song_valence >= 50):
            # For cases when a song is slower but happy
            green += 80 + song_energy
            red += song_energy
        elif(song_energy <= 60):
            # for cases when a song is slower and not happy
            green += song_energy
            blue += 80 + song_energy * 2
        elif(song_energy >= 60):
            # for cases when a song is faster and happy
            green += song_energy
            red += song_energy
            blue -= song_energy
        
        print("red after energy", red)
        print("green after energy", green)
        print("blue after energy", blue)
        # SONG DANCEABILITY # 
        # Song energy and RGB changes
        song_danceability *= 100
        if(song_danceability < 60):
            blue += 60 + song_danceability
        else:
            green += song_danceability * 2
            blue += song_danceability
            red += song_danceability / 2
        
        #If the mode confidence is above or below an arbitrary value:
        if(song_mode == 0 and song_valence <= 0.35):
            blue += 100 * 1.5
        if(song_mode == 1 and song_valence >= 0.65):
            green += 100 * 1.5
        
        # Keeps RGB between 0 and 255
        if(red <= 0):
            red = 0
        if(green <= 0):
            green = 0
        if(blue <= 0):
            blue = 0
        if(blue >= 255):
            blue = 255
        if(green >= 255):
            green = 255
        if(red >= 255):
            red = 255
        print("##########################################################")
        print("Track Info --> ", track_info)
        print("Song Token --> ", token)
        print("Song Name --> ", song_name)
        print("Song Valence --> ", song_valence)
        print("Time Signature --> ", song_time_signature)
        print("Song Tempo --> ", song_tempo)
        print("Song Instrumentalness --> ", song_instrumentalness)
        print("Song Energy --> ", song_energy)
        print("Song Danceability --> ", song_danceability)
        print("-> Red Before sub <-", red)
        print("-> Green Before sub <-", green)
        print("-> Blue Before sub <-", blue)
        print("##########################################################")
        
        image_url = values.get_spotify_image_url(song)


    return render_template('song.html', song=song_name,  image_url=image_url, red = red, green = green, blue = blue)
 
if __name__ == '__main__':
   app.run(debug=True)
