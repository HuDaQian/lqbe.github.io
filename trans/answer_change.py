def transform_answers(row):
    options = row["question_options"]
    if isinstance(options, int):
        options = str(options)
    elif isinstance(options, str):
        if len(options) == 0:
            print("empty options.")
            return ""
    else:
        print("type error.")
        return ""
    new_value = options.replace("：", ":").replace("\n","").replace("\r","").strip()
    # 增加中文顿号处理，选项中顿号正常使用的有且只有一例，所以判断处理下
    if "A、B" not in options:
        new_value = new_value.replace("、", ":")
    print(new_value)
    if "判断题" == row["question_class"]:
        return "对|错"
    else:
        order_index = ["A:","B:","C:","D:","E:","F:","G:"]
        deal_value = split_string_by_keywords(new_value, order_index)
        print(deal_value)
        return "|".join(deal_value)
    
    print("转换失败")
    return answer_str

def split_string_by_keywords(input_string, keywords):
    # 初始化一个结果列表
    result = []
    # 用于追踪当前分割位置
    last_index = 0

    # 当前字符串长度
    input_length = len(input_string)

    while last_index < input_length:
        # 找到下一个关键词的最小索引
        next_keyword_index = -1
        next_keyword = None

        # 遍历关键词以找到下一个关键词
        for keyword in keywords:
            index = input_string.find(keyword, last_index)
            if index != -1 and (next_keyword_index == -1 or index < next_keyword_index):
                next_keyword_index = index
                next_keyword = keyword

        # 如果没有找到任何关键词，结束循环
        if next_keyword_index == -1:
            break

        # 将关键词之前的部分添加到结果列表
        if last_index < next_keyword_index:
            result.append(input_string[last_index:next_keyword_index].strip())

        # 将当前关键词及其后面的内容一起添加到结果
        last_index = next_keyword_index + len(next_keyword)

    # 添加最后一个分割后的部分（如果有的话）
    if last_index < input_length:
        result.append(input_string[last_index:].strip())

    return result


def transform_correct(row):
    corrects = row["question_correct"]
    if isinstance(corrects, int):
        corrects = str(corrects)
    elif isinstance(corrects, str):
        if len(corrects) == 0:
            print("empty corrects.")
            return ""
    else:
        print("type error.")
        return ""
    new_value = corrects.replace("：", ":").replace("\n","").replace("\r","").strip()
    print(new_value)
    if ":" in new_value:
        print("wrong correct answer")
    if "判断题" == row["question_class"]:
        return "A" if new_value == "对" else "B"        
    else:
        print("corrects")
        print(corrects)
        return "|".join(list(new_value))
