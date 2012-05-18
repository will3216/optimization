import os
#If directory (path) doesn't exist, create it!
def createPath(path):
    if not os.path.isdir(path):
        os.mkdir(path)

filename = './Models/test.py'

FILE = open(filename, 'w')

FILE.write('name = "wiggle"')

FILE.close()

createPath('./Models/test/')