with open('file.txt', 'r') as myFile:
    wordOccurrence = {}
    for lines in myFile.readlines():
        words = lines.split(' ')
        for i in range(len(words)):
            try:
                wordOccurrence[words[i].lower()] += 1
            except KeyError as e:
                wordOccurrence[words[i].lower()] = 1

maximum = 0
mostOccurringWord = None
for key, value in wordOccurrence.items():
    if int(value) > maximum:
        maximum = value
        mostOccurringWord = key

print('The most Occurring word is "'+mostOccurringWord+'" with {} occurrence.'.format(maximum))
