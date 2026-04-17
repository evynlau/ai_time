# Day 21: 毕业项目 - 完整版 🌟
# 🎯 学习目标：完成终极毕业项目，综合展示所有技能
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：60 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 21        ")
print("        🌟 毕业项目 - 完整版 🌟")
print("=" * 60)
print()

# ========================================
# 1. 毕业感言
# ========================================
print("📖 1. 毕业感言")
print("-" * 50)
print()

print("🎓 亲爱的同学：")
print()
print("  恭喜你完成了 21 天的 Python 编程课程！")
print()
print("  你已经学会了：")
print("  ✅ Day 01-05: 基础概念（变量、数据类型、运算符）")
print("  ✅ Day 06-10: 条件与循环（if、for、while）")
print("  ✅ Day 11-15: 列表和函数（列表、字典、函数）")
print("  ✅ Day 16-18: 进阶内容（元组、集合、文件、异常）")
print("  ✅ Day 19-20: 综合练习和项目开发")
print()
print("  💡 今天，我们将创建一个完整的'个人图书馆管理系统'")
print("     作为你的毕业项目！")
print()

# ========================================
# 2. 项目设计
# ========================================
print("📖 2. 项目设计：个人图书馆管理系统")
print("-" * 50)
print()

print("📚 功能规划：")
print("  1. 添加书籍（书名、作者、分类、是否已读）")
print("  2. 查看书籍列表")
print("  3. 搜索书籍")
print("  4. 标记已读/未读")
print("  5. 删除书籍")
print("  6. 统计阅读情况")
print("  7. 保存和加载数据（JSON文件）")
print()

# ========================================
# 3. 数据结构设计
# ========================================
print("📖 3. 数据结构设计")
print("-" * 50)
print()

# 每本书用一个字典表示
sample_book = {
    'id': 1,
    'title': 'Python入门',
    'author': '张三',
    'category': '编程',
    'is_read': False
}

print("示例书籍：")
for key, value in sample_book.items():
    print(f"  {key}: {value}")
print()

# 图书馆是一个书籍列表
library = []

print("图书馆（书籍列表）：")
print(f"  library = [{len(library)} 本书]")
print()

# ========================================
# 4. 核心功能实现
# ========================================
print("📖 4. 核心功能实现")
print("-" * 50)
print()

import json
import os

# 生成唯一ID
def generate_id():
    """生成唯一的书籍ID"""
    if not library:
        return 1
    return max(book['id'] for book in library) + 1

def add_book(title, author, category):
    """添加书籍"""
    book = {
        'id': generate_id(),
        'title': title,
        'author': author,
        'category': category,
        'is_read': False
    }
    library.append(book)
    print(f"✅ 已添加：《{title}》by {author}")
    return book

def list_books():
    """列出所有书籍"""
    if not library:
        print("📚 图书馆是空的！")
        return

    print("=" * 60)
    print("                    📚 我的图书馆                    ")
    print("=" * 60)
    print(f"{'ID':^4} | {'书名':^20} | {'作者':^10} | {'分类':^8} | {'状态':^6}")
    print("-" * 60)
    for book in library:
        status = "已读 ✅" if book['is_read'] else "未读 📖"
        print(f"{book['id']:^4} | {book['title']:<20} | {book['author']:<10} | {book['category']:<8} | {status:<6}")
    print("-" * 60)
    print(f"共 {len(library)} 本书")
    print()

def search_books(keyword):
    """搜索书籍"""
    results = []
    for book in library:
        if keyword.lower() in book['title'].lower() or \
           keyword.lower() in book['author'].lower() or \
           keyword.lower() in book['category'].lower():
            results.append(book)

    if results:
        print(f"🔍 找到 {len(results)} 本相关书籍：")
        for book in results:
            print(f"  《{book['title']}》- {book['author']} ({book['category']})")
    else:
        print("🔍 没有找到相关书籍")
    print()
    return results

def mark_as_read(book_id):
    """标记为已读"""
    for book in library:
        if book['id'] == book_id:
            book['is_read'] = True
            print(f"✅ 《{book['title']}》已标记为已读")
            return True
    print(f"❌ 未找到 ID 为 {book_id} 的书籍")
    return False

def delete_book(book_id):
    """删除书籍"""
    for i, book in enumerate(library):
        if book['id'] == book_id:
            removed = library.pop(i)
            print(f"🗑️ 已删除：《{removed['title']}》")
            return True
    print(f"❌ 未找到 ID 为 {book_id} 的书籍")
    return False

def show_stats():
    """显示统计信息"""
    total = len(library)
    if total == 0:
        print("📊 图书馆是空的，暂无统计")
        return

    read_count = sum(1 for book in library if book['is_read'])
    unread_count = total - read_count

    # 按分类统计
    categories = {}
    for book in library:
        cat = book['category']
        if cat not in categories:
            categories[cat] = {'total': 0, 'read': 0}
        categories[cat]['total'] += 1
        if book['is_read']:
            categories[cat]['read'] += 1

    print("=" * 40)
    print("               📊 阅读统计 📊")
    print("=" * 40)
    print(f"  📚 总书籍数：{total}")
    print(f"  ✅ 已读：{read_count}")
    print(f"  📖 未读：{unread_count}")
    if total > 0:
        print(f"  📈 阅读进度：{read_count * 100 // total}%")
    print()
    print("  按分类：")
    for cat, data in categories.items():
        pct = data['read'] * 100 // data['total'] if data['total'] > 0 else 0
        print(f"    {cat}: {data['read']}/{data['total']} ({pct}%)")
    print()

