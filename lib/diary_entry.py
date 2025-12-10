class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.words = self.contents.split()
        self.read_index = 0 

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if wpm <= 0:
            raise ValueError("wpm should be positive")
        return -(-self.count_words() // wpm)

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
        if wpm <= 0 or minutes <=0:
            raise ValueError("wpm and minutes must be positive")
        
        reading_chunk = wpm * minutes

        start = self.read_index
        end = start + reading_chunk

        chunk_words = self.words[start:end]
        self.read_index = end 

        if self.read_index > len(self.words):
            self.read_index = 0
        return "".join(chunk_words)    