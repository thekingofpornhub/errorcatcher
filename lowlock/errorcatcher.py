from read_in_dircetory import read_in_directory
import config
import time

def errorcatcher():
    start_time = time.time()
    read_in_directory(config.DIRECTORY_PATH)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total running time: {elapsed_time} seconds")


