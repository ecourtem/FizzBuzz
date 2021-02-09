# Put in order of how the words should be printed
stops = [3, 5]
words = {3: "Fizz",
         5: "Buzz", }

# Iterate 1 to 100 and print game answers
for i in range(1, 101):
    output = ""
    for j in stops:
        if i % j == 0:
            output += words[j]
    print(i, output)
