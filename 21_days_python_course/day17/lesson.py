# Day 17: 文件操作 - 读写文件 📁
# 🎯 学习目标：学会保存和读取文件
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：45 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 17        ")
print("        📁 文件操作 - 读写文件")
print("=" * 60)
print()

# ========================================
# 1. 为什么需要文件？
# ========================================
print("📖 1. 为什么需要文件？")
print("-" * 50)
print()

print("想象一下：")
print("  你写了一个很棒的日记")
print("  但是关掉电脑后，日记消失了！😢")
print()
print("💡 文件让数据永久保存！")
print("   就像把东西写在纸上，放进抽屉里")
print("   下次打开还在！")
print()

# ========================================
# 2. 打开和关闭文件
# ========================================
print("📖 2. 打开和关闭文件")
print("-" * 50)
print()

print("基本格式：")
print("  file = open('文件名', '模式')")
print("  # 操作文件")
print("  file.close()")
print()

print("文件模式：")
print("  'r' - 读取（默认，文件不存在会报错）")
print("  'w' - 写入（文件不存在会创建，存在会清空）")
print("  'a' - 追加（在文件末尾添加内容）")
print("  'x' - 创建（文件存在会报错）")
print()

# ========================================
# 3. 写入文件
# ========================================
print("📖 3. 写入文件")
print("-" * 50)
print()

# 写入文本文件
print("写入文件示例：")
print("-" * 20)
print("content = 'Hello, Python!\\n这是第二行'")
print("file = open('my_file.txt', 'w')")
print("file.write(content)")
print("file.close()")
print()

content = 'Hello, Python!\n这是第二行'
file = open('/tmp/my_file.txt', 'w')
file.write(content)
file.close()
print("✅ 已写入 /tmp/my_file.txt")
print()

# ========================================
# 4. 读取文件
# ========================================
print("📖 4. 读取文件")
print("-" * 50)
print()

# 读取整个文件
print("方法 1: read() - 读取全部")
file = open('/tmp/my_file.txt', 'r')
all_content = file.read()
file.close()
print(f"内容：{repr(all_content)}")
print()

# 读取一行
print("方法 2: readline() - 读取一行")
file = open('/tmp/my_file.txt', 'r')
first_line = file.readline()
file.close()
print(f"第一行：{repr(first_line)}")
print()

# 读取所有行
print("方法 3: readlines() - 读取所有行")
file = open('/tmp/my_file.txt', 'r')
all_lines = file.readlines()
file.close()
print(f"所有行：{all_lines}")
print()

# ========================================
# 5. with 语句（自动关闭）
# ========================================
print("📖 5. with 语句（推荐方式）")
print("-" * 50)
print()

print("问题：忘记 close() 怎么办？")
print("解决方案：用 with 语句，自动关闭！")
print()

print("格式：")
print("  with open('文件', '模式') as file:")
print("      # 操作文件")
print("  # 自动关闭，无需 file.close()")
print()

print("示例：")
with open('/tmp/my_file.txt', 'r') as file:
    content = file.read()
print(f"读取内容：{content}")
print("✅ with 语句结束后文件自动关闭")
print()

# ========================================
# 6. 逐行处理
# ========================================
print("📖 6. 逐行处理文件")
print("-" * 50)
print()

# 写入多行
lines = ['第一行内容\n', '第二行内容\n', '第三行内容\n']
with open('/tmp/multiline.txt', 'w') as file:
    file.writelines(lines)

print("逐行读取：")
with open('/tmp/multiline.txt', 'r') as file:
    for i, line in enumerate(file, 1):
        print(f"  第{i}行：{line.rstrip()}")
print()

# ========================================
# 7. 追加模式
# ========================================
print("📖 7. 追加模式 'a'")
print("-" * 50)
print()

print("'w' 模式会清空文件，'a' 模式在末尾追加：")
with open('/tmp/append_test.txt', 'w') as file:
    file.write('第一天\n')

with open('/tmp/append_test.txt', 'a') as file:
    file.write('第二天\n')
    file.write('第三天\n')

print("读取追加后的内容：")
with open('/tmp/append_test.txt', 'r') as file:
    print(file.read())
print()

# ========================================
# 8. JSON 文件操作
# ========================================
print("📖 8. JSON 文件操作")
print("-" * 50)
print()

import json

print("JSON 就像结构化的文本文件，可以存储复杂数据：")
print()

# 写入 JSON
data = {
    'name': '小明',
    'age': 10,
    'scores': [95, 88, 92]
}

with open('/tmp/data.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("写入 JSON 数据：")
print(json.dumps(data, ensure_ascii=False, indent=2))
print()

# 读取 JSON
with open('/tmp/data.json', 'r') as file:
    loaded_data = json.load(file)

print("读取 JSON 数据：")
print(f"姓名：{loaded_data['name']}")
print(f"年龄：{loaded_data['age']}")
print(f"分数：{loaded_data['scores']}")
print()

# ========================================
# 9. Python 小贴士
# ========================================
print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. 优先使用 with 语句，自动关闭文件")
print("2. 'w' 模式会清空原文件，要小心！")
print("3. 读取时指定编码：encoding='utf-8'")
print("4. JSON 可以存储字典和列表等复杂数据")
print("5. 文件路径可用相对路径或绝对路径")
print()

# ========================================
# 10. Day 17 总结
# ========================================
print("=" * 60)
print("       📋 Day 17 总结")
print("=" * 60)
print()
print("今天我们学会了：")
print("  ✅ 为什么需要文件 - 永久保存数据")
print("  ✅ open() 和 close()")
print("  ✅ 读取文件 - read(), readline(), readlines()")
print("  ✅ 写入文件 - write(), writelines()")
print("  ✅ with 语句 - 自动关闭文件")
print("  ✅ JSON 文件 - 存储结构化数据")
print()

print("=" * 60)
print("       🎉 Day 17 完成！")
print("=" * 60)
print()
print("太棒了！你的程序现在可以保存数据了！")
print()
print("===========================================")
print("     💪 继续加油！学习进度：17/21 天完成！")
print("===========================================")
