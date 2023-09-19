# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word
    
    def match(self,input_list):
        anagram=[]
        for word in input_list:
            if sorted(word) == sorted(self.word):
                anagram.append(word)
        return anagram
        
print(Anagram("enlist").match(["listen", "poison", "hello"]))