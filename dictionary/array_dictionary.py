from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect
from time import perf_counter_ns

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.words = []


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        # TO BE IMPLEMENTED
        # Need to sort this list
        self.words = sorted(words_frequencies, key=lambda wf: wf.word)


    def search(self, word: str) -> int:
        time_1 = perf_counter_ns()
    
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED

        # Create a dummy WordFrequency object for the searched word
        dummy_word = WordFrequency(word, 0)

        # Find the index to insert the dummy WordFrequency object
        index = bisect.bisect_left(self.words, dummy_word)

        # If the word in that index is the same with the searched word, the searched word is found in the list
        if index < len(self.words) and self.words[index].word == word:
            time_2 = perf_counter_ns()
            print("Search:", time_2 - time_1)
            return self.words[index].frequency
        time_3 = perf_counter_ns()
        print("Search:", time_3 - time_1)
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED

        time_1 = perf_counter_ns()
        index = bisect.bisect_left(self.words, word_frequency)

        if index < len(self.words) and self.words[index].word == word_frequency.word:
            time_2 = perf_counter_ns()
            print("Add:", time_2 - time_1)
            return False  # Word already exists
        self.words.insert(index, word_frequency)
        time_3 = perf_counter_ns()
        print("Add:", time_3 - time_1)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED
        time_1 = perf_counter_ns()
        # Create a dummy WordFrequency object for the deleted word
        dummy_word = WordFrequency(word, 0)

        # Search for that deleted word in the list, delete it if found
        index = bisect.bisect_left(self.words, dummy_word)
        if index < len(self.words) and self.words[index].word == word:
            del self.words[index]
            time_2 = perf_counter_ns()
            print("Delete:", time_2 - time_1)
            return True
        time_3 = perf_counter_ns()
        print("Delete:", time_3 - time_1)
        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        time_1 = perf_counter_ns()

        # Create a dummy WordFrequency object for the prefix word
        dummy_word = WordFrequency(prefix_word, 0)

        # Caclulate the index to insert prefix word
        index = bisect.bisect_left(self.words, dummy_word)

        # Create a list of possible words having that prefix
        autocomplete_list = []

        # Scan part of the list (starting from the position to insert prefix word) 
        for word_freq in self.words[index:]:

            # If a word starts with the prefix, append it to the possible word list
            if word_freq.word.startswith(prefix_word):
                autocomplete_list.append(word_freq)

        # Sort the list of possible words in descending order based on the word frequency
        autocomplete_list.sort(key=lambda x: x.frequency, reverse=True)

        time_2 = perf_counter_ns()
        print("Autocomplete:", time_2 - time_1)
        # Return the top 3 most possible word
        return autocomplete_list[:3]
