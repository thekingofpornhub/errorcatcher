# 编码格式
IN_ENCODING = 'utf-16le'
OUT_ENCODING = 'utf-8'
#分块大小
BIGCHUNKSIZE=10485760
BUFFERSIZE=1024
SMALLCHUNKSIZE=10240
# 输出文件名
ERROR_OUTPUT_FILENAME = 'errorout.txt'
ASSERTIONFAILED_OUTPUT_FILENAME = 'assertionfailedout.txt'
DEAL_OUTPUT_FILENAME = 'deal_out.txt'
TEST='test.txt'
# 文件状态码
INPUTWAYINDEX=1
OUTPUTWAYINDEX=0
STATUS_CODE = ['a', 'r']

# 目录路径
DIRECTORY_PATH = './test'

# Azure OpenAI 配置

#=============================================弃用的模板
# 模板
# ASSERTIONFAILED_TEMPLATE = """
# 只提取出该文件中的assertion failed以及compiler error,如果没有则不要输出任何东西(输出空)
# {body}
# """

# ERROR_TEMPLATE = """
# 只给我提取error,如果没有错误信息，不要输出任何东西（输出空）
# {body}
# """
#======================================================
ENDEAL_TEMPLATE = """
Output error and warning messages along with the solutions.
Below are the error messages: {body}
"""
CNDEAL_TEMPLATE = """
输出报错信息error和waring以及解决方案
以下是报错信息(没有信息就输出。)：{body}
"""
# 定义正则表达式模板来匹配错误信息
MAYBEERROR_PATTERNS = [
    re.compile(r'assertion failed', re.IGNORECASE),  # 匹配 assertion failed
    re.compile(r'compiler error', re.IGNORECASE),  # 匹配 compiler error
    re.compile(r'(error \w{5}):([^:]+):', re.IGNORECASE),
    re.compile(r'(error \w{4}):([^:]+):', re.IGNORECASE)
]

ASSERTIONERROR_PATTERNS = [
    re.compile(r'assertion failed', re.IGNORECASE),  # 匹配 assertion failed
    re.compile(r'compiler error', re.IGNORECASE),  # 匹配 compiler error
]
