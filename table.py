#Norma
#table.py

#Print out a neatly formatted multiplication table


def main():
    print('|   *|  00|  01|  02|  03|  04|  05|  06|  07|  08|  09|  10|  11|  12|')
    print('-----------------------------------------------------------------------')
    for row in range(13):
        if row<10:
            print('| 0',row, end='')
        else:
            print('| ',row, end='')

        for col in range(13):
            v = row*col
            if v<10:
                print('| 0', row*col, end='')
            elif v<100:
                print('| ',row*col, end='')
            else:
                print('|',row*col, end='')
        print('| \n')



main()