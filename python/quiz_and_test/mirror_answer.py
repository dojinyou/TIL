def mirror(num):
	def is_mirror(n):
		str_n = str(n)
		length = len(str_n)
		if length%2 == 1 :
			if str_n[length//2] not in ["0","1","8"]:
				return False
		for i in range(length//2):
			if str_n[i] in ["0","1","8"] and str_n[i] == str_n[length -1 - i]:
				continue
			if str_n[i] == "6" and str_n[length -1 - i] == "9":
				continue
			if str_n[i] == "9" and str_n[length -1 - i] == "6":
				continue
			return False
		return True

	result = []
	for i in range(num+1):
		if is_mirror(i):
			result.append(i)
	return result

# -----------------------------------------------------------
# 아래 코드는 테스트용입니다 건들지마세요.
import mirror_test as mt
if __name__ == "__main__":
	mt.test(mirror)

