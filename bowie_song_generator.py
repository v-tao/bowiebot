import random


from bowie_song_interface import BowieData

class BowieSongGenerator(BowieData):
    def __init__(self, bowie_data_directory, look_behind_length=2):
        super().__init__(bowie_data_directory=bowie_data_directory)

        self._look_behind_length = look_behind_length
        self._look_behind = {}

        for album in self.albums:
            for song in album.get_songs():

                lines = song.text.split("\n")

                prev_words = ["%" * i for i in range(1,self._look_behind_length + 1)]
                for i in range(len(lines)):

                    line = lines[i]
                    suffix = ["@" * i for i in range(1,self._look_behind_length + 1)] if i < len(lines) - 1 else ["%" * i for i in range(1,self._look_behind_length + 1)]
                    words = list(map(lambda x: x.lower(), line.split(" "))) + suffix

                    for word in words:
                        prev_words_tuple = tuple(prev_words)

                        if prev_words_tuple in self._look_behind:
                            self._look_behind[prev_words_tuple] += [word]
                        else:
                            self._look_behind[prev_words_tuple] = [word]

                        prev_words.pop(0)
                        prev_words.append(word)

    def generate_song(self):

        generated_song = ""

        prev_words = ["%" * i for i in range(1,self._look_behind_length + 1)]
        while True:
            prev_words_tuple = tuple(prev_words)

            next_word = random.choice(self._look_behind[prev_words_tuple])

            if "%" in next_word:
                if next_word.count("%") == 0:
                    generated_song += next_word + " "
                    prev_words.append(next_word)
                elif next_word.count("%") == self._look_behind_length - 1:
                    generated_song += "\n\n"
                    prev_words.append(next_word)
                    break
                else:
                    prev_words.append(next_word)

            elif "@" in next_word:
                if next_word.count("@") == 0:
                    generated_song += next_word + " "
                    prev_words.append(next_word)
                elif next_word.count("@") == self._look_behind_length - 1:
                    generated_song += "\n"
                    prev_words.append(next_word)
                else:
                    prev_words.append(next_word)
            
            else:
                generated_song += next_word + " "
                prev_words.append(next_word)

            prev_words.pop(0)

        return generated_song

class AdvancedBowieSongGenerator(BowieData):
    def __init__(self, bowie_data_directory, look_behind_length=2):
        super().__init__(bowie_data_directory=bowie_data_directory)

        self._look_behind_length = look_behind_length
        self._look_behind = {}

        for album in self.albums:
            for song in album.get_songs():

                lines = song.text.split("\n")

                prev_words = ["%" * i for i in range(1,self._look_behind_length + 1)]
                for i in range(len(lines)):

                    line = lines[i]
                    suffix = ["@" * i for i in range(1,self._look_behind_length + 1)] if i < len(lines) - 1 else ["%" * i for i in range(1,self._look_behind_length + 1)]
                    words = list(map(lambda x: x.lower(), line.split(" "))) + suffix

                    for word in words:
                        prev_words_tuple = tuple(prev_words)

                        if prev_words_tuple in self._look_behind:
                            self._look_behind[prev_words_tuple] += [word]
                        else:
                            self._look_behind[prev_words_tuple] = [word]

                        prev_words.pop(0)
                        prev_words.append(word)

    def generate_song(self):

        generated_song = ""

        prev_words = ["%" * i for i in range(1,self._look_behind_length + 1)]
        while True:
            prev_words_tuple = tuple(prev_words)

            next_word = random.choice(self._look_behind[prev_words_tuple])

            if "%" in next_word:
                if next_word.count("%") == 0:
                    generated_song += next_word + " "
                    prev_words.append(next_word)
                elif next_word.count("%") == self._look_behind_length - 1:
                    generated_song += "\n\n"
                    prev_words.append(next_word)
                    break
                else:
                    prev_words.append(next_word)

            elif "@" in next_word:
                if next_word.count("@") == 0:
                    generated_song += next_word + " "
                    prev_words.append(next_word)
                elif next_word.count("@") == self._look_behind_length - 1:
                    generated_song += "\n"
                    prev_words.append(next_word)
                else:
                    prev_words.append(next_word)
            
            else:
                generated_song += next_word + " "
                prev_words.append(next_word)

            prev_words.pop(0)

        return generated_song

    