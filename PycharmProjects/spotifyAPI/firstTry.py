import pandas as pd

inputFile = pd.read_json('spotify.txt', encoding='UTF-8')
for i in range(393):
    print(inputFile['items'][i]['track']['name'])
