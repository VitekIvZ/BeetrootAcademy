

class HashTable:
    def __init__(self):
        self.size = 8
        self.map = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size     #   __hash__()
    
    def _probe(self, pos):
        for i in range(pos+1, self.size+pos):
            index = i % self.size
            if self.map[index] is None:
                return index 
    
    def _resize(self):
        copy_map = self.map
        self.size *= 2
        self.map = [None] * self.size
        for item in copy_map:
            if item is not None:
                key, value = item
                self.add(key, value)

    def add(self, key, value):
        # 1. hash
        h_pos = self._hash(key)
        if self.map[h_pos] is None:
            self.map[h_pos] = (key, value)
        else:
            new_pos = self._probe(h_pos)
            if new_pos is not None:
                self.map[new_pos] = (key, value)
            else:
                self._resize()
                self.add(key, value)
        pass

    def get(self, key):
        pos = self._hash(key)
        if self.map[pos] is not None and self.map[pos][0] == key:    #   __eq__()
            return self.map[pos][1]
        else:
            for i in range(pos+1, self.size+pos):
                index = i % self.size
                if self.map[index] is not None and self.map[index][0] == key:
                    return self.map[index][1] 
        return None
    
    def delete(self, key):
        pos = self._hash(key)
        if self.map[pos] is not None and self.map[pos][0] == key:    #   __eq__()
            self.map[pos] = None
            return True
        else:
            for i in range(pos+1, self.size+pos):
                index = i % self.size
                if self.map[index] is not None and self.map[index][0] == key:
                    self.map[index] = None
                    return True
        return False
    
    def __str__(self):

        return '[' + ', '.join(map(str, filter(lambda x: x is not None, self.map))) + ']'


class Element:

    def __init__(self, key):
        self.key = key
    
    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        return self.key == other.key


if __name__ == '__main__':
    hash_map = HashTable()

    hash_map.add('key1', 'value1')
    hash_map.add('key2', 'value2')
    hash_map.add('key3', 'value3')

    print(hash_map)

    print(hash_map.get('key1'))

    hash_map.delete('key3')
    hash_map.delete('key4')

    print(hash_map)