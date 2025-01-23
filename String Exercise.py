"""
3
"""
string = "      Summer is just 3 weeks away!     "
# A
print(string.strip())
# B
print(string[6:])
# C
print(string[:34])
# D
print(string.replace("e", "*"))
# E
print("*" + string.strip().center(30) + "*")
# F
print("*" + string.strip().ljust(30) + "*")
#G
print("*" + string.strip().rjust(30) + "*")
"""
4
"""
print(ord("B"))
print(ord("d"))
print(ord("#"))
print(ord("&"))
print(ord("Z"))
print(ord("z"))
"""
5
"""
def pig_latin(a):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0].lower() in vowels:
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

word = input("Enter a word to be translated into pig latin: ")
print(pig_latin(word))
"""
6
"""
"""
def pig_latin_function(text):
    words = text.split()
    translated_words = [pig_latin_function(text) for i in words]
    translated_text = ' '.join(translated_words)
    return translated_text

translated_text = pig_latin_function("I hate pig latin so much")
print(translated_text)
"""
