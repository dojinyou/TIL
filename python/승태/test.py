# 수정했습니다.
def searchDic(s) :
	lst = []
	rt_lst = []
	temp = 0

	# 코드 수정
	# 원본 코드
	# for i in dic_Han.keys() :
	#     lst.append(i)
	#     lst.append(dic_Han.get(i))
	# for i in dic_Eg.keys() :
	#     lst.append(i)
	#     lst.append(dic_Eg.get(i))
	# 수정코드
	for key, value in dic_Han.items() :
		lst.extend([key,value]) 
	for key, value in dic_Eg.items() :
		lst.extend([key,value]) 
	# 일단 dict는 데이터 뽑는 방법 3가지
	# 1. key만 뽑기 -> dict, dict.keys()
	# 2. value만 뽑기 -> dict.values()
	# 3. key, value 둘 다 뽑기 -> dict.items()
	# list.append는 element 추가하는 거
	# list.extend는 다른 리스트를 붙이는 거
	# 코드수정
	# 원본코드
	# for i in lst :
	#     if s in lst[temp] :
	#         if temp % 2 == 0 :
	#             pass
	#         else :
	#             rt_lst.append(lst[temp-1])
	#     temp += 1
	# 수정코드
	for i in range(1,len(lst),2):
		if s in lst[i]:
			rt_lst.append(lst[i-1])

	return rt_lst

dic_Han = {}
dic_Eg = {}
for i in range(int(input("Input number of programming languages : "))) : 
	Han_key = input("프로그래밍 언어 이름 : ")
	Han_value = input("프로그래밍 언어 설명 : ")
	dic_Han[Han_key] = Han_value

print("==영어사전 생성==")
for key in dic_Han :
	print(f"discription : {key}")
	Eg_key = input("Input the name of the language in English : ")
	Eg_value = input("Input the discription of the language in English : ")
	dic_Eg[Eg_key] = Eg_value

while 1 : 
	search = input("Enter a word for search : ")
	s = searchDic(search)
	if len(s) :
			print(f"search result : {s}")
	else :
			print("No match! break!")
			break