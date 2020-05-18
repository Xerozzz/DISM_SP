f = open("Practical\Practical 5\students.txt")
for line in f:
    print(line)
f.close()

with open("Practical\Practical 5\students.txt","w") as f:
    f.write("Hello World")

with open("Practical\Practical 5\students.txt","w") as f:
    for line in f:
        print(line)