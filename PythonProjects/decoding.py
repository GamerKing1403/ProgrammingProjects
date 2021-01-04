string = input()
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','|','}']
decoded = ''
for i in string.lower():
    if i in alphabets:
        decoded += alphabets[alphabets.index(i) - 3] 
    elif i == '$':
        decoded += '!'
    elif i == '#':
        decoded += ' '
    elif i == '1':
        decoded += '.'
    elif i == '/':
        decoded += ','
    elif i == '2':
        decoded += '/'
    elif i == '=':
        decoded += ':'
    elif i == '\“':
        decoded += '\''
    else:
        decoded += i

print(decoded)
