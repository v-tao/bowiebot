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

items = list(word_frequency_dictionary.items())
items.sort(key=lambda x: -x[1])

total_words = sum(list(map(lambda x: x[1], items)))

# From Wikipedia
english_100_most_common_words = list(map(lambda x: x.lower(),[
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
]))

bowie_100_most_common_words = list(map(lambda x: x[0], items[:100]))

unique = set(bowie_100_most_common_words) - set(english_100_most_common_words)
