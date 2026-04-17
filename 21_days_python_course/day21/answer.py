# Day 21: 毕业项目 - 完整版 - 参考答案
print("=" * 50)
print("       ✅ Day 21 参考答案")
print("=" * 50)
print()

import json

# ========================================
# 练习 1: 创建书籍字典
# ========================================
print("📝 练习 1: 创建书籍字典")
print("-" * 40)
print()

book = {
    'id': 1,
    'title': 'Python编程',
    'author': '张三',
    'category': '编程',
    'is_read': False
}

print(f"书籍信息：")
for key, value in book.items():
    print(f"  {key}: {value}")
print()
print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 创建图书馆列表
# ========================================
print("📝 练习 2: 创建图书馆列表")
print("-" * 40)
print()

library = [
    {'id': 1, 'title': 'Python入门', 'author': '张三', 'category': '编程', 'is_read': False},
    {'id': 2, 'title': '数据结构', 'author': '李四', 'category': '编程', 'is_read': True},
    {'id': 3, 'title': '红楼梦', 'author': '曹雪芹', 'category': '文学', 'is_read': True},
]

print(f"图书馆共有 {len(library)} 本书：")
for book in library:
    status = "已读" if book['is_read'] else "未读"
    print(f"  《{book['title']}》- {book['author']} [{status}]")
print()
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 添加书籍函数
# ========================================
print("📝 练习 3: 添加书籍函数")
print("-" * 40)
print()

def add_book(library, title, author, category='未分类'):
    new_id = max(b['id'] for b in library) + 1 if library else 1
    book = {
        'id': new_id,
        'title': title,
        'author': author,
        'category': category,
        'is_read': False
    }
    library.append(book)
    print(f"✅ 已添加：{title}")
    return book

add_book(library, '三体', '刘慈欣', '科幻')
add_book(library, '人类简史', '尤瓦尔', '历史')
print(f"\n图书馆现有 {len(library)} 本书")
print()
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 搜索书籍
# ========================================
print("📝 练习 4: 搜索书籍")
print("-" * 40)
print()

def search_books(library, keyword):
    results = []
    for book in library:
        if keyword.lower() in book['title'].lower() or \
           keyword.lower() in book['author'].lower():
            results.append(book)
    return results

results = search_books(library, 'Python')
print(f"搜索'Python'结果：{len(results)} 本")
for b in results:
    print(f"  《{b['title']}》")

results = search_books(library, '刘慈欣')
print(f"\n搜索'刘慈欣'结果：{len(results)} 本")
for b in results:
    print(f"  《{b['title']}》")
print()
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 统计功能
# ========================================
print("📝 练习 5: 统计功能")
print("-" * 40)
print()

def show_stats(library):
    total = len(library)
    read = sum(1 for b in library if b['is_read'])
    unread = total - read

    categories = {}
    for b in library:
        cat = b['category']
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += 1

    print("=" * 40)
    print("           📊 统计信息")
    print("=" * 40)
    print(f"  总数：{total}")
    print(f"  已读：{read}")
    print(f"  未读：{unread}")
    if total > 0:
        print(f"  进度：{read * 100 // total}%")
    print(f"  分类：{categories}")
    print()

show_stats(library)
print("✅ 练习 5 完成！")
print()

# ========================================
# 练习 6: 保存和加载
# ========================================
print("📝 练习 6: 保存和加载")
print("-" * 40)
print()

def save_library(library, filename='/tmp/library.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(library, f, ensure_ascii=False, indent=2)
    print(f"✅ 已保存 {len(library)} 本书")

def load_library(filename='/tmp/library.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

save_library(library)
loaded = load_library()
print(f"已加载 {len(loaded)} 本书")
print()
print("✅ 练习 6 完成！")
print()

# ========================================
# 综合练习
# ========================================
print("📝 综合练习: 完整管理系统")
print("-" * 40)
print()

def run_demo():
    my_library = []

    print("1. 添加书籍")
    add_book(my_library, 'Python入门', '张三', '编程')
    add_book(my_library, '数据结构', '李四', '编程')
    add_book(my_library, '红楼梦', '曹雪芹', '文学')
    print()

    print("2. 书籍列表")
    for b in my_library:
        status = "已读" if b['is_read'] else "未读"
        print(f"  《{b['title']}》[{status}]")
    print()

    print("3. 搜索'编程'")
    results = search_books(my_library, '编程')
    for b in results:
        print(f"  《{b['title']}》")
    print()

    print("4. 统计")
    show_stats(my_library)

run_demo()
print()
print("✅ 综合练习完成！")
print()

# ========================================
# 知识点总结
# ========================================
print("=" * 50)
print("       📊 21天课程知识点总结")
print("=" * 50)
print()
print("✅ Day 01-05: 变量、数据类型、运算符")
print("✅ Day 06-10: if语句、for循环、while循环")
print("✅ Day 11-15: 列表、字典、函数、返回值")
print("✅ Day 16-18: 元组、集合、文件操作、异常处理")
print("✅ Day 19-20: 综合练习、智能问答系统")
print("✅ Day 21: 毕业项目、图书馆管理系统")
print()
print("🎓 恭喜毕业！你已经是小程序员了！")
print()
