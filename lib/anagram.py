# your code goes here!

from random import shuffle

class Anagram:

    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, my_list):
       anagrams = []
       for word in my_list:
          # word != self.word  checks that the word in the list is not the entered word
          # sorted(word)== sorted(self.word) checks that the jumbled word contains the same
          # letters as the entered word
          if word.lower() != self.word and sorted(word.lower())== sorted(self.word):
             anagrams.append(word)
       return anagrams
    

listen = Anagram("Listen")
result = listen.match(['enlists', 'google', 'inlets',"ilnste",'banana'])
print(result)