# ========================================
# 5. 文件操作
# ========================================
print("📖 5. 文件操作：保存和加载")
print("-" * 50)
print()

def save_library(filename='/tmp/my_library.json'):
    """保存图书馆到文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(library, f, ensure_ascii=False, indent=2)
        print(f"✅ 图书馆已保存到 {filename}")
        print(f"   共保存 {len(library)} 本书")
    except Exception as e:
        print(f"❌ 保存失败：{e}")

def load_library(filename='/tmp/my_library.json'):
    """从文件加载图书馆"""
    global library
    if not os.path.exists(filename):
        print(f"📁 文件 {filename} 不存在，从空图书馆开始")
        library = []
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            library = json.load(f)
        print(f"✅ 已从 {filename} 加载 {len(library)} 本书")
    except Exception as e:
        print(f"❌ 加载失败：{e}")
        library = []

# ========================================
# 6. 菜单系统
# ========================================
print("📖 6. 菜单系统")
print("-" * 50)
print()

def show_menu():
    """显示菜单"""
    print("=" * 40)
    print("       📚 个人图书馆管理系统 📚")
    print("=" * 40)
    print("  1. 📖 添加书籍")
    print("  2. 📚 查看书籍列表")
    print("  3. 🔍 搜索书籍")
    print("  4. ✅ 标记为已读")
    print("  5. 🗑️  删除书籍")
    print("  6. 📊 统计信息")
    print("  7. 💾 保存图书馆")
    print("  8. 📂 加载图书馆")
    print("  0. 🚪 退出系统")
    print("=" * 40)
    print()

def run_system():
    """运行图书馆管理系统"""
    global library

    print()
    print("🎓 欢迎使用个人图书馆管理系统！")
    print()

    # 尝试自动加载
    try:
        load_library('/tmp/my_library.json')
    except:
        pass

    while True:
        show_menu()
        try:
            choice = input("请选择操作 (0-8)：").strip()
        except EOFError:
            print("（非交互环境）")
            break

        if choice == '0':
            print("\n📚 感谢使用！再见！")
            print("💾 自动保存中...")
            save_library('/tmp/my_library.json')
            break

        elif choice == '1':
            print("\n--- 添加书籍 ---")
            title = input("书名：").strip()
            author = input("作者：").strip()
            category = input("分类：").strip() or "未分类"
            if title:
                add_book(title, author, category)
            else:
                print("❌ 书名不能为空！")

        elif choice == '2':
            print()
            list_books()

        elif choice == '3':
            keyword = input("\n🔍 输入搜索关键词：").strip()
            if keyword:
                search_books(keyword)
            else:
                print("❌ 请输入搜索关键词！")

        elif choice == '4':
            book_id = input("\n✅ 输入要标记的书籍ID：").strip()
            if book_id.isdigit():
                mark_as_read(int(book_id))
            else:
                print("❌ 请输入有效的ID！")

        elif choice == '5':
            book_id = input("\n🗑️ 输入要删除的书籍ID：").strip()
            if book_id.isdigit():
                delete_book(int(book_id))
            else:
                print("❌ 请输入有效的ID！")

        elif choice == '6':
            print()
            show_stats()

        elif choice == '7':
            save_library('/tmp/my_library.json')

        elif choice == '8':
            load_library('/tmp/my_library.json')

        else:
            print("❌ 无效选择！请输入 0-8")

        input("\n按回车继续...")

# ========================================
# 7. 系统演示
# ========================================
print("📖 7. 系统演示")
print("-" * 50)
print()

print("--- 添加演示书籍 ---")
add_book('Python入门', '张三', '编程')
add_book('数据结构', '李四', '编程')
add_book('红楼梦', '曹雪芹', '文学')
add_book('三体', '刘慈欣', '科幻')
add_book('人类简史', '尤瓦尔', '历史')
print()

print("--- 查看书籍列表 ---")
list_books()

print("--- 搜索书籍 ---")
search_books('Python')
search_books('刘慈欣')
print()

print("--- 标记已读 ---")
mark_as_read(1)
mark_as_read(3)
print()

print("--- 统计信息 ---")
show_stats()

print("--- 保存图书馆 ---")
save_library('/tmp/my_library.json')
print()

# ========================================
# 8. Day 21 总结
# ========================================
print("=" * 60)
print("       📋 Day 21 总结")
print("=" * 60)
print()
print("今天我们完成了：")
print("  ✅ 个人图书馆管理系统 - 完整版")
print("  ✅ 添加、查看、搜索、标记、删除书籍")
print("  ✅ 阅读统计功能")
print("  ✅ JSON 文件保存和加载")
print("  ✅ 菜单式交互系统")
print()

print("🎓 毕业感言：")
print("  恭喜你完成了 21 天的 Python 编程课程！")
print("  你从一个编程新手，成长为一个能够独立")
print("  开发小程序的小程序员了！")
print()
print("  记住：编程最重要的不是记住所有语法，")
print("  而是学会解决问题的思维方法！")
print()
print("  继续加油，未来可期！🚀")
print()

print("=" * 60)
print("       🎓 恭喜毕业！🎓")
print("=" * 60)
print()
print("===========================================")
print("     🎉 学习进度：21/21 天全部完成！")
print("===========================================")
