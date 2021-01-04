upperCaseChar = 0
lowerCaseChar = 0
noOfVowels = 0
noOfConsonants = 0
vowel = ['a', 'e', 'i', 'o', 'u']

with open('file.txt', 'r') as myFile:
    for lines in myFile.readlines():
        for letter in lines:
            if letter.isalpha():
                if letter.lower() in vowel:
                    noOfVowels += 1
                else:
                    noOfConsonants += 1
                if letter.isupper():
                    upperCaseChar += 1
                elif letter.islower():
                    lowerCaseChar += 1

print('Here is the Results:- \nNo of Vowels = ', noOfVowels, '\nNo of Consonants = ', noOfConsonants,
      '\nNo of Upper Case Letter = ', upperCaseChar, '\nNo. of lower case letter = ', lowerCaseChar)
