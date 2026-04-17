# Day 20: 毕业项目 - 智能问答程序 - 参考答案
print("=" * 50)
print("       ✅ Day 20 参考答案")
print("=" * 50)
print()

import json

# ========================================
# 练习 1: 创建知识库
# ========================================
print("📝 练习 1: 创建知识库")
print("-" * 40)
print()

knowledge = {
    "你好": "你好！今天过得怎么样？",
    "你叫什么": "我叫问答小助手！",
    "再见": "再见！期待下次见面！",
    "今天天气": "天气很棒，适合出去玩！",
    "Python难吗": "Python不难，适合初学者！",
}

print(f"知识库共有 {len(knowledge)} 条：")
for q, a in knowledge.items():
    print(f"  Q: {q}")
    print(f"  A: {a}")
    print()
print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 查找答案
# ========================================
print("📝 练习 2: 查找答案函数")
print("-" * 40)
print()

def find_answer(question, kb):
    """在知识库中查找答案"""
    if question in kb:
        return kb[question]
    for q, a in kb.items():
        if question.lower() in q.lower():
            return a
    return None

tests = ["你好", "天气", "Python", "名字"]
for t in tests:
    a = find_answer(t, knowledge)
    if a:
        print(f"'{t}' → {a}")
    else:
        print(f"'{t}' → 找不到")
print()
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 添加新知识
# ========================================
print("📝 练习 3: 添加新知识")
print("-" * 40)
print()

def add_knowledge(q, a, kb):
    if q in kb:
        print(f"'{q}' 已存在，原答案：{kb[q]}")
        return False
    kb[q] = a
    print(f"✅ 已添加：{q} → {a}")
    return True

add_knowledge("喜欢吃什么", "我喜欢吃水果！", knowledge)
add_knowledge("你好", "hi", knowledge)
print()
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 删除知识
# ========================================
print("📝 练习 4: 删除知识")
print("-" * 40)
print()

def delete_knowledge(q, kb):
    if q in kb:
        deleted = kb.pop(q)
        print(f"✅ 已删除：{q} → {deleted}")
        return True
    else:
        print(f"'{q}' 不存在")
        return False

delete_knowledge("今天天气", knowledge)
delete_knowledge("不存在的问题", knowledge)
print()
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 统计功能
# ========================================
print("📝 练习 5: 统计功能")
print("-" * 40)
print()

def show_stats(kb):
    print(f"📊 知识库统计：")
    print(f"  总问题数：{len(kb)}")
    total_chars = sum(len(q) + len(a) for q, a in kb.items())
    print(f"  总字符数：{total_chars}")
    avg_len = total_chars / len(kb) if kb else 0
    print(f"  平均长度：{avg_len:.1f}")

show_stats(knowledge)
print()
print("✅ 练习 5 完成！")
print()

# ========================================
# 练习 6: 保存和加载
# ========================================
print("📝 练习 6: 保存和加载知识库")
print("-" * 40)
print()

def save_kb(kb, filename='/tmp/qa_kb.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(kb, f, ensure_ascii=False, indent=2)
    print(f"✅ 已保存 {len(kb)} 条到 {filename}")

def load_kb(filename='/tmp/qa_kb.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        print("加载失败")
        return {}

save_kb(knowledge)
loaded = load_kb()
print(f"已加载 {len(loaded)} 条")
print()
print("✅ 练习 6 完成！")
print()

# ========================================
# 综合练习
# ========================================
print("📝 综合练习: 完整问答系统")
print("-" * 40)
print()

def simple_qa_system():
    kb = {
        "你好": "你好！",
        "叫什么": "我叫小天才！",
        "再见": "再见！",
    }
    print("🤖 简单问答系统（演示）")
    print("你：你好 → 🤖: 你好！")
    print("你：叫什么 → 🤖: 我叫小天才！")
    print("你：再见 → 🤖: 再见！")

simple_qa_system()
print()
print("✅ 综合练习完成！")
print()

# ========================================
# 知识点总结
# ========================================
print("=" * 50)
print("       📊 Day 20 知识点总结")
print("=" * 50)
print()
print("✅ 知识库用字典存储问题-答案对")
print("✅ 精确匹配和模糊匹配")
print("✅ 添加、删除、修改知识")
print("✅ JSON 文件保存和加载")
print("✅ 完整的交互式问答系统")
print()
print("🎉 恭喜完成所有练习！")
print()
