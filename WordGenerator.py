class WordGenerator():

    def __init__(self, file_location):
        self.file_location = file_location

    def open_words_txt(self, location):
        try:
            temp_text = open(location)
        except OSError as ex:
            print(
                f"C err no#: {ex.errno}\nError message: {ex.strerror}\nPath passed in: {ex.filename}")
        else:
            return temp_text.read().splitlines()
        finally:
            temp_text.close()
