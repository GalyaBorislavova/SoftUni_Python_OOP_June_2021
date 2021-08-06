string_ = "Hello"
list_ = [i for i in range(1, 11)]
tuple_ = tuple(list_)
set_ = set([i for i in range(1, 11)])
dict_ = {chr(i): i for i in range(97, 123)}

print(string_, list_, tuple_, set_, dict_, sep="\n")

my_list = [1, 2, 3, 'example', 3.132, 10, 30]
my_list.insert(3, 4)
print(my_list)
