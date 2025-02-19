


class DictHandler:

    def __init__(self, file_name=''):
        self.file_name = file_name
        self.dictionary = set()
        self._create_dict()

    def _create_dict(self):
        self.file = None
        try:
            self.file = open(self.file_name, 'r')
            self.dictionary = {word.strip() for word in self.file}
            print(f"dictionary word count: {len(self.dictionary)}")
        except Exception as err:
            print(f"{err.__class__.__name__}: {err}")
        finally:
            if self.file:
                self.file.close()
    
    def __contains__(self, element):
        return element in self.dictionary
    
