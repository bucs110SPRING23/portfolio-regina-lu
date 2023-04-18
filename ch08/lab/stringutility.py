class StringUtility:
    def __init__(self, string):
        self.x = string
    def __str__(self):
        string = self.x
        return string
    def vowels(self):
        string = self.x
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        for letter in string:
            if letter in vowels:
                count = count + 1
        if count < 5:
            return str(count)
        if count >= 5:
            return "many"
    def bothEnds(self):
        string = self.x
        if len(string) <= 2:
            return ""
        else:
            return string[0:2] + string[-2:]
    def fixStart(self):
        string = self.x
        if len(string) <= 1:
            return string
        else:
            character = string[0]
            for letters in string [1:]:
                if letters == character:
                    newstring = string.replace(character, "*")
                    string = string[0] + newstring[1:]
            return string
    def asciiSum(self):
        string = self.x
        value = 0
        for character in string:
            addvalue = int(ord(character))
            value = value + addvalue
        return value
    def cipher(self):
        string = self.x
        result = ""
        length = len(string)
        for char in string:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                new_pos = (ord(char) - start + (length)) % 26
                char = chr(start + new_pos)
            result += char
        return result