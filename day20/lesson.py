# Day 20: 综合练习 - 学生管理系统
# 🎯 学习目标：综合运用所有知识
#
# 📖 故事：创建简单的学生管理系统!
# 记录学生姓名、年龄、成绩

# 使用字典列表
students = []

# 添加学生
students.append({
    "name": "小明",
    "age": 8,
    "score": 90
})

students.append({
    "name": "小红",
    "age": 9,
    "score": 95
})

students.append({
    "name": "小华",
    "age": 8,
    "score": 85
})

# 显示所有学生
print("📚 学生列表:")
for i, student in enumerate(students, 1):
    print(f"{i}. {student['name']}, {student['age']}岁, 成绩:{student['score']}")

# 平均成绩
total = 0
for student in students:
    total += student['score']
average = total / len(students)

print(f"📊 平均成绩：{average:.1f}")

# 🎮 练习：添加新学生
def add_student(name, age, score):
    new_student = {"name": name, "age": age, "score": score}
    students.append(new_student)
    print(f"✅ 添加了{name}!")

add_student("小丽", 10, 88)

print()
print("📚 更新后的学生列表:")
for i, student in enumerate(students, 1):
    print(f"{i}. {student['name']}, {student['age']}岁, 成绩:{student['score']}")
