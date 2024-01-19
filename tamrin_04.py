count = 0
n = "tamrin_04f.txt"
file = open(n,"r")
x = file.readlines()
for i in x:
    count += 1
file.close()
print(f"line : {count}")