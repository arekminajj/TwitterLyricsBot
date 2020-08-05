import lyricsgenius
from random import randrange
import time
import tweepy

genius = lyricsgenius.Genius("")
genius.remove_section_headers = True
artist = genius.search_artist("artist", max_songs=999, sort="title")

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth)

while True:
    try:
        #GENIUS API PART
        song_title = artist.songs[randrange(artist.num_songs+1)].title
        print(song_title)
        song = genius.search_song(song_title, artist.name)
        numberoflines = len(song.lyrics.splitlines())
        barLine = randrange(numberoflines-1)

        #TEST
        print (song.lyrics.splitlines()[barLine])
        print (song.lyrics.splitlines()[barLine+1])
        print(barLine)
        print(numberoflines)

        #TWEET IT
        tweet_message = song.lyrics.splitlines()[barLine] + ' ' + song.lyrics.splitlines()[barLine+1] + ' ~ ' + artist.name
        api.update_status(tweet_message)

        time.sleep(120)
    except:
        print("Something went wrong, trying again :(")
        continue