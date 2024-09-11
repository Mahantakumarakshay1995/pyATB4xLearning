my_list = [1,2,3,]

my_list.append(4)  #append object to the end of the list

print(len(my_list))
for i in my_list: # for  each loop
    print(i)

print(my_list)
my_list.extend([7,8,9])
#my_list.insert(1,"AKM")
my_copy_list=my_list.copy()

my_list.sort(reverse=True)

print(my_list)