---
marp: true
---

# Fastcampus Web Programming SCHOOL

## Python

---

<!--
paginate: true
theme: default
size: 16:9
footer : fastcampus 웹프로그래밍 스쿨, Wooyoung Choi, 2021
-->

## 조건문

## Conditional Statements

---

### Let's get back to the Day1

`배가 고프다!!!`
- case 1: 집이라면
	- 밥이 있다면
	- 밥이 없다면

- case 2: 밖이라면
	- 현금이 10만원 초과라면
	- 현금이 5만원 초과라면
	- 현금이 없다면

---

## If

```python
if 조건:
	실행문

if 조건1 and 조건2:
	실행문

if 조건1 or 조건2:
	실행문
if not 조건:
	실행문
```

---

## if

```python
if 현금 > 100000:
	레스토랑으로 간다
```

```python
cash = 120000
if cash > 100000:
	print("go to restaurant")
```

---

## else

```python
if 조건:
	실행문1
else:
	실행문2
```

```python
cash = 120000
if cash > 100000:
    print("go to restaurant")
else:
    print("go to cvs")
```

---

## else if

```python
if 조건1:
	실행문1
else:
	if 조건2:
		실행문2
	else:
		실행문3
```

```python
cash = 120000
if cash > 100000:
    print("go to restaurant")
else:
        if cash > 50000:
            print("go to bobjib")
        else:
            print("go to cvs")
```

---

## if in else in if in else in ..

```python
cash = 120000
if cash > 100000:
    print("go to restaurant")
else:
    if cash > 50000:
        print("go to bobjib")
    else:
        if cash > 30000:
            print("go to buffet")
        else:
            if cash > 20000:
                print("go to ramen store")
            else:
                if cash > 10000:
                    print("go to chinese restaurant")
                else:
                    print("go to cvs")
```

---

## elif

```python
if 조건1:
	실행문1
elif 조건2:
	실행문2
elif 조건3:
	실행문3
...
else:
	실행문n
```

---

### elif

```python
cash = 120000
if cash > 100000:
    print("go to restaurant")
elif cash > 50000:
    print("go to bobjib")
elif cash > 30000:
    print("go to buffet")
elif cash > 20000:
    print("go to ramen store")
elif cash > 10000:
    print("go to chinese restaurant")
else:
    print("go to cvs")
```

---

## Do it your self!

### Numguess

- 1부터 100까지 정수 중 하나를 `answer`라는 변수에 할당
- 사용자로 부터 임의의 값 하나를 받아 `guess`라는 변수에 할당
- `answer`와 `guess`를 비교하여 정답여부를 출력

---

## numguess

```python
import random


answer = random.randint(1,100)
print(answer)
```

---

## numguess

```python
username = input("Hi there, What's your name?? ")
guess = eval(input("Hi, "+ username + "guess the number: "))

if guess == answer:
	print("Correct! The answer was ", str(answer))
else:
	print("That's not what I wanted!! The answer was ", str(answer))
```

---

## numguess advanced!!

how to make it with more fun??

---

## 삼항연산자

## Ternary Operators

---
## 단항연산자

- 부호(+,-), not
	- +3
	- -0.2
	- not True

## 이항연산자

- 대부분의 연산자
	- 3 + 1
	- 2 * 3.14

---

## Ternary Operators in Python

## [Conditional Expressions](https://www.python.org/dev/peps/pep-0308/)

---

## Conditional Expressions

- `a` if `condition` else `b`
- condition == True => a
- condition == False => b

---

## Conditional Expressions in Conditional Expressions

`a` if `condition` else `b` if `condition` else `c`

```python
if condition:
	result = 'a'
else:
	if condition:
		result = 'b'
	else:
		result = 'c'
```

---

## Expression is Expression, not Statement!!

Possible
```python
if Condition:
	result = b
else:
	another_result = c
```

Impossible
```python
result = b if condition else another_result = c
```

---

## And, Conditional Expressions 는 파이썬 연산자 중 가장 낮은 순위를 가집니다. 

---

## Practice(1)

사용자가 입력한 요일('월'~'일' or '월요일'~'일요일')을
- 평일일 경우, "평일이네요ㅜㅜ"
- 주말일 경우, "주말입니다^^"
- 잘못 입력한 경우, "요일을 입력하세요"

