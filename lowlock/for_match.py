import re
import config
def for_match_maybeerror(log):
    # 定义正则表达式模板来匹配错误信息
   
    # 用于存储匹配成功的内容
    matched_content = set()  # 使用集合来存储匹配内容，确保唯一性

    # 匹配并合并结果
    for pattern in config.MAYBEERROR_PATTERNS:
        for match in pattern.finditer(log):
            matched_text = match.group(0)
            matched_content.add(matched_text)  # 添加匹配文本到集合中

    # 返回合并后的匹配内容
    return "\n".join(matched_content)

def for_match_assertionerror(log):
    # 定义正则表达式模板来匹配错误信息
    # 用于存储匹配成功的内容
    matched_content = set()  # 使用集合来存储匹配内容，确保唯一性

    # 匹配并合并结果
    for pattern in config.ASSERTIONERROR_PATTERNS:
        for match in pattern.finditer(log):
            matched_text = match.group(0)
            matched_content.add(matched_text)  # 添加匹配文本到集合中

    # 返回合并后的匹配内容
    return "\n".join(matched_content)
