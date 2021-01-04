import os
import sys
import subprocess

if __name__ == "__main__":

    rawLib = open('pythonLibraries.txt', 'r')
    libraries = open('libraries.txt', 'a+')

    for lib in rawLib:
        if lib.find('-') == -1 and lib.find('Package') == -1:
            lib = lib.split(' ',2)
            libName = lib[0]
            libraries.write(libName.strip() + '\n')
    rawLib.close()
    libraries.close()
    os.remove('pythonLibraries.txt')

    libraries = open('libraries.txt', 'r')
    batFile = open('Installer.txt', 'a+')
    temp_str = ''

    for lib in libraries:
        temp_str += lib.strip() + " "
    print(temp_str)
    batFile.write('c:\python3.7\python.exe -m pip install --upgrade pip\npip install '+temp_str+' --upgrade')

    batFile.close()
    os.rename('Installer.txt','Installer.bat')
    libraries.close()
    os.remove('libraries.txt')
    try:
        subprocess.run('Installer.bat')
        os.remove('Installer.bat')
    except:
        print("Keyboard Interupt")
        os.remove('Installer.bat')
        sys.exit(0)
