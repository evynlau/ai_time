"""
📚 Day 14：字串運算 —— 字元的藝術 🎨
===============================
在程式的世界裡，文字是至關重要的存在！
今天我們要學習 Python 中處理字串的各種強大技巧。🔤

字串（String）是用引號包起來的文字序列，
在 Python 中可以用單引號 ' 或雙引號 " 來建立。

讓我們一起探索字串的奧秘吧！✨
"""

# =============================================================================
# 第一章：字串的基本建立 📝
# =============================================================================

print("=" * 60)
print("🌟 第一章：字串的基本建立")
print("=" * 60)

# 使用單引號建立字串
name1 = '小明的世界'
print(f"單引號建立：{name1}")

# 使用雙引號建立字串
name2 = "Python 是我的最愛"
print(f"雙引號建立：{name2}")

# 使用三引號建立多行字串
poem = """賞花歸去馬如飛，
立馬踟躕�。
去時雪如絲，
歸時雪滿地。"""
print("多行字串：")
print(poem)

# 使用反斜線轉義特殊字元
quote = '她說："今天天氣真好！"'
print(f"轉義字元：{quote}")

print()

# =============================================================================
# 第二章：字串索引 —— 找到特定字元 🔍
# =============================================================================

print("=" * 60)
print("🔍 第二章：字串索引")
print("=" * 60)

text = "Hello, Python!"

# 正向索引：從 0 開始
print(f"字串：'{text}'")
print(f"第 0 個字元（第一個）：{text[0]}")
print(f"第 1 個字元（第二個）：{text[1]}")
print(f"第 2 個字元（第三個）：{text[2]}")

# 反向索引：從 -1 開始（最後一個）
print(f"倒數第一個字元：{text[-1]}")
print(f"倒數第二個字元：{text[-2]}")
print(f"倒數第三個字元：{text[-3]}")

# 使用 len() 取得字串長度
print(f"字串長度：{len(text)}")

# 取得最後一個字元（安全方法）
last_char = text[len(text) - 1]
print(f"最後一個字元（安全方法）：{last_char}")

print()

# =============================================================================
# 第三章：字串切片 —— 取得子字串 ✂️
# =============================================================================

print("=" * 60)
print("✂️ 第三章：字串切片")
print("=" * 60)

text = "Hello, Python!"

print(f"原始字串：'{text}'")
print(f"長度：{len(text)}")

# 基本切片 [起始:結束]（不包括結束位置）
print(f"text[0:5] = '{text[0:5]}'")   # Hello
print(f"text[7:13] = '{text[7:13]}'") # Python

# 省略起始值（從頭開始）
print(f"text[:5] = '{text[:5]}'")     # Hello

# 省略結束值（到末尾為止）
print(f"text[7:] = '{text[7:]}'")     # Python!

# 負數索引切片
print(f"text[-6:] = '{text[-6:]}'")   # Python
print(f"text[:-7] = '{text[:-7]}'")  # Hello,

# 切片加步進值 [起始:結束:步進]
numbers = "0123456789"
print(f"數字字串：'{numbers}'")
print(f"numbers[::2] = '{numbers[::2]}'")  # 取得偶數位：02468
print(f"numbers[1::2] = '{numbers[1::2]}'") # 取得奇數位：13579
print(f"numbers[::-1] = '{numbers[::-1]}'") # 反轉：9876543210

# 實用範例：取出副檔名
filename = "photo.jpg"
extension = filename[-3:]
print(f"檔案 '{filename}' 的副檔名：{extension}")

print()

# =============================================================================
# 第四章：字串連接 —— 組合文字 🔗
# =============================================================================

print("=" * 60)
print("🔗 第四章：字串連接")
print("=" * 60)

# 使用 + 運算子連接字串
greeting = "你好" + "，" + "世界"
print(f"'你好' + '，' + '世界' = '{greeting}'")

# 使用 * 重複字串
divider = "=" * 30
print(f"'=' * 30 = '{divider}'")

heart = "❤️" * 5
print(f"'❤️' * 5 = '{heart}'")

# 使用 join() 方法連接多個字串（更推薦）
words = ["Python", "is", "awesome"]
space_joined = " ".join(words)
print(f"' '.join(['Python', 'is', 'awesome']) = '{space_joined}'")

