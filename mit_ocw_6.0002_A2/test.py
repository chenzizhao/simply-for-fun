# # test 1

# mylist = [1,0,0]
# mylist2 = [2,0,0]

# def myfunction (list):
#     list += [1]
#     print(f'inside function {list}')
#     print(id(list))

# def myfunction2(list):
#     list = list.append(2)
#     print(f'inside function {list}')
#     print(id(list))


# print(mylist)
# print(id(mylist))
# myfunction(mylist)
# print(mylist)

# print(mylist2)
# print(id(mylist2))
# myfunction2(mylist2)
# print(mylist2)


#  # test 2: list.append and list += 
# mylist = [0, 1]
# result = mylist

# def func1(l):
#     # l = l + [1]
#     l.append(1)
#     print(l)
#     print(id(l))
#     return func2(l)

# def func2(l):
#     l.append(2)
#     # l = l + [2]
#     print(l)
#     print(id(l))
#     return l

# print(mylist)
# print(id(mylist))
# print(result)
# print(id(result))

# result = func1(mylist)

# print(mylist)
# print(id(mylist))
# print(result)
# print(id(result))

# test 3 increment

var = 1
var2 = var

def increment(variable):
    variable += 1

print(var)
print(var2)
increment(var)
print(var)
print(var2)