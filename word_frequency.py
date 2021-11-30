from bowie_song_interface import BowieData

bowie_data = BowieData("./data")

word_frequency_dictionary = {}

for album in bowie_data.albums:
    for song in album.get_songs():
        lines = song.text.split("\n")
        words = []
        for line in lines:
            words += line.split(" ")
        for word in words:
            if word.lower() in word_frequency_dictionary:
                word_frequency_dictionary[word.lower()] += 1
            else:
                word_frequency_dictionary[word.lower()] = 1

