import random
f= open("Hangman_wordbank.txt", "a")
def enter_words():
  word=input("Enter a word to the bank: ")
  if (word!="/e"):

     f.write(word)
     f.write("\n")
  f.close()



#enter_words()
def get_word():
  f= open("Hangman_wordbank.txt", "r")
  lines=0
  count =0
  for line in f: lines+=1 # calculating how many lines/words are in the file
  f.close()
  f= open("Hangman_wordbank.txt", "r") #repeating opening and closing required to reset pointer i guess
  line=0
  rnum= random.randint(0,lines) #chooses a random line in the bank
  rword=0 #holds the word for string ops.
  for line in f:

    if(count==rnum):
      rword=line

      return rword

    count += 1
  f.close()