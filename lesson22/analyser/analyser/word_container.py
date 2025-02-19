


class WordContainer:

    def __init__(self, file_name=''):
        self.file_name = file_name
        self.container = dict()
        # self.container = set()
        # self._create_dict()

    def add(self, word):
        # if container is set 
        # if self.file and word not in self.container: 
        #     self.file.write(word + '\n')
        #     self.container.add(word)
        #
        self.container[word] = self.container.get(word, 0) + 1

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        print(self.file)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            for key, value in self.container.items():
                self.file.write(f"{key:20} : {value} \n")
            self.file.close()

        if exc_value:
            print(f"{exc_type}: {exc_value}")
            return True
