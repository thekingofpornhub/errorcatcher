import config
import threading
file_lock = threading.Lock()
def IO(filepath,maybeerror,maybeassertionerror,deal):#将文件的写进行原子化操作
    global file_lock

    with file_lock:
        print(filepath+"io已经拿到锁")
        with open(config.ERROR_OUTPUT_FILENAME, mode=config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
            file.write(f"================================{filepath}\n")
        with open(config.ASSERTIONFAILED_OUTPUT_FILENAME, mode=config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
            file.write(f"================================{filepath}\n")
        with open(config.DEAL_OUTPUT_FILENAME, mode=config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
            file.write(f"================================{filepath}\n")
        if maybeerror:
            with open(config.TEST, config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
                file.write(maybeerror)  # 初级错误
        if maybeassertionerror:
            with open(config.ERROR_OUTPUT_FILENAME, config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
                file.write(maybeassertionerror)  # asser错误
        with open(config.DEAL_OUTPUT_FILENAME, config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
            file.write(deal)
