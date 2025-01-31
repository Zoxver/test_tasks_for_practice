class HashMap:
    EMPTY = None
    DELETED = object()

    def __init__(self):
        self.size = 8
        self.table = [self.EMPTY] * self.size
        self.count = 0

    def _hash1(self, key):
        return hash(key) % self.size

    def _hash2(self, key):
        return 1 + (hash(key) % (self.size - 1))

    def find_slot(self, key):
        """
        Находит подходящий слот для вставки или обновления значения.
        Возвращает индекс и флаг доступности.
        """
        h1 = self._hash1(key)
        h2 = self._hash2(key)
        index = h1

        for _ in range(self.size):
            item = self.table[index]

            if item == self.EMPTY:
                return index, True

            elif item != self.DELETED:
                current_key, _ = item
                if current_key == key:
                    return index, False

            if item == self.DELETED:
                return index, True

            index = (index + h2) % self.size

        return None, False

    def _rehash(self):
        old_buckets = self.table
        self.size *= 2
        self.table = [self.EMPTY] * self.size
        self.count = 0

        for item in old_buckets:
            if item not in (self.EMPTY, self.DELETED):
                key, value = item
                self[key] = value

    def __setitem__(self, key, value):
        index, is_empty = self.find_slot(key)

        if is_empty:
            self.table[index] = (key, value)
            self.count += 1
        else:
            self.table[index] = (key, value)

        load_factor = self.count / self.size
        if load_factor > 0.7:
            self._rehash()

    def __getitem__(self, key):
        index, _ = self.find_slot(key)
        if index is not None and self.table[index] not in (self.EMPTY, self.DELETED):
            return self.table[index][1]
        raise KeyError(key)

    def __delitem__(self, key):
        index, _ = self.find_slot(key)
        if index is None or self.table[index] in (self.EMPTY, self.DELETED):
            raise KeyError(key)

        self.table[index] = self.DELETED
        self.count -= 1

    def __contains__(self, key):
        index, _ = self.find_slot(key)
        return index is not None and self.table[index] not in (self.EMPTY, self.DELETED)

    def __len__(self):
        return self.count

    def add(self, key, value):
        self.__setitem__(key, value)

    def keys(self):
        return [item[0] for item in self.table if item not in (self.EMPTY, self.DELETED)]

    def values(self):
        return [item[1] for item in self.table if item not in (self.EMPTY, self.DELETED)]

    def items(self):
        return [(item[0], item[1]) for item in self.table if item not in (self.EMPTY, self.DELETED)]
