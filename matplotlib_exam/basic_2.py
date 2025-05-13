import re

txt="Field. Friend fr!end"
# 단어 패턴 => 포함하는 경우 탐색
n=re.findall(r'ie',txt)
print(n)
txt="""
    삼성전자는 이번 갤럭시S25 엣지 신작으로 스마트폰 디자인 트랜드를 선도하고, 전통적 비수기인 2분기 실적 반전을 꾀한다는 전략이다.
    현재 스마트폰 업계는 고가의 플래그십 제품 판매량을 늘리기 위해 제품 폼팩터 다변화를 고민 중이다.
    삼성과 애플 모두 올해부터 내년까지 본격 슬림 제품을 추가로 선보일 예정이다.
    또한 삼성전자는 미국발 관세 여파로 2분기 반도체 실적이 불확실할 것으로 전망하고 있는데,
    스마트폰 분야에서 1분기 이어 2분기에도 호실적을 올려 이를 상쇄하고자 하는 전략이다.
    
    삼성전자는 12일 오전 9시 삼성닷컴 등 온라인에서 공개행사를 열고 갤럭시S25 엣지 신작 스마트폰을 공개했다.
    삼성전자는 “갤럭시S25 엣지는 역대 갤럭시S시리즈 중 가장 얇으면서도 강력한 성능, 견고한 내구성을 모두 갖춘 제품”이라고 했다.
"""
# [가-힣] => Konlp
n=re.findall(r'[가-힣]+',txt)
print(n)
print(len(n))

#n=re.findall(r'\d+',txt)
n=re.findall(r'[0-9]+',txt)
print(n)

txt="123456 23456"
print(re.findall(r'234',txt))

txt1="white      space"
txt2="white space"
print(re.findall(r'e\ss',txt1))
print(re.findall(r'e\ss',txt2))
# a2f aaa 15f = a\df
# ^,$
txt="this this this this"
print(re.findall(r"^this",txt))
print(re.sub(r"^this","Begin",txt))
print(re.findall(r"this$",txt))
print(re.sub(r"this$","End",txt))
# 중괄호
txt="Teth Teeth Teeeth Teeeeth"
print(re.findall(r"Te{1,3}th",txt))
# TE + {e ee eee} + th
print(re.findall(r"Te{0,1}th",txt))
# Teth Teeth
print(re.findall(r"Te{2,}th",txt))
# *(0이상), +(1이상)
txt="Tth Teth Teeth Teeeta Taskfsfsfsfsfdsfth"
print(re.findall(r"Te*th",txt))
# Te*th => T시작 문자는 e가 0이상 th로 종료
# Youtube 동영상 키
print(re.findall(r"Te+th",txt))
print(re.findall(r"T[^e]*th",txt))
# e를 제외한 문자가 여러개 0개 존재
txt="""
    211.238.142.101 127.0.0.1 123,123,123,123 192.168.1.101
"""
n=re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",txt)
print(n)
n=re.findall(r"\d+",txt)
print(n)

txt='"abcd" <abc>'
n=re.findall(r"<[^>]*>|\"[^\"]*\"",txt)
# < => >를 제외 => 문자여러개 => >
# 여는 " => 닫는 "를 제외 => 문자 여러개 => 닫는 "
# 인용 부호 => 사람이름 , Actor
print(n)

#() => 그룹
#   (([0,9]{1,3})\.([0,9]{1,3})\.([0,9]{1,3}))\.([0,9]{1,3})
#   ------------------------------------------  ------------
#       회사 번호                                   고유 번호
txt="My Phone number is 010-1111-1111"
match=re.search(r"(\d{3})-(\d{4})-(\d{4})",txt)
if match:
    print("번호 전체:",match.group(0))
    print("Area:",match.group(1))
    print("Prifix:",match.group(2))
    print("Line:",match.group(3))
    # group() => list, groups() => tuple
    print(match.groups())
    # search => 없는 경우 : none 반환
    # 문자 대체 => sub
    # 찾기 => findall
    # 단어 => 긍정 / 부정 => 데이터 사전 => 가중치
    # 트위터 / 페이스북 => 대선
    # 정규식은 문자열의 형태를 만들어서 찾는다
    # ----- 오라클 / MySQL regexp_like()
    # split(정규식) replaceAll(정규식)