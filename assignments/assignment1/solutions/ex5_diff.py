import nltk
from nltk.corpus import wordnet
nltk.download("wordnet")
legitwords = [word for word in wordnet.words() if len(word)>1]
legitwords.append("i")
legitwords.append("a")
alphabet = "abcdefghijklmnopqrstuvwxyz"

cipher = list(input("Enter cipher: "))
solutions = []
for shift_size in range(26):
    shifted = ""
    for letter in cipher:
        shifted += alphabet[(alphabet.index(letter)+shift_size)%26]
    solutions.append(shifted)
print(solutions)

wordcounts = [0]*26
for solution in solutions:
    for word in legitwords:
        if word in solution:
            wordcounts[solutions.index(solution)] += 1

print(solutions[wordcounts.index(max(wordcounts))])