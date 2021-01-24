# https://www.acmicpc.net/problem/10820

from sys import stdin
import re

while True :
	try :
		text = stdin.readline()	
		countArray = []
		countArray.append(len(re.findall(r'[a-z]',text)))
		countArray.append(len(re.findall(r'[A-Z]',text)))
		countArray.append(len(re.findall(r'[\d]',text)))
		countArray.append(len(re.findall(r'[" "]',text)))
		print(" ".join(map(str,countArray)))
	except :
		break

import sys 
while True: 
	text = sys.stdin.readline().rstrip('\n') 
	if not text :
		break
	countArray = []
	countArray.append(len(re.findall(r'[a-z]',text)))
	countArray.append(len(re.findall(r'[A-Z]',text)))
	countArray.append(len(re.findall(r'[\d]',text)))
	countArray.append(len(re.findall(r'[" "]',text)))
	print(" ".join(map(str,countArray)))


	import sys

# while True:
#     line = sys.stdin.readline().rstrip('\n')

#     if not line:
#         break

#     # 소문자, 대문자, 숫자, 공백
#     l, u, d, s = 0, 0, 0, 0
#     for each in line:
#         if each.islower():
#             l += 1
#         elif each.isupper():
#             u += 1
#         elif each.isdigit():
#             d += 1
#         elif each.isspace():
#             s += 1

#     print(l, u, d, s)