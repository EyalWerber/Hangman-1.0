def find_all(word,char):
    start = 0
    while True:
        start = word.find(char, start)
        if start == -1: return #If find() finds nothing it returns  = -1
        yield start #if nothing was found, find all returns iterable/generator(list) 0.
        start += len(char) #each time loop runs, start point goes up by 1


def replace_str_index(text,index=0,replacement=''):   #Substring replacing func
    return '%s%s%s'%(text[:index],replacement,text[index+1:]) #this is a slice argument. each '%s' refers a slice given at the %()


import HangmanWords
import string
word=HangmanWords.get_word().upper()
print(word)
hide=word #Holds a randomly chosen from database Hangman_wordbank.txt
for char in word:
    if char!="\n":
        hide=hide.replace(char,"_")
print(hide)

strike_count= 5

while(word!=hide and strike_count>0):
    flag = False
    try:
        Gchar = input("Enter a character: ").upper()  # Guess char
        if not Gchar:
            raise ValueError("No input recieved")
        elif len(Gchar)>1:
            raise ValueError("Only one letter!")
        else:
            c_index = (list(find_all(word, Gchar)))
    except ValueError as e:
        print(e)

    for char in word:
      if char == Gchar:
        for i in range(len(c_index)):
           ind = c_index[i]

           hide = replace_str_index(hide,ind,Gchar)
           flag = flag = True

    if flag==False:
        strike_count-=1


    print(hide)
    print(str(strike_count)+" strikes left!!!")

if strike_count>0:
    print("You win!")
    print("oh and you got "+str(strike_count)+" points")
else:
    print("you Lose")


