file = open("basic.txt","w")
file.write("hello programming")
file.close()


with open("basic.txt","r") as file:
    contents = file.read()

print("contents=",contents)#contents= hello programming




