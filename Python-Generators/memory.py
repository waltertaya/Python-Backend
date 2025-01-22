import sys


list_compr = [num**3 for num in range(1, 5000)]
gen_obj = (num**3 for num in range(1, 5000))

print(f'List comprehension memory: {sys.getsizeof(list_compr)}')
print(f'Python generators memory: {sys.getsizeof(gen_obj)}')
