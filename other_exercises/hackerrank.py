#List Comprehensions (easy)
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print ([[a,b,c] for a in range(0,x+1) 
for b in range(0,y+1) 
for c in range(0,z+1) 
if a + b + c != n ])

#Find the Runner-Up Score!
n = int(input())
arr = map(int, input().split())
my_list = [0 for i in range(n)]
my_list = list(arr)
unique_numbers = list(set(my_list))
firstPlayer = max(unique_numbers[0], unique_numbers[1])
secondPlayer = min(unique_numbers[0], unique_numbers[1])

for i in range(2, len(unique_numbers)):
    if unique_numbers[i] > firstPlayer:
        secondPlayer = firstPlayer
        firstPlayer = unique_numbers[i]
    elif unique_numbers[i] > secondPlayer and unique_numbers[i] != firstPlayer:
        secondPlayer = unique_numbers[i]
print(secondPlayer)


# Nested Lists
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
if __name__ == '__main__':
p_s = []
    for _ in range(int(input())):
        p_s = []
        name = input()
        score = float(input())
        p_s.append(name, score)