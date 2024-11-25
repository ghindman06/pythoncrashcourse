f = open("example.txt", "w")
f.write("Hello World \n Goodbye World")
f.close()

f = open("example.txt", "r")
content = f.read()
print(content.split("\n"))
f.close()