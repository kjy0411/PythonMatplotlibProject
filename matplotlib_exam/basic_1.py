import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
# re => 정규식

text="Hello Python 3 Matplotlib 100."
numbers=re.findall(r'\d+',text)
# \d+ => 숫자 1개 이상
# 패턴은 반드시 r'패턴'
# 댓글 , 내용 , 뉴스 => 필요한 데이터 추출 => 정규식
# 데이터의 형식을 지정
print(numbers)
#   패턴 = 자바, 자바스크립트, 파이썬 동일
#   . : 모든 문자 한개 (임의의 문자)
#   \d 숫자(0,9) => 1개 => 123 >> '1','2','3'
#                   \d+ => 123 >> '123'
#       +(한개 이상), *(0개 이상)
#   \D 숫자가 아닌 문자
#   \w 알파벳 / 숫자 / 밑줄
#   \W \w가 아닌 문자 찾기 => hello@123 >> '@'
#   \s 공백문자 a b >> ' '
#   \S 공백이 아닌 문자 a b >> 'a','b'
#   ^ : 문자열 시작 apply >> 'a'
#   $ : 문자열 끝 apply >> 'y'
#   [abc] => a,b,c중 하나 => a|b|c
#   [a-z] => 소문자 알파벳
#   [A-Z] => 대문자 알파벳
#   [0-9] => 숫자
#   [^abc] => a,b,c 제외 a1b2 >> '1','2'
#   (abc) => 그룹 (abc)+
#   * 0이상
#   + 1이상
#   {n} n개 이상   [0-9]{3} 123 12 111 23 => '123','111'
#   {n,} 최소 n개 이상
#   {n,m} n개 이상 m개 이하
#
#   => match => re.match(pattern,str)
#                        패턴과 일치
#   => findall => re.findall(pattern,str)
#   => sub => 패턴과 일치할 때 원하는 부분만 replace
#      re.sub(pattern,replace,str)
#      ------ index
text="123"
n=re.findall(r'\d',text)
print(n)
text="hello_123"
n=re.findall(r'\D',text)
# findall => list
print(n)
n=re.findall(r'\w',text)
# 문자 / 숫자 / 밑줄
print(n)
text="hello@123"
n=re.findall(r'\W',text)
print(n)
text="a b"
n=re.findall(r'\s',text)
print(n)
n=re.findall(r'\S',text)
print(n)
text="apple bbb aaa ddd abc abbb"
n=re.findall(r'(abc)+',text)
print(n)