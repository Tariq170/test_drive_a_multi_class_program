class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)
        
        
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        

    def all(self):
        return self.entries
        # Returns:
        #   A list of instances of DiaryEntry
        

    def count_words(self):

        return sum(entry.count_words() for entry in self.entries)
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if wpm <= 0:
            raise ValueError("wpm should be positive")
        return -(-self.count_words() // wpm)

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
        max_words = wpm * minutes
        best_entry = None
        best_word_count = 0 

        for entry in self.entries:
            words = entry.count_words()
            if words <= max_words and words > best_word_count:
                best_entry = entry
                best_word_count = words

        return best_entry        