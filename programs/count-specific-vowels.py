data = str(input("Please type a sentence: "))
vowels = "aeiou"
for v in vowels:
    print(v, data.lower().count(v))