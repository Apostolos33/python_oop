class vowels:
    VOWELS = ["a", "e", "i", "o", "u", "y"]

    def __init__(self, text: str):
        self.text = text
        self.current_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx += 1
        if self.current_idx >= len(self.text):
            raise StopIteration
        if self.text[self.current_idx].lower() in self.VOWELS:
            return self.text[self.current_idx]
        else:
           return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

