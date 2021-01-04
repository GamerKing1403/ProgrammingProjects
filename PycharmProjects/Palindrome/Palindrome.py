
if __name__ == '__main__':
    continuingVar = 'Y'
    checking = ['Y', 'YES', 'YE']
    while continuingVar.upper() in checking:
        userString = input("Enter string: ")
        is_palindrome = True
        if userString.upper() != userString[::-1].upper():
            is_palindrome = False
        if is_palindrome:
            print(userString, "is a palindrome word.")
        else:
            print(userString, "is not a palindrome word.")

        continuingVar = input("Do You Want to Continue? ")
