class HashTable:
    def __init__(self):
        self.MAX = 100
        self.storage = [(None, 0) for i in range(self.MAX)]

    def get_hash(self, value):
        s = 0
        for char in value:
            s += ord(char)
        return s % self.MAX

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        _value = self.__getitem__(key)
        self.storage[index] = (key, value+_value)

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.storage[index][1]


dict = HashTable()

text = """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;"""

for word in text.split():
    for special_char in ["!", ",", ".", ";"]:
        word = word.replace(special_char, "")
    dict[word.lower()] = 1

for output in dict.storage:
    if output[0]:
        print(output)
        
# output        
"""
('i', 3)
('and', 3)
('undergrowth', 1)
('as', 2)
('far', 1)
('in', 2)
('the', 2)
('one', 2)
('bent', 1)
('to', 1)
('both', 1)
('long', 1)
('could', 2)
('not', 2)
('looked', 1)
('where', 1)
('down', 1)
('wood', 1)
('diverged', 1)
('two', 1)
('stood', 1)
('travel', 1)
('yellow', 1)
('traveler', 1)
('sorry', 1)
('a', 1)
('be', 1)
"""
