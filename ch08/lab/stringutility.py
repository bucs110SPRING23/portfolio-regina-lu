class StringUtility:
    def __init__(self, string):
        def __str__(self):
            return string
        def vowels(self):
            vowels = ["a", "e", "i", "o", "u"]
            count = 0
            for letter in string:
                if letter in vowels:
                    count = count + 1
            if  string < 5:
                return str(string)
            if string >= 5:
                return "many"
        def bothEnds(self):
            if len(string) <= 2:
                return ""
            else:
                return string[0:2] + string[-2]
        def fixStart(self):
            if len(string) <= 1:
                return string
            else:
                character = string[0]
                string = character.replace(character, "*")
                string = character + string[1:]
                return string
        def asciiSum(self):
            return int(sum(ascii))
        def cipher(self):
            length = len(string)
            for char in string:
                if char.isalpha():
                    start = ord('A') if char.isupper() else ord('a')
                    new_pos = (ord(char) - start + (length)) % 26
                    char = chr(start + new_pos)
                result += char
            return result