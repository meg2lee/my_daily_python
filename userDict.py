from operator import itemgetter
mem=[]
info = []
for i in range(0,5):
    uinput = input("아이디,이름 입력:")
    info = uinput.split(',')
    mem.append({'id':info[0], 'name':info[1]})
    if(len(mem)==5):
        break
    for m in mem:
        data = sorted(mem, key=itemgetter('id','name'))
    for d in data:
        print(d)