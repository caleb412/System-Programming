import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
path = os.getenv("VAR")

def count_directory_size(directory):

    files = os.listdir(directory)
    count = 0
    for file in files:
        count +=1
    print(count)

if __name__ == '__main__':
    count_directory_size(path)
