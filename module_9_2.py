first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(x1) for x, x1 in zip(first, second) if len(x) != len(x1))
# print(first_result)
# for i in first_result:
#     print(i)


second_result = (len(first[i]) == len(second[i]) for i in range (min(len(first),len(second))))
# print(second_result)
# for i in second_result:
#     print(i)

print(list(first_result))
print(list(second_result))