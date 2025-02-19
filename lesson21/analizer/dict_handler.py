class DictHandler:
    def __init__(self, file=''):
        self.file = file
        self.data_set = set()

    def __enter__(self):
        self.file = open(self.file, 'r')
        self._load_to_set()
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

    def _load_to_set(self):
        for line in self.file:
            self.data_set.add(line.strip())
            
    def __contains__(self, element):
        return element in self.data_set       

if __name__ == '__main__':
    file = "./lesson21/analizer/english3.txt"
    
    # Використання власного контекстного менеджера для завантаження файлу в set
    with DictHandler(file) as handler:
        print(handler.data_set)