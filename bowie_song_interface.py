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
    def __init__(self, album_directory):

        directory_name = album_directory.split("/")[-1]

        self.album_directory = album_directory
        self.title = directory_name[4:]
        self.year = int(directory_name[:4])
        self.sides = []
        self._songs = {}

        self._load_songs_from_album_directory()

    def get_songs(self):
        songs = []

        for side in self.sides:
            songs += self._songs[side]

        return songs

    def _load_songs_from_album_directory(self):
        files = list(os.walk(self.album_directory))

        self.sides = files[0][1]
        for side in self.sides:

            side_files = list(os.walk(self.album_directory + f"/{side}"))

            songs = [Song(self.album_directory + f"/{side}/" + song_file) for song_file in side_files[0][2]]
            songs.sort(key=lambda x: x.track_number)
            self._songs[side] = songs

        if files[0][2] != []:
            self.sides.append("No_Side")
            songs = [Song(self.album_directory + "/" + song_file) for song_file in files[0][2]]
            songs.sort(key=lambda x: x.track_number)
            self._songs['No_Side'] = songs

        self.sides.sort()

    def _side_as_str(self, side):
        return "".join([f'\n>>>>>> {song}' for song in self._songs[side]])


    def __repr__(self):
        headline = f"{self.year:<4}: {self.title}"
        sides = "".join([f"\n>>> {side} {self._side_as_str(side)}" for side in self.sides])
        return headline + sides

class BowieData:
    def __init__(self, bowie_data_directory):

        self.bowie_data_directory = bowie_data_directory
        self.albums = []

        self._load_albums_from_bowie_data_directory()

        self.songs = self.get_songs()

    def get_songs(self):
        return [song for album in self.albums for song in album.get_songs()]

    def _load_albums_from_bowie_data_directory(self):
        files = list(os.walk(self.bowie_data_directory))

        data_directory, album_folder_names, _ = files[0]

        for album_folder_name in album_folder_names:

            self.albums.append(Album(data_directory + "/" + album_folder_name))

        self.albums.sort(key=lambda x: x.year)

    def __repr__(self):
        headline = f"BOWIE ALBUM DATA:\n"
        sides = "".join([f"\n#####\n{album}" for album in self.albums])
        return headline + sides