dash_joined = "-".join(words)
print(f"'-'.join(['Python', 'is', 'awesome']) = '{dash_joined}'")

# 使用 f-string 格式化（現代方法，强烈推薦✨）
name = "小美"
age = 12
city = "台北"
intro = f"我是{name}，今年{age}歲，住在美麗的{city}！"
print(f"f-string 格式化：{intro}")

# 複雜的 f-string 運算
a = 10
b = 20
result = f"{a} + {b} = {a + b}"
print(f"f-string 運算：{result}")

print()

# =============================================================================
# 第五章：常用字串方法 🔧
# =============================================================================

print("=" * 60)
print("🔧 第五章：常用字串方法")
print("=" * 60)

text = "  Hello, Python! 你好 Python!  "

print(f"原始字串：'{text}'")
print(f"長度：{len(text)}")

# strip() - 移除首尾空白
cleaned = text.strip()
print(f"strip() 移除首尾空白：'{cleaned}'")

# lstrip() - 移除左側空白
left_stripped = text.lstrip()
print(f"lstrip() 移除左側空白：'{left_stripped}'")

# rstrip() - 移除右側空白
right_stripped = text.rstrip()
print(f"rstrip() 移除右側空白：'{right_stripped}'")

print()

# 大小寫轉換
msg = "Hello World"

upper_msg = msg.upper()
print(f"'{msg}'.upper() = '{upper_msg}'")

lower_msg = msg.lower()
print(f"'{msg}'.lower() = '{lower_msg}'")

capitalize_msg = msg.capitalize()
print(f"'{msg}'.capitalize() = '{capitalize_msg}'")

title_msg = msg.title()
print(f"'{msg}'.title() = '{title_msg}'")

print()

# =============================================================================
# 第六章：取代與分割 🔄
# =============================================================================

print("=" * 60)
print("🔄 第六章：取代與分割")
print("=" * 60)

# replace() - 取代字串
sentence = "I love Python, Python is great!"
new_sentence = sentence.replace("Python", "Programming")
print(f"取代前：{sentence}")
print(f"取代後：{new_sentence}")

# 可以指定取代次數
limited_replace = sentence.replace("Python", "Code", 1)
print(f"只取代第一次：{limited_replace}")

print()

# split() - 分割字串
fruits = "蘋果,香蕉,橘子,葡萄,草莓"
fruit_list = fruits.split(",")
print(f"原始字串：'{fruits}'")
print(f"split(',') 分割結果：{fruit_list}")

# 使用空白分割
sentence = "今天 天氣 很好"
words = sentence.split(" ")
print(f"'{sentence}'.split(' ') = {words}")

# 限定分割次數
data = "a,b,c,d,e"
limited_split = data.split(",", 2)
print(f"'{data}'.split(',', 2) = {limited_split}")

# partition() - 分割為三部分
url = "http://www.example.com"
protocol, sep, rest = url.partition("://")
print(f"url.partition('://') = ({protocol}, {sep}, {rest})")

print()

# =============================================================================
# 第七章：成員測試 —— in 和 not in 🔎
# =============================================================================

print("=" * 60)
print("🔎 第七章：成員測試")
print("=" * 60)

email = "student@school.edu.tw"

# 使用 in 測試是否包含
print(f"測試字串：'{email}'")
print(f"'@' in email = {'@' in email}")
print(f"'.' in email = {'.' in email}")
print(f"'python' in email = {'python' in email}")  # 注意大小寫

# 使用 not in 測試是否不包含
print(f"'#' not in email = {'#' not in email}")
print(f"'.edu' not in email = {'edu' not in email}")

print()

# 實用範例：檢查輸入
password = "Pass1234"

has_digit = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)

print(f"密碼 '{password}' 強度檢查：")
print(f"  包含數字：{has_digit} ✅" if has_digit else f"  包含數字：{has_digit} ❌")
print(f"  包含大寫：{has_upper} ✅" if has_upper else f"  包含大寫：{has_upper} ❌")
print(f"  包含小寫：{has_lower} ✅" if has_lower else f"  包含小寫：{has_lower} ❌")

print()

# =============================================================================
# 第八章：字串格式化進階 🎯
# =============================================================================

