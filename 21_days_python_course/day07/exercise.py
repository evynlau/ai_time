# Day 7 练习题：编程小天才挑战！ 🎯

## 目标：完善你的计算器程序

### 练习 1: 测试你的加法函数
编写一个函数，测试两个数的加法。
```python
# 写出你的加法函数
def test_addition(num1, num2):
    # 你的代码在这里
    # 返回两个数的和
    pass

# 测试
result = test_addition(10, 20)
print(f"10 + 20 = {result}")  # 应该输出 30
```

### 练习 2: 完成减法函数
减法函数中，需要确保不会出现负数结果（对小一点的数减大一点的数）。
```python
def test_subtraction(num1, num2):
    # 你的代码在这里
    # 如果 num1 < num2，返回"不能相减，num1 较小"
    # 否则返回 num1 - num2 的结果
    pass

# 测试
print(test_subtraction(10, 5))   # 应该输出 5
print(test_subtraction(5, 10))   # 应该输出"不能相减，num1 较小"
```

### 练习 3: 处理除法中的零
除法函数需要处理除数为 0 的情况，这是编程中的常见错误。
```python
def test_division(num1, num2):
    # 你的代码在这里
    # 如果 num2 为 0，返回"错误：除数不能为 0!"
    # 否则返回 num1 / num2 的结果
    pass

# 测试
print(test_division(20, 4))      # 应该输出 5.0
print(test_division(10, 0))      # 应该输出"错误：除数不能为 0!"
```

### 练习 4: 编写乘法表生成器
使用循环，生成一个数的乘法表（比如 2 的乘法表）。
```python
def generate_multiplication_table(number):
    # 你的代码在这里
    # 使用循环生成 1-10 的乘法表
    # 格式：number × 1 = result, number × 2 = result, ...
    pass

# 测试
generate_multiplication_table(3)
# 输出应该是:
# 3 × 1 = 3
# 3 × 2 = 6
# 3 × 3 = 9
# ... 
# 3 × 10 = 30
```

### 练习 5: 计算器升级 - 添加平方根功能
使用 math 模块计算平方根。
```python
import math

def calculate_square_root(number):
    # 你的代码在这里
    # 如果 number < 0，返回"错误：不能计算负数的平方根"
    # 否则返回数学根号下的 number
    pass

# 测试
print(calculate_square_root(16))     # 应该输出 4.0
print(calculate_square_root(-4))     # 应该输出"错误：不能计算负数的平方根"
```

### 练习 6: 编写幂运算函数
学习指数运算，自己实现一个幂函数。
```python
def power(base, exponent):
    # 你的代码在这里
    # 计算 base 的 exponent 次方
    # 例如: power(2, 3) = 2 × 2 × 2 = 8
    pass

# 测试
print(power(2, 3))   # 应该输出 8 (2³ = 8)
print(power(5, 2))   # 应该输出 25 (5² = 25)
print(power(3, 0))   # 应该输出 1 (任何数的 0 次方等于 1)
```

### 练习 7: 创建成绩评分器
根据分数判断等级。
```python
def grade(score):
    # 你的代码在这里
    # 90-100: 'A'
    # 80-89: 'B'
    # 70-79: 'C'
    # 60-69: 'D'
    # <60: 'F'
    pass

# 测试
print(grade(95))     # 应该输出 'A'
print(grade(85))     # 应该输出 'B'
print(grade(72))     # 应该输出 'C'
print(grade(65))     # 应该输出 'D'
print(grade(45))     # 应该输出 'F'
```

### 练习 8: 编写密码验证器
学习字符串和条件判断。
```python
def check_password(password):
    # 你的密码验证函数
    # 密码规则:
    # - 至少 8 个字符
    # - 包含至少一个数字
    # - 包含至少一个大写字母
    # 如果满足所有规则，返回"密码安全"
    # 否则返回"密码不安全"
    pass

# 测试
print(check_password("MyPass123"))     # 应该输出"密码安全"
print(check_password("short1"))        # 应该输出"密码不安全"
print(check_password("NoNumber"))      # 应该输出"密码不安全"
print(check_password("NoCapital1"))    # 应该输出"密码不安全"
print(check_password("abc"))           # 应该输出"密码不安全"
```

### 练习 9: 计算列表平均值
学习列表操作和数学运算。
```python
def calculate_average(scores):
    # 你的代码在这里
    # 计算列表 scores 中所有数字的平均值
    # 例如: [85, 90, 78, 92, 88] 的平均值是 86.6
    pass

# 测试
scores = [85, 90, 78, 92, 88]
print(f"平均分: {calculate_average(scores)}")  # 应该输出 86.6
```

### 练习 10: 创建猜数字游戏（最终挑战！）
综合运用所有知识，创建一个有趣的游戏。
```python
import random

def guessing_game():
    # 你的代码在这里
    # 程序随机选择一个 1-100 之间的数字
    # 用户猜测，程序提示"太大了"或"太小了"
    # 用户猜中后，显示"恭喜你！猜对了"和"你猜了 X 次"
    
    # 提示：
    # 1. 使用 random.randint(1, 100) 生成随机数
    # 2. 使用 while 循环直到猜中
    # 3. 使用 input() 获取用户输入
    # 4. 使用 if-elif-else 判断大小
    # 5. 使用计数器记录猜测次数
    pass

# 运行游戏
guessing_game()
```

---

## 🌟 进阶挑战

### 挑战 A: 科学计算器
添加更多功能：
- 计算绝对值 (`abs()`)
- 计算最大值和最小值 (`max()`, `min()`)
- 四舍五入 (`round()`)

### 挑战 B: 分数计算器
创建一个分数计算器，可以：
- 分数的加法、减法、乘法、除法
- 显示最简分数

### 挑战 C: 货币转换器
创建一个货币转换器：
- 美元转人民币
- 人民币转美元
- 汇率可以修改

---

## 💡 学习提示

1. **先理解问题**: 仔细阅读每个练习的要求
2. **小步测试**: 写完代码就运行测试
3. **利用注释**: 在思考不清楚时写下注释
4. **查看答案**: 卡住时可以参考答案，但尽量自己写
5. **挑战自己**: 完成所有练习后，尝试进阶挑战

记住：编程就像搭积木，一步一步来，你一定能成功！🎉