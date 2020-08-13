def next_number(num):
	str_num = str(num)
	for i in range(len(str_num)-2,-1,-1):
		if str_num[i] >= str_num[i+1]:
			continue
		text = ''.join(sorted(str_num[i:]))
		idx = text.rindex(str_num[i]) + 1
		result = ''.join((str_num[:i],text[idx],text[:idx],text[idx+1:]))
		return int(result)
	return -1

# -----------------------------------------------------------
# 아래 코드는 테스트용입니다 건들지마세요.
import next_number_test as nnt
if __name__ == "__main__":
	nnt.test(next_number)