print("=" * 60)
print("🎯 第八章：字串格式化進階")
print("=" * 60)

# f-string 進階用法
name = "小明"
scores = {"數學": 95, "英文": 88, "自然": 92}

# 在 f-string 中使用字典
print(f"姓名：{name}")
print(f"數學成績：{scores['數學']}")

# f-string 中進行運算
a, b = 15, 8
print(f"{a} × {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # 保留兩位小數

# format() 方法（較舊但仍常用）
template = "我叫 {}，今年 {} 歲，在 {} 讀書。"
result = template.format("小華", 13, "國中二年級")
print(f"format() 方法：{result}")

# 使用索引
template2 = "{0} 最喜歡的科目是 {1}，因為 {2}。"
result2 = template2.format("小美", "資訊科技", "很有趣")
print(f"format() with indices：{result2}")

# 使用命名參數
template3 = "{name} 的生日是 {birthday}。"
result3 = template3.format(name="小李", birthday="2008-03-15")
print(f"format() with names：{result3}")

print()

# =============================================================================
# 第九章：常見應用情境 💡
# =============================================================================

print("=" * 60)
print("💡 第九章：常見應用情境")
print("=" * 60)

# 情境 1：處理使用者輸入
username = input("請輸入使用者名稱：").strip()
if username:
    print(f"歡迎，{username}！🎉")
else:
    print("使用者名稱不能為空！")

print()

# 情境 2：清理手機號碼
phone = "  +886-912-345-678  "
clean_phone = phone.strip().replace(" ", "").replace("-", "")
print(f"原始號碼：'{phone}'}")
print(f"清理後：'{clean_phone}'}")

print()

# 情境 3：產生格式化列表
items = ["鉛筆", "橡皮擦", "尺", "剪刀"]
print("📋 我的文具清單：")
for i, item in enumerate(items, 1):
    print(f"  {i}. {item}")

print()

# 情境 4：檢查是否為有效檔案名稱
def is_valid_filename(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    return not any(char in filename for char in invalid_chars)

test_names = ["report.txt", "data<1>.csv", "notes:2024.docx", "photo.jpg"]
for name in test_names:
    status = "✅ 有效" if is_valid_filename(name) else "❌ 無效"
    print(f"'{name}' - {status}")

print()

# =============================================================================
# 第十章：實用技巧與注意事項 ⚠️
# =============================================================================

print("=" * 60)
print("⚠️ 第十章：實用技巧與注意事項")
print("=" * 60)

# 注意 1：字串是不可變的（Immutable）
original = "Hello"
# original[0] = "J"  # 這會報錯！
# 正確做法是建立新字串
modified = "J" + original[1:]
print(f"修改字串：'{original}' → '{modified}'")

# 注意 2：小心空白字元
text1 = "abc"
text2 = "abc "
print(f"'{text1}' == '{text2}' → {text1 == text2}")
print(f"'{text1}' == '{text2}'.strip() → {text1 == text2.strip()}")

# 注意 3：處理中文字串
chinese = "你好，世界！🌏"
print(f"中文字串：'{chinese}'")
print(f"長度（字元數）：{len(chinese)}")
# 注意：中英文混合時，len() 會正確計算字元數

# 注意 4：避免常見錯誤
# 錯誤：混用引號導致語法錯誤
# correct = 'It's fine'  # 錯誤！
correct = "It's fine"  # 正確
print(f"正確的引號使用：{correct}")

print()

# =============================================================================
# 總結 🎊
# =============================================================================

print("=" * 60)
print("🎊 今天學到的知識點總結")
print("=" * 60)
print("""
✅ 字串索引：使用 [位置] 取得特定字元
✅ 字串切片：使用 [起始:結束:步進] 取得子字串
✅ 字串連接：使用 + 或 join() 或 f-string
✅ 大小寫：upper(), lower(), capitalize(), title()
✅ 清理：strip(), lstrip(), rstrip()
✅ 取代：replace()
✅ 分割：split(), partition()
✅ 成員測試：in, not in
✅ 格式化：f-string, format()

💪 勤加練習，你就能熟練掌握字串運算！
""")

print("=" * 60)
print("🌟 Day 14 課程完成！繼續加油！")
print("=" * 60)
