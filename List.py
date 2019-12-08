List = []
print("Blank List")
print(List)


List.append(1)
List.append(2)
List.append(10)
print("\nList after adding three elements: ")
print(List)


for i in range(11, 19):
    List.append(i)
print("\nList after adding elements through iterator: ")
print(List)


List.append((21, 22))
print("\nList after adding elements as tuples: ")
print(List)

List1 = ['ab', 'bc']
List.append(List1)
print("\nList after adding elements as Lists: ")
print(List)
