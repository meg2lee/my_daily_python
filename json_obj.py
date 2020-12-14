member_data = {
    'num':11, 'name':'Landon', 'phone':'010-2547-8540',
    'hobby':['gaming','reading'] # json 배열
} #파이썬 dict이자, json 오브젝트
print(type(member_data)) # <class 'dict'>

import json

#json 오브젝트를 직렬화하여 파일에 저장
with open('member.json','w')as json_file: #빈 파일 생성
    json.dump(member_data, json_file) #左를 右에 저장
    
#json  오브젝트를 문자열로 메모리에 저장
json_str = json.dumps(member_data, indent=4) #dumps는 메모리에 문자열로 저장하기 위함
print('json string:','r')as json_file:
    python_dic = json.load(json_file) #load는 파일에서 메모리로 도로 가져옴(문자열 or dict)
print(type(python_dic)) # <class 'dict'>

#메모리에 문자열 형태로 저장된 json 데이터를 파이썬 dict로 변환하기
dic2 = json.loads(json_str) #loads는 문자열로부터 load(곧, dict형)
print(type(dic2)) # <class 'dict'>
