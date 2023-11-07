mylist = [1, 5, 4, 9]
mylist2 = ["d", "ddd"]
mylist3 = ['k', 'g', 6]
mystring = "hellow from me"
mylist.extend(mylist3)
mylist.extend(mylist3)
print(mylist)

z = ("A", "B", "C")
a, b, c = z
print(b)  # B
x = ("D", "E", 4, "G")
a, _, b, c = x
print(c)  # 4
