#Norma
#patterns2.py


def triangle(N):
    print("This is your triangle: ", '\n')
    for count in range(N):
        for i in range(count+1):
            print(end=' ')
        for x in range(N - count):
            print('*', end='')
        print()


def hollow_box(N):
    print("This is your box: ", '\n')

    for count in range(N):
        if count ==0 or count == N-1:
            for x in range(N):
                print('*', end='')
            print()
        elif count>0 and count <N-1:
            st = ''
            t = '*'
            for c in range(N-2):
                st = ' ' + st
            myString = t + st + t
            print(myString)



        print()

def main():
    N = int(input("Enter N >=0: "))
    triangle(N)
    hollow_box(N)





main()