import os
import config

def get_txt_files(directory):
    txt_files = []
    for filename in os.listdir(directory):#将txt结尾的文件路径写入
        if filename.endswith('.txt'):
            txt_files.append(os.path.join(directory, filename))
    return txt_files

def read_large_file_with_buffer(file_path, chunk_size=config.BIGCHUNKSIZE, buffersize=config.BUFFERSIZE):
    with open(file_path, config.STATUS_CODE[config.INPUTWAYINDEX], encoding=config.IN_ENCODING) as file:
        buffer = ''
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield buffer + chunk#丢出块
            buffer = chunk[-(buffersize // 2):]#负索引等于从后往前
def split_large_string(bigchunk, chunk_size=config.SMALLCHUNKSIZE, buffer_size=config.BUFFERSIZE):
    buffer = ''
    index = 0
    while index < len(bigchunk):
        chunk = bigchunk[index:index + chunk_size]
        yield buffer + chunk
        buffer = chunk[-(buffer_size // 2):]
        index += chunk_size - (buffer_size // 2)