#   Author: Corso Montuori
#   Date: 3/4/2024
#   Version: 1.1

def songAlgo(song_valence, song_tempo, song_instrumentalness, 
             song_energy, song_danceability, song_mode):
        red = 0
        green = 0
        blue = 0
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
            
        return red, green, blue