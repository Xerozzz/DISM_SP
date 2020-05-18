start = int(input("Pls enter a starting number: "))
end = int(input("Pls enter an ending number: "))
output = ""

for i in range(23,34):
    if i % 2 == 0:
        output += str(i) + "\t"

print(output)
        
