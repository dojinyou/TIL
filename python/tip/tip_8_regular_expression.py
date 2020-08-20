# 정규표현식(Regular Expression)

# 메타 문자(meta characters) - 문자 그대로 뜻이 아닌 특별한 뜻으로 사용되는 문자
# . ^ $ * + ? { } [ ] \ | ( )

import re
text = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''
regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{4}'
print(re.findall(regex, text))

# --------------------------------------------------

# 문자 클래스
# [] : 안에 있는 것 중에 하나(^ 사용하면 부정의 의미)
# \d : 숫자만
# \w : 모든 문자 + _
# \s : 공백(space tab enter verticaltab 등)

# --------------------------------------------------

# dot(.)
# \n 줄바꿈 말고 모든 문자와 매칭
# asterisk(*)
# 0번 이상 반복
# plus(+)
# 1번 이상 반복
# {s,e}
# s번 이상 e번 이하 반복
# ?
# 있거나 없거나