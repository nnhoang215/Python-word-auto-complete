from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


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
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED


        dummy_word = WordFrequency(word, 0)
        index = bisect.bisect_left(self.words, dummy_word)

        if index < len(self.words) and self.words[index].word == word:
            return self.words[index].frequency
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED

        index = bisect.bisect_left(self.words, word_frequency)

        if index < len(self.words) and self.words[index].word == word_frequency.word:
            return False  # Word already exists
        self.words.insert(index, word_frequency)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED

        dummy_word = WordFrequency(word, 0)
        index = bisect.bisect_left(self.words, dummy_word)

        if index < len(self.words) and self.words[index].word == word:
            del self.words[index]
            return True
        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        dummy_word = WordFrequency(prefix_word, 0)
        index = bisect.bisect_left(self.words, dummy_word)
        autocomplete_list = []

        for word_freq in self.words[index:]:
            if word_freq.word.startswith(prefix_word):
                autocomplete_list.append(word_freq)
            else:
                break

        autocomplete_list.sort(key=lambda x: x.frequency, reverse=True)
        return autocomplete_list[:3]
