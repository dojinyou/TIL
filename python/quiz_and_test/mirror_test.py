testcase = [
	[1, [0,1]],
	[8, [0,1,8]],
	[10, [0,1,8]],
	[87, [0, 1, 8, 11, 69]],
	[100, [0, 1, 8, 11, 69, 88, 96]]
]
def test(func):
	print("mirror")
	for i, (argument, answer) in enumerate(testcase):
		if func(argument) == answer:
			result = "pass"
		else:
			result = "Non pass"
			col = False
		print(f"testcase{i+1} : {result}")