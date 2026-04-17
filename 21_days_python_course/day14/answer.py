"""
✅ Day 14 解答：字串運算 🎯
===============================
練習題的參考答案，
請先自己嘗試完成後再來參考喔！💪
"""

# =============================================================================
# 練習 1：字串索引基本功 🔢
# =============================================================================

print("=" * 50)
print("✅ 練習 1：字串索引基本功")
print("=" * 50)

text = "Python Programming"

# 第一個字元
first_char = text[0]
print(f"第一個字元：{first_char}")  # P

# 倒數第一個字元
last_char = text[-1]
print(f"倒數第一個字元：{last_char}")  # g

# 第 8 個字元（索引從 0 開始，所以是 text[7]）
eighth_char = text[7]
print(f"第 8 個字元：{eighth_char}")  # P

print()

# =============================================================================
# 練習 2：字串切片高手 ✂️
# =============================================================================

print("=" * 50)
print("✅ 練習 2：字串切片高手")
print("=" * 50)

text = "Hello, World!"

# 取出 "Hello"
hello_part = text[0:5]
print(f"取出 'Hello'：{hello_part}")

# 取出 "World"（不包含驚嘆號）
world_part = text[7:12]
print(f"取出 'World'：{world_part}")

# 將字串反轉
reversed_text = text[::-1]
print(f"反轉字串：{reversed_text}")

print()

# =============================================================================
# 練習 3：字串方法實作 🔧
# =============================================================================

print("=" * 50)
print("✅ 練習 3：字串方法實作")
print("=" * 50)

user_input = "   python is fun!   "

# 處理流程
step1 = user_input.strip()           # 移除首尾空白
step2 = step1.upper()                # 全部轉大寫
step3 = step2.replace("PYTHON", "Python")  # 取代

print(f"原始輸入：'{user_input}'")
print(f"處理後：'{step3}'")

print()

# =============================================================================
# 練習 4：分割與合併 🔄
# =============================================================================

print("=" * 50)
print("✅ 練習 4：分割與合併")
print("=" * 50)

# 題目 4a：將句子分割成單字
sentence = "The quick brown fox jumps over"
words = sentence.split(" ")
print(f"分割結果：{words}")
# 輸出：['The', 'quick', 'brown', 'fox', 'jumps', 'over']

# 題目 4b：將單字用 "-" 連接起來
connected = "-".join(words)
print(f"連接結果：{connected}")
# 輸出：The-quick-brown-fox-jumps-over

print()

# =============================================================================
# 練習 5：會員測試大作戰 🔎
# =============================================================================

print("=" * 50)
print("✅ 練習 5：會員測試大作戰")
print("=" * 50)

emails = [
    "alice@example.com",
    "bob@school.edu",
    "invalid email.com",    # 包含空格
    "missing@at",           # 缺少 .
    "noatall.com"           # 缺少 @
]

def is_valid_email(email):
    has_at = "@" in email
    has_dot = "." in email
    has_space = " " in email
    return has_at and has_dot and not has_space

print("郵箱有效性檢查：")
for email in emails:
    valid = is_valid_email(email)
    status = "✅ 有效" if valid else "❌ 無效"
    print(f"  {email}：{status}")

print()

# =============================================================================
# 練習 6：f-string 格式化高手 📊
# =============================================================================

print("=" * 50)
print("✅ 練習 6：f-string 格式化高手")
print("=" * 50)

name = "小明"
age = 12
score = 95.5

# 使用 f-string 產生格式輸出
output = f"""════════════════════════
姓名：{name}
年齡：{age} 歲
成績：{score} 分
════════════════════════"""

print(output)

print()

# =============================================================================
# 練習 7：實作反轉字串函數 🔄
# =============================================================================

print("=" * 50)
print("✅ 練習 7：實作反轉字串函數")
print("=" * 50)

def reverse_string(s):
    """反轉輸入的字串"""
    return s[::-1]

# 測試
test_cases = ["hello", "Python", "字串反轉", "12345"]
for test in test_cases:
    result = reverse_string(test)
    print(f"reverse_string('{test}') = '{result}'")

print()

# =============================================================================
# 練習 8：統計字元出現次數 📊
# =============================================================================

print("=" * 50)
print("✅ 練習 8：統計字元出現次數")
print("=" * 50)

text = "abracadabra"

# 統計 'a' 出現的次數
a_count = text.count('a')
print(f"'a' 出現的次數：{a_count}")

# 統計每個字元（不重複）
unique_chars = set(text)
print(f"不重複字元：{unique_chars}")

# 統計每個字元出現次數
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print("各字元出現次數：")
for char, count in char_count.items():
    print(f"  '{char}': {count} 次")

print()

# =============================================================================
# 練習 9：驗證輸入 💡
# =============================================================================

print("=" * 50)
print("✅ 練習 9：驗證輸入")
print("=" * 50)

def check_password_strength(password):
    """
    檢查密碼強度
    返回：強（符合所有條件）/ 弱（不符合條件）
    """
    # 檢查長度
    if len(password) < 8:
        return "弱（長度不足 8 字元）"
    
    # 檢查是否包含數字
    has_digit = any(c.isdigit() for c in password)
    
    # 檢查是否包含大寫字母
    has_upper = any(c.isupper() for c in password)
    
    if has_digit and has_upper:
        return "強 ✅"
    else:
        reasons = []
        if not has_digit:
            reasons.append("需要數字")
        if not has_upper:
            reasons.append("需要大寫字母")
        return "弱（" + "，".join(reasons) + "）"

# 測試
passwords = ["abc123", "Password1", "short1A", "VeryLongPassword123"]
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"'{pwd}': {strength}")

print()

# =============================================================================
# 練習 10：綜合挑戰 🎯
# =============================================================================

print("=" * 50)
print("✅ 練習 10：綜合挑戰")
print("=" * 50)

sentence = "  Python is AWESOME and python is FUN!  "

# 處理流程
result = sentence.strip()            # 1. 移除首尾空白
result = result.lower()              # 2. 全部轉成小寫
result = result.replace("python", "資訊科技")  # 3. 取代
result = result.replace("awesome", "有趣")     # 4. 取代
result = result.replace("fun", "好玩")          # 5. 取代

print(f"處理前：'{sentence}'")
print(f"處理後：'{result}'")
# 預期輸出：'資訊科技是有趣的而且資訊科技是好玩的！'

print()

print("=" * 50)
print("🎉 恭喜完成所有練習！")
print("=" * 50)
