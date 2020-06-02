str = input("Введите слова через пробел - ")
my_list = str.split(' ')
#print(my_list)
#Первый вариант
#for i in range(0, len(my_list), 1):
#    print(i+1, my_list[i][:10:])
 
#Второй вариант   
for ind, el in enumerate(my_list, 1):
    print(ind, el[:10:])