"""
8. Write a Python script to print distinct elements along with their frequencies of
occurrence in the list.
"""

List=['E','E','F','G','F','G','G','E','F']
Frequency = {}

for i in List:
    if i in Frequency:
        Frequency[i] +=1
    else:
        Frequency[i] = 1

print(Frequency)