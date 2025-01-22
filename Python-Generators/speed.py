import cProfile

print('List Comprehension')
print(cProfile.run("min([num**4 for num in range(1, 200000)])"))
print('Python Generators')
print(cProfile.run("min((num**4 for num in range(1, 200000)))"))
