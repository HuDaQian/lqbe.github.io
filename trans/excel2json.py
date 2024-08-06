import pandas as pd
import json
import answer_change

# 读取Excel表格中的内容
df = pd.read_excel('./Template.xlsx', header=[0,1])

# 空单元格补充成空字符串
df.fillna('', inplace=True)

# 定义列名到JSON字段的映射
columns_mapping = {
    '一、试题部分_序号':'question_index',
    '一、试题部分_部分':'question_section',
    '一、试题部分_章':'question_paragraph',
    '一、试题部分_节':'question_item',
    '一、试题部分_题型':'question_class',
    '一、试题部分_试题内容':'question_info',
    '一、试题部分_答案选项':'question_options',
    '一、试题部分_正确答案':'question_correct',
    '二、出处部分_参考用书':'answer_book',
    '二、出处部分_章':'answer_paragraph',
    '二、出处部分_节':'answer_item',
    '二、出处部分_部分':'answer_section',
    '二、出处部分_内容':'answer_content',
    '题目类型':'record_type',
    '新增试题备注':'record_note',
    '变动备注':'record_change'
}

# 标题合并
df.columns = [f'{col[0]}_{col[1]}' if 'Unnamed' not in col[1] else f'{col[0]}' for col in df.columns]

# 标题转换
df = df.rename(columns=columns_mapping)

# 试题选项预处理
df['question_options'] = df.apply(answer_change.transform_answers, axis=1)

# 正确答案与处理
df['question_correct'] = df.apply(answer_change.transform_correct, axis=1)

# 将DataFrame转换成JSON
records = df.to_dict('records')

# 写入JSON文件
with open('data_2023.json', 'w') as f:
    json.dump(records, f, indent=None)

