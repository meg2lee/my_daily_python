def read_file():
    info = input("회원번호,이름,전화;")
    num,name,phone = info.split(',')
    
    
def add_info():
    

while True:
    action = input("추가(a),검색(s)")
    
    if(action=='a'):
        
        with open('members.csv','a') as file_object:
