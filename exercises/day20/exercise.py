# Day 20 课后练习题 - 综合练习
print("练习 1: 学生管理系统")

# 学生列表 (用字典)
students = [
    {"name": "小明", "age": 8, "score": 90},
    {"name": "小红", "age": 9, "score": 95},
    {"name": "小刚", "age": 8, "score": 85}
]

print("📚 学生列表:")
for i, student in enumerate(students, 1):
    print(f"{i}. {student['name']}, {student['age']}岁，成绩:{student['score']}")

# 🎯 挑战：添加新学生
print("\n➕ 添加新学生:")

new_student = {"name": "小丽", "age": 10, "score": 88}
students.append(new_student)
print(f"✅ 添加了{new_student['name']}")

print("\n📚 更新后的列表:")
for i, student in enumerate(students, 1):
    print(f"{i}. {student['name']}, {student['age']}岁，成绩:{student['score']}")

# 计算平均分
total_score = 0
for student in students:
    total_score += student['score']

average = total_score / len(students)
print(f"\n📊 平均成绩：{average:.1f}")
