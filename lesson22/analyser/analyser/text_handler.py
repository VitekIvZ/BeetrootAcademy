import string

translator = str.maketrans('', '', string.punctuation)
# word.translate(translator)

class TextHandler:

    def __init__(self, file_name=''):

        self.file_name = file_name
        self.file = None

    def __enter__(self):
        try:
           self.file = file = open(self.file_name, 'r')
        except FileNotFoundError as err:
            print(f'File not founded. {err}')
        # except AttributeError as err:
        #     print(f'Problem with file. {err}')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

        if exc_value:
            print(f"{exc_type}: {exc_value}")
            return True

    def __iter__(self):
        # self.idx = 0
        return self
    
    @staticmethod
    def _cleaned_word(word):
        # clean word from punctuation
        if word.startswith("'") or word.endswith("'"):
            word = word.strip("'")
        if word.endswith("'s"):
            word = word.rstrip("'s")
        elif word.endswith("'st"):
            word = word.rstrip("'st")
        return word.translate(str.maketrans('', '', string.punctuation)).lower()

    def _gen_word(self, line):
        for word in line.split():
            yield self._cleaned_word(word)

    def _gen_line(self):
        # counter = 0
        if self.file:
            for line in self.file:
                # counter += 1
                # idx += 1
                yield from self._gen_word(line)
                # for word in line.split():
                #     yield self._cleaned_word(word)
            # if counter > 2:
            #     break
            # for word in line.split():
            #     yield self._cleaned_word(word)

    def __next__(self):
        return next(self._gen_line())
    

if __name__ == '__main__':
    # handler = TextHendler()
    # dictionary = Dictionary()
    # missed_word = WordContainer()
    from time import time
    start = time()
    with TextHandler(".\\shakespeare.txt") as handler:  #, :
        for word in handler:
            pass
            # print(word)
            # if word not in dictionary:
            #     missed_word.add(word)
    print(f"word read time: {time() - start}")
