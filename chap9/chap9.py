# /usr/bin/env python
# -*- coding:utf-8 -*-

### 関数定義の基礎
def fact(n):
    """Return the factrial of the given number."""
    r = 1
    while n > 0:
        r *= n
        n -= 1
    return r

print(fact.__doc__)             # __doc__で関数の説明が見れる

print(fact(4))
x = fact(4)
print(x)

### 関数パラメータの種類
def power(x, y):
    r = 1
    while y > 0:
        r = r * x
        y = y - 1
    return r

print(power(3, 3))              # 位置によって指定
# power(3) 部分適用はできない

fun = lambda x, y: x * y
print(fun(3, 2))

def power(x, y=2):
    r = 1
    while y > 0:
        r = r * x
        y = y - 1
    return r

print(power(3, 3))
print(power(3))

print(power(2, 3))
print(power(3, 2))
print(power(y=2, x=3))          # キーワード渡し

## 可変個の引数
def maximum(*numbers):
    if len(numbers) == 0 :
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum :
                maxnum = n
        return maxnum

print(maximum(3, 2, 8))
print(maximum(1, 5, 9, -2, 2))

## 可変個のキーワード引数
def example_fun(x, y, **other):
    print("x: {0}, y: {1}, keys in 'other': {2}".format(x, y, list(other.keys())))
    other_total = 0
    for k in other.keys():
        other_total = other_total + other[k]

    print ("The total of value in 'other' is {0}".format(other_total))

example_fun(2, y="1", foo=3, bar=4)

### ミュータブルなオブジェクトを引数とする
def f(n, list1, list2):
    list1.append(3)
    list2 = [4, 5, 6]
    n = n +1

x = 5
y = [1, 2]
z = [4, 5]
f(x, y , z)
print(x, y ,z)                  # y 値が変っている

### ローカル変数、ノンローカル変数、グローバル変数
def fun():
    global a
    a = 1
    b = 2

a = "one"
b = "two"
fun()
print(a, b)                     # aはグローバルなので値が変わる


