

class TextHandler:

    def __init__(self, file_name=''):

        self.file_name = file_name

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __iter__(self):
        return self
    
    @staticmethod
    def _cleaned_word(word):
        # clean word from punctuation
        # .lower()
        return None
    
    def _gen_word(self):

        for line in self.file:
            
            for word in line.split():
                yield self._cleaned_word(word)

    def __next__(self):
        return next(self._gen_word())
    

if __name__ == '__main__':
    # handler = TextHendler()
    # dictionary = Dictionary()
    # missed_word = WordContainer()

    with TextHandler("") as handler:  #, Dictionary("") as dictionary:
        for word in handler[:2]:
            print(word)

            # if word not in dictionary:
            #     missed_word.add(word)
