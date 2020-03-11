iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

# implementation in for loop
count = 0
word = "hello, world"
for iteration in range(5):
    while True:
        count += len(word)
        break
    print("Iteration " + str(iteration) + ", count is: " + str(count))