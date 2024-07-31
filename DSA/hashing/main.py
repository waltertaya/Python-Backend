from search import search_name
from insert import insert_element
from delete import delete_element

if __name__ == '__main__':
    print('''
        Enter the choice:
          1. searching
          2. inserting
          3. deleting
    ''')
    choice = input('Choice: ')
    if choice == '1':
        print(search_name())
    elif choice == '2':
        print(insert_element())
    elif choice == '3':
        print(delete_element())
    else:
        print('Wrong choice')
