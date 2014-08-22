# /usr/bin/env python
# -*- coding:utf-8 -*-

### Whileループ
## break文とcontinue文
# breakで抜けた場合は、elseは実行されない

### if-elif-else文
x = 0

if x < 5:
    pass
else:
    x = 5

# case文はない

### forループ
# forループのelse, continue, breakはwhileのそれと同じように機能する

x = [1.0, 2.0, 3.0]
for n in x:
    print(1 / n)

## range関数
x = [1, 3, -7, 4, 9, -5, 4]
for i in range(len(x)):
    if x[i] < 0:
        print("Found a negative number at index ", i)

print(list(range(3, 7)))
print(list(range(2, 10)))

print(list(range(5, 3)))        # カウントは逆方向には進まない

print(list(range(0, 10, 2)))    # 2でカウント
print(list(range(5, 0, -1)))    # 負方向にカウント


somelist = [(1, 2), (3, 7), (9, 5)]
result = 0
for x,y in somelist:
    result = result + x * y
print(result)

## enumerate関数
x = [1, 3, -7, 4, 9, -5, 4]
for i, n in enumerate(x):
    if n < 0:
        print("Found a negative number at index ", i)

## zip関数
x = [1, 2, 3, 4]
y = ['a', 'b', 'c']
z = zip(x, y)
print(z)                        # zはzip objectになる(generator?)
print(list(z))                  # 短い方にあわせる

### リストと辞書の内包表示
x = [1, 2, 3, 4]
x_squared = []
for item in x:
    x_squared.append(item*item)
    
print(x_squared)

x = [1,2,3,4]
x_squared = [item * item for item in x]
print(x_squared)

x_squared = [item * item for item in x if item > 2]
print(x_squared)

x_squared_dict = {item: item * item for item in x }
print(x_squared_dict)

### 文、ブロック、インデント
x = 1; y = 0; z = 0
if x > 0: y = 1; z = 10
else: y = -1

print(x, y, z)

print('string1', 'string2', 'string3'\
      'string4', 'string5')

x = 100 + 200 + 300 \
    + 400 + 500

v = [100, 200, 300, 400, 500,
     600, 700, 800, 900]

max(1000, 300, 500,
    800, 1200)

x = (100 + 200 + 300
     + 400 + 500)


x = "string seperated by whitespace" \
    """are automatically""" ' concatenated'
print(x)

x = 1
if x > 0:
    string1 = "this string broken by a backslash will end up\
              with the indentation tabs in it"

print(string1)

if x > 0:
    string1 = "this can be easily avoided by splittng the "\
              "string in this way"

print(string1)

### ブール値とブール式
print([2] and [3, 4])
print([] and 5)
print([2] or [3, 4])
print([] or 5)

x = [0]
y = [x, 1]
print(x is y[0])                       # 同じオブジェクトかどうかを確認

x = [0]
print(x is y[0])                       # 違うオブジェクト

print(x == y[0])                # 等値性の判定

## テキストファイルを分析する簡単なプログラムの記述
# word_count.py



