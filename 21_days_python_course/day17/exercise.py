# Day 17: 文件操作 - 练习
print("=" * 50)
print("       📝 Day 17 练习：文件操作")
print("=" * 50)
print()

import json
import os

# ========================================
# 练习 1: 写入文本文件
# ========================================
print("🎯 练习 1: 写入文本文件")
print("-" * 40)
print()

content = "Hello, Python!\n我学会了文件操作！"
with open('/tmp/hello.txt', 'w', encoding='utf-8') as file:
    file.write(content)

print("✅ 已写入 /tmp/hello.txt")
print()

# ========================================
# 练习 2: 读取文本文件
# ========================================
print("🎯 练习 2: 读取文本文件")
print("-" * 40)
print()

with open('/tmp/hello.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print(f"读取内容：{content}")
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 逐行读取
# ========================================
print("🎯 练习 3: 逐行读取")
print("-" * 40)
print()

lines = ['第一行\n', '第二行\n', '第三行\n', '第四行\n']
with open('/tmp/lines.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines)

print("逐行显示：")
with open('/tmp/lines.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file, 1):
        print(f"  第{i}行：{line.rstrip()}")
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 追加内容
# ========================================
print("🎯 练习 4: 追加内容")
print("-" * 40)
print()

with open('/tmp/diary.txt', 'w', encoding='utf-8') as file:
    file.write('4月1日：今天开始学Python\n')

with open('/tmp/diary.txt', 'a', encoding='utf-8') as file:
    file.write('4月2日：学会了变量\n')
    file.write('4月3日：学会了循环\n')

print("日记内容：")
with open('/tmp/diary.txt', 'r', encoding='utf-8') as file:
    print(file.read())
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 统计文件行数
# ========================================
print("🎯 练习 5: 统计文件行数")
print("-" * 40)
print()

line_count = 0
with open('/tmp/lines.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line_count += 1

print(f"/tmp/lines.txt 共有 {line_count} 行")
print("✅ 练习 5 完成！")
print()

# ========================================
# 练习 6: JSON 写入和读取
# ========================================
print("🎯 练习 6: JSON 写入和读取")
print("-" * 40)
print()

# 写入 JSON
student = {
    'name': '小明',
    'age': 10,
    'grade': '四年级',
    'scores': {'语文': 95, '数学': 88, '英语': 92}
}

with open('/tmp/student.json', 'w', encoding='utf-8') as file:
    json.dump(student, file, ensure_ascii=False, indent=2)

print("写入 JSON：")
print(json.dumps(student, ensure_ascii=False, indent=2))
print()

# 读取 JSON
with open('/tmp/student.json', 'r', encoding='utf-8') as file:
    loaded = json.load(file)

print("读取 JSON：")
print(f"姓名：{loaded['name']}")
print(f"年龄：{loaded['age']}")
print(f"分数：{loaded['scores']}")
print("✅ 练习 6 完成！")
print()

# ========================================
# 练习 7: 保存多个学生信息
# ========================================
print("🎯 练习 7: 保存多个学生信息")
print("-" * 40)
print()

students = [
    {'name': '小明', 'age': 10, 'score': 95},
    {'name': '小红', 'age': 11, 'score': 88},
    {'name': '小刚', 'age': 10, 'score': 92}
]

with open('/tmp/students.json', 'w', encoding='utf-8') as file:
    json.dump(students, file, ensure_ascii=False, indent=2)

with open('/tmp/students.json', 'r', encoding='utf-8') as file:
    loaded_students = json.load(file)

print("学生列表：")
for s in loaded_students:
    print(f"  {s['name']}，{s['age']}岁，分数{s['score']}")
print("✅ 练习 7 完成！")
print()

# ========================================
# 练习 8: 读写 CSV 格式（简单版）
# ========================================
print("🎯 练习 8: 简单 CSV 格式")
print("-" * 40)
print()

# CSV 就是用逗号分隔的值
csv_content = "姓名,年龄,分数\n小明,10,95\n小红,11,88\n小刚,10,92"

with open('/tmp/grades.csv', 'w', encoding='utf-8') as file:
    file.write(csv_content)

print("CSV 内容：")
with open('/tmp/grades.csv', 'r', encoding='utf-8') as file:
    for line in file:
        print(f"  {line.rstrip()}")
print("✅ 练习 8 完成！")
print()

# ========================================
# 完成
# ========================================
print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
print()
print("今天学到了：")
print("  ✅ 写入文件 write()")
print("  ✅ 读取文件 read(), readlines()")
print("  ✅ 追加模式 'a'")
print("  ✅ with 语句自动关闭")
print("  ✅ JSON 读写 json.dump/load()")
print("  ✅ 简单 CSV 格式")
print()
print("🎉 明天学习异常处理！")
print()
