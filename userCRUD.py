from member import *

def read_file():
    info = input("회원번호,이름,전화;")
    num,name,phone = info.split(',')
    print(Member(num,name,phone))
    
def add(m):
    with open('members.csv','a') as file_object:
        file_object.write(f'{m.num},{m.name},{m.phone}\n')
        
def search_mem(num):
    with open('members.csv','a') as file_object2:
        for m in file_object2:
            mnum,name,phone = n.split(',')
            if(num==mnum):
                print(m)

while True:
    action = input("추가(a),검색(f),취소(x)")
    
    if(action=='a'):        
        add(read_file())
        
    elif(action=='f'):
        num = int(input("검색할 회원번호:"))
        search_mem(num)
        
    elif(action=='x'):
        break

print('프로그램 종료...')


    
