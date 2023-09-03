from time import perf_counter_ns
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.root = TrieNode()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        for word_freq in words_frequencies:
            current = self.root
            word = word_freq.word

            for letter in word:
                if letter not in current.children:
                    current.children[letter] = TrieNode(letter)
                current = current.children[letter]

            current.is_last = True
            current.frequency = word_freq.frequency


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        time_1 = perf_counter_ns()
        node = self._traverse_word(word)
        if node and node.is_last:
            time_2 = perf_counter_ns()
            print("Search:", time_2 - time_1)
            return node.frequency
        time_3 = perf_counter_ns()
        print("Search:", time_3 - time_1)
        return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        time_1 = perf_counter_ns()
        current = self.root
        word = word_frequency.word

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]

        if current.is_last:
            time_2 = perf_counter_ns()
            print("Add:", time_2 - time_1)
            return False

        current.is_last = True
        current.frequency = word_frequency.frequency
        time_3 = perf_counter_ns()
        print("Add:", time_3 - time_1)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        time_1 = perf_counter_ns()
        node = self._traverse_word(word)
        if node and node.is_last:
            node.is_last = False
            time_2 = perf_counter_ns()
            print("Delete:", time_2 - time_1)
            return True
        time_3 = perf_counter_ns()
        print("Delete:", time_3 - time_1)
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        time_1 = perf_counter_ns()
        node = self._traverse_word(word)
        if not node:
            time_2 = perf_counter_ns()
            print("Autocomplete:", time_2 - time_1)
            return []

        autocomplete_list = []
        self._collect_autocomplete_words(node, word, autocomplete_list)
        autocomplete_list.sort(key=lambda x: x.frequency, reverse=True)
        time_3 = perf_counter_ns()
        print("Autocomplete:", time_3 - time_1)
        return autocomplete_list[:3]

    def _traverse_word(self, word: str) -> TrieNode:
        current = self.root

        for letter in word:
            if letter not in current.children:
                return None
            current = current.children[letter]

        return current

    def _collect_autocomplete_words(self, node: TrieNode, word_prefix: str, result_list: list):
        if node.is_last:
            result_list.append(WordFrequency(word_prefix, node.frequency))
        for letter, child_node in node.children.items():
            self._collect_autocomplete_words(
                child_node, word_prefix + letter, result_list)
