input1 = input()
#input1 = '10 1 11 8 13 53 20 63 99 79 94'
temp = input1.split(' ')
list_of_numbers = []
for i,value in enumerate(temp):
    if i != 0:
        value = int(value)
        list_of_numbers.append(value)
#print(len(list_of_numbers))



list_length = len(list_of_numbers)
#list_of_numbers+1 = list_of_numbers.index(

answers = []
#print(list_of_numbers)
GVF = 0
list1 = []

for x in list_of_numbers:
    if GVF <= x:
        GVF = x
        list1.append(x)

#print(list1)




note = len(list_of_numbers)
list2 = []
#LVF = list_of_numbers[-1]
LVF = 100

for x in range(len(list_of_numbers)-1,-1,-1):
    #print(x)
    x = list_of_numbers[x]
    #print(x)
    #print(LVF) 
    if LVF > x:
        LVF = x
        list2.append(x)

    #print('\n')
#print(list2)



answers = [value for value in list1 if value in list2]


print(f'{len(answers)} ',end='')

for a in answers:
    print(f'{a} ', end='')
#print(len(answer),answer)
    
    


# 1 11 8 13 53 20 63 99 79 94
