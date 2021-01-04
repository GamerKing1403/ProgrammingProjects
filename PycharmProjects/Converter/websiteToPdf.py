import convertapi
convertapi.api_secret = 'r1Z76YULbnro78mZ'

x = 20
website = "https://automatetheboringstuff.com/2e/chapter" + str(x) + "/"
result = convertapi.convert('pdf',{'Url':website})

result.save_files(r'C:\Users\user\Desktop\AutomatePython\Chapter'+str(x)+'.pdf')
