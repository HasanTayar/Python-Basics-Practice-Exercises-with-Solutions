numbers = []
letters = []
n = int(input("Enter index of Lists: "))
for i in range(0,n):
    element = int(input("Enter Element for Numbers:"))
    numbers.append(element)
print(numbers)
for i in range(0,n):
    ele = (input("Enter a Letters: "))
    letters.append(ele)
print(letters)
for i in numbers:
    print(letters[i],end="")

