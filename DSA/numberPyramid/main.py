#!/usr/bin/env python3

def print_pyramid(rows):
    count = 1
    while(count <= rows):
        row = []
        for i in range(1, count + 1):
            row.append(i)
        print(*row, sep=' ')
        count = count + 1


if __name__ == '__main__':
    rows = int(input('Enter the number of rows: '))
    print_pyramid(rows)
