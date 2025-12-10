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

