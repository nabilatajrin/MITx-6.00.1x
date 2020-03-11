vowels = "aioue"
text = input("Please enter your text: ")
count = 0

for i in text:
    if i in vowels:
        count += 1

print("There are", count, "vowels in your text")