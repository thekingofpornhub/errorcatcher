from error_processing import chaterror
from file_utils import get_txt_files
import concurrent.futures
import threading
def read_in_directory(directorypath):
    txt_files = get_txt_files(directorypath)
    print(txt_files)
    file_lock = threading.Lock()
    with concurrent.futures.ThreadPoolExecutor() as executor:#线程池创建
        # 将chaterror函数应用于每个txt文件路径
        
        executor.map(chaterror, txt_files)#线程池中添加线程，并发的将txt——files每一个元素进行chaterrir并发
