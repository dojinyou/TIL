def quiz1(nums):
	return nums[:-1]
def quiz2(nums):
	nums.insert(2, 100)
	return nums
def quiz3(num):
	result = ""
	for i in range(num):
		result += (" "*(num - 1 - i))+("*"*(2*i+1))+"\n"
	return result[:-1]
def quiz4(nums):
	nums.sort()
	count = 0
	prev = None
	rank = 0
	while len(nums) > 0:
		now = nums.pop()
		if now != prev :
			rank += 1
			if rank > 3 :
				break
		count += 1
		prev = now
	return count
def quiz5(limit, num, weights):
	weights.reverse()
	sum_weight = 0
	count = 0
	while len(weights) != 0:
		if sum_weight + weights[-1] > limit:
			break
		sum_weight += weights.pop()
		count += 1
	return count
# -----------------------------------------------------------
# 아래 코드는 테스트용입니다 건들지마세요.
import quiz_test as qt
if __name__ == "__main__":
	qt.test([quiz1,quiz2,quiz3,quiz4])
	qt.__test(quiz5)