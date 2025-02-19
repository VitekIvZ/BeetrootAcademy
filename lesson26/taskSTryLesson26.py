#Реалізувати in (__contains__) та len (__len__) методи для HashTable

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def __contains__(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return True
        return False

    def __len__(self):
        count = 0
        for bucket in self.map:
            if bucket is not None:
                count += len(bucket)
        return count

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

    print('key1' in hash_map)
    print('key3' in hash_map)
    print(len(hash_map))
