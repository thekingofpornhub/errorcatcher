import re

def for_match_maybeerror(log):
    # 定义正则表达式模板来匹配错误信息
    MAYBEERROR_PATTERNS = [
    re.compile(r'assertion failed', re.IGNORECASE),  # 匹配 assertion failed
    re.compile(r'compiler error', re.IGNORECASE),  # 匹配 compiler error
    re.compile(r'(error \w{5}):([^:]+):', re.IGNORECASE),
    re.compile(r'(error \w{4}):([^:]+):', re.IGNORECASE)
]
    # 用于存储匹配成功的内容
    matched_content = set()  # 使用集合来存储匹配内容，确保唯一性
    
    # 匹配并合并结果
    for pattern in MAYBEERROR_PATTERNS:
        for match in pattern.finditer(log):
            matched_text = match.group(0)
            matched_content.add(matched_text)  # 添加匹配文本到集合中

    # 返回合并后的匹配内容
    return "\n".join(matched_content)

def for_match_assertionerror(log):
    # 定义正则表达式模板来匹配错误信息
    # 用于存储匹配成功的内容
    matched_content = set()  # 使用集合来存储匹配内容，确保唯一性
    ASSERTIONERROR_PATTERNS = [
    re.compile(r'assertion failed', re.IGNORECASE),  # 匹配 assertion failed
    re.compile(r'compiler error', re.IGNORECASE),  # 匹配 compiler error
]
    # 匹配并合并结果
    for pattern in ASSERTIONERROR_PATTERNS:
        for match in pattern.finditer(log):
            matched_text = match.group(0)
            matched_content.add(matched_text)  # 添加匹配文本到集合中

    # 返回合并后的匹配内容
    return "\n".join(matched_content)
