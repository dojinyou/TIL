# 문제 1
testcase_quiz1 = [
	[[1,2,3,4,5], [1,2,3,4]],
	[[1,2,3], [1,2]],
	[[1], []]
]
testcase_quiz2 = [
	[[1,2,3,4,5], [1,2,100,3,4,5]],
	[[1,2,3], [1,2,100,3]],
	[[1,0], [1,0,100]]
]
testcase_quiz3 = [
	[0, ""],
	[1, "*"],
	[5, "    *\n   ***\n  *****\n *******\n*********"]
]
testcase_quiz4 = [
	[[1,2,3,4,5], 3], # 정상적인 케이스 
	[[1,2,3,4,5,5,5], 5], # 중복이 있는 케이스 
	[[1,2,3,3,4,5,5,5], 6], # 중복이 있는 케이스 
	[[1,2], 2], # 3등까지 없는 케이스
	[[1,1,1,2,2], 5] # 3등까지 없는 케이스 중복
]
testcase_quiz5 = [
	[[200, 5, [80,70,50,60,75]], 3], # 정상적인 케이스 
	[[200, 5, [80,90,50,60,75]], 2], # 정상적인 케이스 무게 부족 
	[[200, 3, [50,50,50]], 3], # 사람 부족 
	[[200, 0, []], 0], # 사람이 없는 경우
	[[50, 5, [80,70,50,60,75]], 0], # 한명도 못 태우는 경우
]
testcases = [
	testcase_quiz1, 
	testcase_quiz2, 
	testcase_quiz3, 
	testcase_quiz4
	]
def test(quiz):
	print("------test-------")
	for i, testcase in enumerate(testcases):
		print(f"quiz{i+1}")
		col = True
		for j, (argument, answer) in enumerate(testcase):
			if quiz[i](argument) == answer:
				result = "pass"
			else:
				result = "Non pass"
				col = False
			print(f"testcase{j+1} : {result}")
		print("----------------")

def __test(quiz):
	print("quiz5")
	for j, (argument, answer) in enumerate(testcase_quiz5):
		if quiz(argument[0],argument[1],argument[2]) == answer:
			result = "pass"
		else:
			result = "Non pass"
			col = False
		print(f"testcase{j+1} : {result}")
	print("----------------")