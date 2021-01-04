if __name__ == '__main__':
    continuingVar = 'Y'
    checking = ['Y', 'YES', 'YE']
    while continuingVar.upper() in checking:
        # This is the Input Section
        n = int(input("Enter the number which you Want the n-bonacchi series to be:- "))
        length = int(input("Enter the Length of the series that you want:- "))
        # This is the main Working
        series = [0, 1]
        for i in range(length-2):
            series.append((n*series[i+1]) + series[i])

        print(series)
        continuingVar = input("Do You Want to Continue? ")
