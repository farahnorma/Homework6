#Norma
#wordbox.py


def wordswitch(word):
    for i in range(len(word)):
        myString = word[i:len(word)+1] + word[0:i]
        print(myString, end=" ")
        print('\n')


def main():
    word = str(input("Word: ")).lower()
    wordswitch(word)


main()