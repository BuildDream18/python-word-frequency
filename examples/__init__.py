# -*- coding: utf-8 -*-
from examples.word_frequency import WordFrequency


if __name__ == '__main__':

    file_path = '../test/words.txt'
    frequency = WordFrequency().fast_serial_word_frequency(file_path)

    for word in frequency:
        print ' : '.join([word, frequency[word]])