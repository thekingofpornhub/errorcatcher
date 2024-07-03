from file_utils import read_large_file_with_buffer
from file_utils import split_large_string
from openai_utils import autodeal
import time
from for_match import for_match_assertionerror
from for_match import for_match_maybeerror
import config

def chaterror(filepath):
    chunksize = 0  # 计数器
    start_time = time.time()  # 记录开始时间

    # 输出文件头部信息
    with open(config.ERROR_OUTPUT_FILENAME, mode=config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
        file.write(f"================================{filepath}\n")
    with open(config.ASSERTIONFAILED_OUTPUT_FILENAME, mode=config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
        file.write(f"================================{filepath}\n")
    with open(config.DEAL_OUTPUT_FILENAME, mode=config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
        file.write(f"================================{filepath}\n")
    
    maybeerror = ''
    maybeassertionerror = ''
    
    # 逐块读取文件并进行匹配
    for chunk in read_large_file_with_buffer(filepath):
        chunksize += 1
        inputtxt = chunk
        for chunksmall in split_large_string(inputtxt):
            maybeassertionerror += for_match_assertionerror(chunksmall)
            maybeerror += for_match_maybeerror(chunksmall)
        
        print(f"在 {filepath} 的第 {chunksize} 块处理完成")

    # 输出匹配结果
    print(f"筛选处理总耗时：{time.time() - start_time:.2f}秒")
    print(maybeerror)
    # 将匹配结果写入文件
    with open(config.TEST, config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
        file.write(maybeerror)  # 初级错误
    
    with open(config.ERROR_OUTPUT_FILENAME, config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
        file.write(maybeassertionerror)  # asser错误
    
    print("处理完成")

    # 进行进一步的处理
    with open(config.DEAL_OUTPUT_FILENAME, config.STATUS_CODE[config.OUTPUTWAYINDEX], encoding=config.OUT_ENCODING) as file:
        deal = autodeal(maybeerror, config.CNDEAL_TEMPLATE)
        print(deal)
        if deal:
            file.write(deal)

