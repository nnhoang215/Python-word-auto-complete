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
        self.root = TrieNode()

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word_freq in words_frequencies:

            # Starting from the root
            current = self.root
            word = word_freq.word

            # Add letter in the word as a trie node if it does not exists in the trie
            for letter in word:
                if letter not in current.children:
                    current.children[letter] = TrieNode(letter)

                # Assign the current letter to its parent node
                current = current.children[letter]

            # Set the node containing the last letter 
            current.is_last = True
            current.frequency = word_freq.frequency


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # traverse the trie to find the word
        node = self._traverse_word(word)

        # Return the word if found
        # (Found the nodes corresponds to the letters and the node contains 
        # the last character is last node in a word) 
        if node and node.is_last:
            return node.frequency
        
        return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # Starting from the root
        current = self.root
        word = word_frequency.word

        # Add letter in the word as a trie node if it does not exists in the trie
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter)
            current = current.children[letter]

        # Return false if found the word already exists in the trie
        if current.is_last:
            return False

        # Otherwise, add it to the trie, set the node containing the last letter
        current.is_last = True
        current.frequency = word_frequency.frequency
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        # traverse the trie to find the deleted word
        node = self._traverse_word(word)

        # Delete the word if found and return true
        if node and node.is_last:
            node.is_last = False
            return True
        
        # Return false if do not found it
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # traverse the trie to find the prefix word
        node = self._traverse_word(word)

        # If do not find the prefix word, return an empty array
        if not node:
            return []

        autocomplete_list = []

        # If found, run the function to get the words starting with that prefix
        self._collect_autocomplete_words(node, word, autocomplete_list)

        # Sort the possible words list in reverse order
        autocomplete_list.sort(key=lambda x: x.frequency, reverse=True)

        return autocomplete_list[:3]

    def _traverse_word(self, word: str) -> TrieNode:
        # Starting from the root
        current = self.root

        # traverse the trie based on the letters in the word 
        for letter in word:
            if letter not in current.children:
                return None
            current = current.children[letter]

        return current

    def _collect_autocomplete_words(self, node: TrieNode, word_prefix: str, result_list: list):
        # Base case: Append the word to the result list if facing a node is marked as
        # the last node in a word
        if node.is_last:
            result_list.append(WordFrequency(word_prefix, node.frequency))

        # Recursive calls: traverse along all the children of the prefix node to find
        # all the words starting with that prefix
        for letter, child_node in node.children.items():
            self._collect_autocomplete_words(
                child_node, word_prefix + letter, result_list)
