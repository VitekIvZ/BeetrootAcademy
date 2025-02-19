import string

class TextHandler:
    def __init__(self, file=''):
        self.file = file
        self.word_gen = None

    def __enter__(self):
        self.file = open(self.file, 'r')
        self.word_gen = self._gen_word()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"Closing file: {self.file}")
        if exc_type:
            print(f"An exception occurred: {exc_type}, {exc_value}")
            print(f"Traceback: {traceback}")
            return True
        return False 


    def __iter__(self):
        return self

    @staticmethod
    def _cleaned_word(word):
        return ''.join([x for x in word if x not in string.punctuation]).lower()

    def _gen_word(self):
        for line in self.file:
            for word in line.split():
                yield self._cleaned_word(word)

    def __next__(self):
        return next(self.word_gen)
    
    

if __name__ == '__main__':
    file = "./lesson21/analizer/shakespeare.txt"
    
    # Використання власного контекстного менеджера для читання файлу
    with TextHandler(file) as handler:
        for word in handler:
            print(word)
    
    
