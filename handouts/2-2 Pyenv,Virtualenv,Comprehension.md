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

## How to start python project with virtual environment

---

## Python Version Manager - Pyenv

- 사용자에 따라 다른 python version 사용
- 프로젝트에 따라 다른 python version 사용
- 간단한 커맨드로 python version 변경 가능

---

## Install pyenv

https://github.com/pyenv/pyenv#installation

- For MacOS

```shell
$ brew update
$ brew install pyenv
```

- For other OS with bash
`$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
`
```shell
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
```

- For windows
https://github.com/pyenv-win/pyenv-win#installation

---

## Pyenv Virtualenv

- 설정된 python version에 따른 독립적인 라이브러리 사용

```text
ex)
python3.8
	- django 1.11
	- requests 2.0
python3.9.1
	- django 2.0
	- requests 1.9.1
```

---

### Install pyenv-virtualenv

- For Unix-like OS(Ubuntu, MacOS)

https://github.com/pyenv/pyenv-virtualenv#installation

- For Windows(Don't recommand)

https://thinkdiff.net/python/how-to-install-python-virtualenv-in-windows/

https://jackmckew.dev/managing-virtual-environments-on-windows.html

---

## List Comprehension

존재하는 리스트를 활용하여 새로운 리스트를 생성하는 방법

비슷한 표현들

- Set Comprehension
- Dictionary Comprehension
- Parallel list Comprehension

---

## List Comprehension

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	doubled_list.append(i * 2)
```

---

## List Comprehension

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	doubled_list.append(i * 2)
```

```python
doubled_list = []
```

---

## List Comprehension

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	doubled_list.append(i * 2)
```

```python
doubled_list = [i * 2]
```

---

## List Comprehension

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	doubled_list.append(i * 2)
```

```python
doubled_list = [i * 2 for i in old_list]
```

---

## List Comprehension - another example

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	if i % 2 == 0:
		doubled_list.append(i * 2)
```

---

## List Comprehension - another example

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	if i % 2 == 0:
		doubled_list.append(i * 2)
```

```python
doubled_list = []
```

---

## List Comprehension - another example

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	if i % 2 == 0:
		doubled_list.append(i * 2)
```

```python
doubled_list = [i * 2]
```

---

## List Comprehension - another example

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	if i % 2 == 0:
		doubled_list.append(i * 2)
```

```python
doubled_list = [i * 2 for i in old_list]
```

---

## List Comprehension - another example

```python
old_list = [1, 2, 3, 4, 5,]

doubled_list = []
for i in old_list:
	if i % 2 == 0:
		doubled_list.append(i * 2)
```

```python
doubled_list = [i * 2 for i in old_list if i % 2 == 0]
```

---

## Do it yourself!

- List comprehension 으로 FizzBuzz 한줄로 구현하기

---
`["Fizz"*(not i%3) + "Buzz"*(not i%5) or i for i in range(1,100)]`

---

## Practice(1)



---

## Dictionary Comprehensions

---

## Dictionary Comprehensions

- 기존의 딕셔너리를 활용해 새로운 딕셔너리를 만들고 싶을때

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    new_dict[k]=v*2
```

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    new_dict[k]=v*2
```

```python
new_dict = {}
```

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    new_dict[k]=v*2
```

```python
new_dict = {k:v*2} #new_dict[k]=v*2
```

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    new_dict[k]=v*2
```

```python
new_dict = {k:v*2 for k,v in old_dict.items()}
```

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    if v%2!=0:
        new_dict[k*2]=v*3
```

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    if v%2!=0:
        new_dict[k*2]=v*3
```

```python
new_dict = {}
```

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    if v%2!=0:
        new_dict[k*2]=v*3
```

```python
new_dict = {k*2:v*3} #new_dict[k*2]=v*3
```

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    if v%2!=0:
        new_dict[k*2]=v*3
```

```python
new_dict = {k*2:v*3 for k,v in old_dict.items()}
```

---

## Dictionary Comprehensions

```python
old_dict = {1:1,2:2,3:3,4:4,}
new_dict = {}
for k,v in old_dict.items():
    if v%2!=0:
        new_dict[k*2]=v*3
```

```python
new_dict = {k*2:v*3 for k,v in old_dict.items() if v%2!=0}
```

---

## Practice(2)

다음 dictionary에 대해 dictionary comprehension을 수행하여 각 key에 들어있는 모든 value의 길이로 대체된 dictionary를 만드세요.

```python
old_words = {
	
}
```

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