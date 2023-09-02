from time import perf_counter_ns
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # Initialize the linked list
        self.head = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # Sort the input list of WordFrequency objects by word
        # sorted_words_frequencies = sorted(words_frequencies, key=lambda wf: wf.word)

        # Create a linked list of nodes from the sorted list of WordFrequency objects
        for word_freq in words_frequencies:
            # Create a new node with the given WordFrequency
            new_node = ListNode(word_freq)

            # Insert the new node at the beginning of the linked list
            new_node.next = self.head
            self.head = new_node

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        time_1 = perf_counter_ns()
        current = self.head
        while current:
            if current.word_frequency.word == word:
                time_2 = perf_counter_ns()
                print("Search:", time_2 - time_1)
                return current.word_frequency.frequency
            current = current.next
        time_3 = perf_counter_ns()
        print("Search:", time_3 - time_1)
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # Check if the word is already in the dictionary
        time_1 = perf_counter_ns()
        if self.search(word_frequency.word) > 0:
            time_2 = perf_counter_ns()
            print("Add:", time_2 - time_1)
            return False

        # Create a new node with the given WordFrequency
        new_node = ListNode(word_frequency)

        # Insert the new node at the beginning of the linked list
        new_node.next = self.head
        self.head = new_node
        time_3 = perf_counter_ns()
        print("Add:", time_3 - time_1)
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when word not found
        """
        time_1 = perf_counter_ns()
        current = self.head
        prev = None

        while current:
            if current.word_frequency.word == word:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                time_2 = perf_counter_ns()
                print("Delete:", time_2 - time_1)
                return True
            prev = current
            current = current.next
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
        current = self.head
        autocomplete_list = []

        while current:
            if current.word_frequency.word.startswith(prefix_word):
                autocomplete_list.append(current.word_frequency)
            current = current.next

        # Sort the list of possible words in descending order based on the word frequency
        autocomplete_list.sort(key=lambda x: x.frequency, reverse=True)
        time_2 = perf_counter_ns()
        print("Autocomplete:", time_2 - time_1)
        return autocomplete_list[:3]
