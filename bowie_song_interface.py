import os


class Song:
    def __init__(self, file_path):

        file_name = file_path.split("/")[-1]

        track_number_and_title = (file_name.split(".")[0])
        self.track_number = int(track_number_and_title.split("_")[0])
        self.title = " ".join(track_number_and_title.split("_"))[1:]
        self.text = open(file_path, 'r').read()

    def __repr__(self):
        return self.title


class Album:
    def __init__(self, directory):

        directory_name = directory.split("/")[-1]

        self.title = directory_name[4:]
        self.year = directory_name[:4]
        self.sides = []
        self.songs = {}

        self.load_songs_from_album_directory(directory)

    def load_songs_from_album_directory(self, directory):
        files = list(os.walk(directory))

        self.sides = files[0][1]
        for side in self.sides:

            side_files = list(os.walk(directory + f"/{side}"))

            self.songs[side] = [Song(directory + f"/{side}/" + song_file) for song_file in side_files[0][2]]

        if files[0][2] != []:
            self.songs['No_Side'] = [Song(directory + "/" + song_file) for song_file in files[0][2]]


    def side_as_str(self, side):
        return "".join([f'\n>>>>>> {song}' for song in self.songs[side]])


    def __repr__(self):
        headline = f"{self.year:<4}: {self.title}"
        sides = "".join([f"\n>>> {side} {self.side_as_str(side)}" for side in self.sides])
        return headline + sides