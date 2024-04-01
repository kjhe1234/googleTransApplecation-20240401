import re  # regular expressions 정규표현식 표준 라이브러리

# str = "안녕 Good Morning!! 오늘은 3월26일이야!?"
#
# # 한글만 추출
# pattern = re.compile("[ㄱ-ㅎ|가-힣]+")
# result = pattern.findall(str)
# print(result)

# 영어만 추출
# pattern = re.compile("[a-z|A-Z]+")
# result = pattern.findall(str)
# print(result)

# 영어만 제거
# pattern = re.compile("[^a-z|A-Z]+")
# result = pattern.findall(str)
# print(result)

# 주민번호 뒷자리 *로 마스킹
# str2 = "991231-1234567"
#
# pattern = "-[0-9]{7}"   # - 뒤에 숫자 7자리가 나오는 패턴을 찾아라
# result1 = re.sub(pattern, "-*******", str2)
# print(result1)


word = "안녕"
reg = re.compile(r'[가-힣]')

if reg.match(word):
    print("한글입니다")

else:
    print("한글이 아닙니다.")