을 출력하도록 Conditional Statements 와 Conditional Expressions로 각각 구현하세요

---

## For, while

```python
for 변수 in (리스트 or 문자열):
	실행문1
    ...
```
```python
for i in ["python", "java", "golang"]:
	print(i)
```

---

## For, while

```python
sum = 0
for i in range(1,11):
	sum += i
    sum = sum + i
	print(sum)
```

---

## For, while

```python
while 조건:
	실행문1
	...
```

```python
while name != "foo bar":
	name = input("What's your name? ")
	print("Hi, " + name + "So, where is foo bar?")
```

```python
while 1:
	print("Hello world!")
```

---

## Practice(2)

다음 문제를 해결하세요.

1. 사용자가 입력한 임의의 정수(2~100)에 대해 팩토리얼 연산을 수행하세요.

2. 다음 2차원 list에 대해 각 요소의 합을 구하세요.

```python
[
	[1, 0, 7, 0],
	[0, 2, 0, 9],
	[0, 6, 3, 7],
	[4, 0, 5, 1],
]
```

---

## Dictionary with Iterations

---

### get word list

```python
a_words = []
with open('./a_word_list.txt') as f:
	textlines = f.readlines()
	for item in textlines:
	a_words.append(item.replace('\n',''))
```

---

### 길이별 단어 수 구하기

```python
len_count = {}
for i in map(len, a_words):
	if i in len_count:
		len_count[i] += 1
	else:
		len_count[i] = 1
```

---

### 길이별 단어 수 구하기 with get

```python
len_count = {}
for i in map(len, a_words):
	len_count[i] = len_count.get(i,0) + 1
```

---

### 길이별 단어 분류하기

```python
a_word_by_len = {}
for word in a_words:
	a_word_by_len.setdefault(len(word),[]).append(word)
```

---

## Iterations with Conditional Statements

---

## Fizzbuzz

1부터 100까지 **반복하면서,**

3의 배수 = "Fizz"
5의 배수 = "Buzz"
15의 배수 = "FizzBuzz"
나머지 = 그 숫자

---

## Fizzbuzz

```python
num = eval(input("type the number: "))

for i in range(1, num + 1):
	if i % 15 == 0:
		print("fizzbuzz")
	elif i % 3 == 0:
		print("fizz")
	elif i % 5 == 0:
		print("buzz")
	else:
		print(i)
```

---

## Refactoring numguess

```python
import random


answer = random.randint(1,100)
username = input("Hi there, What's your name?? ")

while True:
	guess = eval(input("Hi "+ username + ", guess the number: "))

	if guess == answer:
		print("Correct! The answer was ", str(answer))
		break
	else:
		print("That's not what I wanted!! Try again!!")
```

---

## give a hint!!

```python
import random


answer = random.randint(1,100)
username = input("Hi there, What's your name?? ")

while True:
    guess = eval(input("Hi, "+ username + "guess the number: "))

    if guess == answer:
        print("Correct! The answer was ", str(answer))
        break
    elif guess > answer:
        print("Too high!! Try again!!")
    elif guess < answer:
        print("Too Low!! Try again!!")
```

---

## limit trial

```python
import random


answer = random.randint(1,100)
username = input("Hi there, What's your name?? ")
trial = 5
while trial:
    guess = eval(input("Hi, "+ username + ". guess the number: "))

    if guess == answer:
        print("Correct! The answer was ", str(answer))
        break
    elif guess > answer:
        trial -= 1
        print("Too high!! Try again!!(%d times left)" % (trial))
    elif guess < answer:
        trial -= 1
        print("Too Low!! Try again!!(%d times left)" % (trial))
        
if trial == 0:
    print("You are Wrong! The answer was ", str(answer))
```

---

## Monty Hall Problem

---

![](https://i.ytimg.com/vi/rn1y-HrmA5c/maxresdefault.jpg)

<link href="https://fonts.googleapis.com/css?family=Nanum+Gothic:400,800" rel="stylesheet">
<link rel='stylesheet' href='//cdn.jsdelivr.net/npm/hack-font@3.3.0/build/web/hack-subset.css'>

<style>
h1,h2,h3,h4,h5,h6,
p,li, dd {
font-family: 'Nanum Gothic', Gothic;
}
span, pre {
font-family: Hack, monospace;
}
</style>