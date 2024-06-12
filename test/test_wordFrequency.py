# -*- coding: utf-8 -*-
from unittest import TestCase
from examples.word_frequency import WordFrequency
from timeit import timeit


class TestWordFrequency(TestCase):

    def test_serial_word_frequency(self):
        file_path = 'words.txt'
        response = WordFrequency().serial_word_frequency(file_path)

        self.assertIn('war', response)
        self.assertEqual(166, response['war'])

        self.assertIn('peace', response)
        self.assertEqual(59, response['peace'])

        # Function execution timing
        print (
            'Elapsed time for serial_word_frequency %s',
            timeit(
                'WordFrequency().serial_word_frequency("words.txt")',
                setup='from examples.word_frequency import WordFrequency',
                number=10
            ) / 10.0
        )

    def test_fast_serial_word_frequency(self):
        file_path = 'words.txt'
        response = WordFrequency().fast_serial_word_frequency(file_path)

        self.assertIn('war', response)
        self.assertEqual(166, response['war'])

        self.assertIn('peace', response)
        self.assertEqual(59, response['peace'])

        # Function execution timing
        print (
            'Elapsed time for fast_serial_word_frequency %s',
            timeit(
                'WordFrequency().fast_serial_word_frequency("words.txt")',
                setup='from examples.word_frequency import WordFrequency',
                number=10
            ) / 10.0
        )

    def test_parallel_word_frequency(self):
        file_path = 'words_part{0}.txt'
        threads = 4
        response = WordFrequency().parallel_word_frequency(file_path, threads)

        self.assertIn('war', response)
        self.assertEqual(166, response['war'])

        self.assertIn('peace', response)
        self.assertEqual(59, response['peace'])

        # Function execution timing
        print (
            'Elapsed time for parallel_word_frequency %s',
            timeit(
                'WordFrequency().parallel_word_frequency("words_part{0}.txt", 4)',
                setup='from examples.word_frequency import WordFrequency',
                number=10
            ) / 10.0
        )
