import os
from dotenv import find_dotenv, load_dotenv
from pathlib import Path
load_dotenv(find_dotenv())
PATH = os.getenv("PATH")

def count_directory_size(directory):

    files = os.listdir(directory)
    count = 0
    for file in files:
        count +=1
    print(count)

#Высокоуровневый подход
def count_folder_size(directory):
    path = Path(directory)
    folder_size = 0
    for x in path.iterdir():
        folder_size+=1
    return folder_size


if __name__ == '__main__':
    print(count_folder_size('C:/Users'))
    # filepath = input("Enter a file path to access:")
    # if os.path.exists(filepath):
    #     count_directory_size(filepath)
    # else:
    #     # count_directory_size(PATH)
    #
