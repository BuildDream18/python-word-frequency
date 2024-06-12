# -*- coding: utf-8 -*-
from collections import defaultdict
from itertools import chain
import multiprocessing


class WordFrequency(object):

    def serial_word_frequency(self, file_path):
        """
        Reads a file, line by line and produces a frequency distribution
        ** Standard implementation - Reads a file one line at a time for
        ** reduced memory overhead. Uses exceptions to determine if a word
        ** needs adding or a word count needs incrementing
        :param file_path: Path to file of words
        :return: Frequency distribution dict
        """
        frequency = {}

        # Get a file object and read in line by line
        with open(file_path) as file_object:
            for word in file_object:
                word = word.strip()

                if word:
                    try:
                        frequency[word] += 1
                    except KeyError:
                        # If there is no key, first encounter of this word
                        frequency[word] = 1

        return frequency

    def fast_serial_word_frequency(self, file_path, frequency=None):
        """
        Reads a file, line by line and produces a frequency distribution
        ** More efficient version of standard implementation. Uses built in
        ** Collections class that creates an initialized dictionary. This has
        ** the benefit of not using exceptions, which are slower.
        :param file_path: Path to file of words
        :return: Frequency distribution dict
        """
        # Can be called recursively if required
        if not frequency:
            # Creates a 0 initialized dict so exception check no longer required
            frequency = defaultdict(int)

        # Get a file object and read in line by line
        with open(file_path) as file_object:
            for word in file_object:
                word = word.strip()

                if word:
                    frequency[word] += 1

        return frequency

    def parallel_word_frequency(self, file_path, num_threads):
        """
        A parallel mapreduce type approach
        ** The problem lends itself to a mapreduce approach except for requiring
        ** one pass through a complete file. For example this method uses pre
        ** split files, like hadoop / hdfs would split them
        :param file_path:
        """
        frequency = defaultdict(int)
        thread_pool = multiprocessing.Pool(num_threads)

        file_parts = [
            file_path.format(file_part) for file_part in range(num_threads)
        ]

        # Map chunks of words for processing
        wordset = thread_pool.map(chunker, file_parts)

        # Flatten the list of lists to a list of words using fast itertools
        words = list(chain.from_iterable(wordset))

        # Reduce results set to final required output
        frequency = reducer(words, frequency)

        return frequency


def chunker(file_path):
    """
    Read a block of lines from a file
    :param file_path:
    :return:
    """
    words = []

    with open(file_path, 'r') as file_object:
        for word in file_object:
            word = word.strip()

            if word:
                words.append(word)

    return words


def reducer(words, frequency):
    """
    reduces words to final output frequency list
    :param words:
    :param frequency:
    :return: dict of unique words and their frequencies
    """
    for word in words:
        frequency[word] += 1

    return frequency