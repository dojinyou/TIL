# https://www.acmicpc.net/problem/11655

originText = input()
ROT13Text = ""
for c in originText:
	if not c.isalpha():
		ROT13Text += c
	elif c.isupper():
		ROT13Text += chr((ord(c)-65+13)%26+65)
	elif c.islower():
		ROT13Text += chr((ord(c)-97+13)%26+97)
print(ROT13Text)