import os
path = '/home/karthik/Downloads/hand guns _ Google Search'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, str(index)+'.jpg'))