from bowie_song_interface import BowieData
from bowie_song_generator import BowieSongGenerator

bowie_data = BowieData("./data")

songs = bowie_data.get_songs()
non_instrumental_songs = list(filter(lambda song: (song.text.strip() != ""), songs))

longest_song = max(non_instrumental_songs, key=lambda x: len(x.text))
shortest_song = min(non_instrumental_songs, key=lambda x: len(x.text))


non_instrumental_generator = BowieSongGenerator(
    bowie_data_directory="./data", look_behind_length=2, 
    filter_key=lambda song: (song.text.strip() != "")
    )

fire_generator = BowieSongGenerator(
    bowie_data_directory="./data", look_behind_length=2, 
    filter_key=lambda song: "fire" in song.text
    )

death_generator = BowieSongGenerator(
    bowie_data_directory="./data", look_behind_length=2, 
    filter_key=lambda song: "death" in song.text
    )
