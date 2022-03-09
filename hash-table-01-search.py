class HashTable:
    def __init__(self):
        self.MAX = 30
        self.days = [None for i in range(30)]

    def get_hash(self, value):
        s = 0
        for char in value:
            s += ord(char)
        return s % self.MAX

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.days[index] = value

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.days[index]


dict = HashTable()

dict["Jan 1"] = 27
dict["Jan 2"] = 31
dict["Jan 3"] = 23
dict["Jan 4"] = 34
dict["Jan 5"] = 37
dict["Jan 6"] = 38
dict["Jan 7"] = 29
dict["Jan 8"] = 30
dict["Jan 9"] = 35
dict["Jan 10"] = 30

print(dict.days[0:7])

print(dict["Jan 7"])  # 29
print(dict["Jan 2"])  # 31

