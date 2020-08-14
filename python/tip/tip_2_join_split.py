# split
# String type의 값을 나눠서 list형태로 변환
items = 'zero one two three'.split() # 빈칸을 기준으로 문자열 나누기
print(items)
# ['zero', 'one', 'two', 'three']
example = 'python,java,c'.split(",") # ","을 기준으로 문자열 나누기
print(example)
# ['python', 'java', 'c']

# --------------------------------------------------

# unpacking
# 나눠 담기
email_address = 'djyou128@mju.ac.kr'
user_id, domain_address = email_address.split('@')
print(f"user_id : {user_id} , type : {type(user_id)}")
print(f"domain_address : {domain_address} , type : {type(domain_address)}")
# user_id : djyou128 , type : <class 'str'>,
# domain_address : mju.ac.kr , type : <class 'str'>,
sub_domain, domain, nation = domain_address.split('.')
print(sub_domain, domain, nation)
# mju ac kr
# nation이 없다면?

# --------------------------------------------------

# join
# list type의 값들을 합쳐서 String type으로 변환
color = ['red', 'blue', 'yellow']
print(''.join(color)) # 공백 없이 합치기
# redblueyellow
print(' '.join(color))# 공백 넣고 합치기
# red blue yellow
print('-'.join(color)) # '-' 넣고 합치기
# red-blue-yellow