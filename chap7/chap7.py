# /usr/bin/env python
# -*- coding:utf-8 -*-

### 辞書とは
x = []
y = {}

y[0] = 'Hello'
y[1] = 'Goodbye'

print(y[0])
print(y[1]+ ", Friend.")

y["two"] = 2
y["pi"] = 3.14
print(y["two"] * y["pi"])

english_to_french = {}
english_to_french['red']= 'rouge'
english_to_french['blue'] = 'bleu'
english_to_french['green'] = 'vert'
print("red is", english_to_french['red'])

## その他の辞書の操作
english_to_french = {'red': 'rouge', 'blue': 'bleu', 'green':'vert'}
print(len(english_to_french))

print(list(english_to_french.keys()))

print(list(english_to_french.values()))

print('red' in english_to_french) # キーが存在するかどうか確認する
print('orange' in english_to_french)

print(english_to_french.get('blue', 'No translation'))
print(english_to_french.get('chartreuse', 'No translation'))

print(english_to_french.setdefault('chartreuse', 'No translation'))

x = {0: 'zero', 1:'one'}

y = x.copy()                    # シャローコピー
print(y)

z = {1: 'One', 2: 'Two'}
x = {0: 'Zero', 1: 'One'}

x.update(z)                     # 最初の辞書を2つめの辞書のすべてのキーと値で更新する
print(x)

## 単語数のカウント
sample_string = "To be or not to be"

occurences = {}

for word in sample_string.split():
    occurences[word] = occurences.get(word, 0) + 1

for word in occurences:
    print("The word", word, "occurs", occurences[word], "times in the string")

## キーに使えるもの
print((1, 2).__hash__())
print((2, 3).__hash__())

## 疎行列
matrix = [[3, 0, -2, 11],
          [0, 9, 0, 0], 
          [0, 7, 0, 0],
          [0, 0, 0, -5]]

matrix = {(0,0): 3, (0, 2): -2, (0,3): 11,
          (1,1): 9,
          (2,1): 7,
          (3, 3): -5 }

def access_matrix(rownum, colnum):
    if (rownum, colnum) in matrix:
        element = matrix[(rownum, colnum)]
    else:
        element = 0
    return element
    
def access_matrix2(rownum, colnum):
    element = matrix.get((rownum, colnum), 0)
    return element

## 辞書をキャッシュとして使う
