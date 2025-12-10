1. Describe the Problem

Users want to keep diary entries.
They should be able to:

Add diary entries

See all diary entries

Count all words in all entries

Get total reading time based on WPM

Find the best entry to read in the time they have

Each diary entry should be able to:

Count its own words

Calculate reading time

Return chunks of readable text based on WPM and minutes, remembering progress


# File: lib/diary.py

class Diary:
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass


from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_add_and_list_entries():
    diary = Diary()
    e1 = DiaryEntry("Day 1", "I went to the park.")
    diary.add(e1)
    assert diary.all() == [e1]

def test_count_words_multiple_entries():
    diary = Diary()
    diary.add(DiaryEntry("A", "one two"))
    diary.add(DiaryEntry("B", "three four five"))
    assert diary.count_words() == 5

def test_reading_time_total():
    diary = Diary()
    diary.add(DiaryEntry("A", "one two three four"))
    assert diary.reading_time(2) == 2

def test_best_entry_for_reading_time():
    diary = Diary()
    e1 = DiaryEntry("A", "one two")          # 2 words
    e2 = DiaryEntry("B", "one two three")    # 3 words
    e3 = DiaryEntry("C", "1 2 3 4 5")        # 5 words
    diary.add(e1)
    diary.add(e2)
    diary.add(e3)
    assert diary.find_best_entry_for_reading_time(2, 2) == e3

def test_reading_chunk():
    entry = DiaryEntry("Title", "one two three four five")
    assert entry.reading_chunk(2, 1) == "one two"
    assert entry.reading_chunk(2, 1) == "three four"
    assert entry.reading_chunk(2, 1) == "five"
    assert entry.reading_chunk(2, 1) == "one two"

