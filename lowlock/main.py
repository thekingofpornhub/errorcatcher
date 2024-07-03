from error_processing import chaterror
from file_utils import get_txt_files
import config
import time

def read_in_directory(directorypath):
    txt_files = get_txt_files(directorypath)
    print(txt_files)
    
    for filepath in txt_files:
        chaterror(filepath)

def main():
    start_time = time.time()
    read_in_directory(config.DIRECTORY_PATH)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total running time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
