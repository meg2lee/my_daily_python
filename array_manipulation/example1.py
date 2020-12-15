import numpy as np

print('3개의 행렬 생성 [1,2,3] [4,5,6] [7,8,9]:')
arr = np.arange(1,10).reshape([3,3])
print(arr)

print('1행짜리 배열 3개 a,b,c:')
a,b,c = np.vsplit(arr,3)
print(a,b,c)

print('이들 행렬을 컬럼으로 d행렬 생성:')
d = np.column_stack((a.ravel(),b.ravel(),c.ravel()))
print(d)

print('이들 행렬을 행으로 사용하여 e행렬 생성:')
e = np.row_stack((a,b,c))
print(e)

print('d,e행렬을 수직으로 합쳐서 h행렬 생성:')
h = np.vstack((d,e))
print(h)

print('d의 수직합계, e의 수평합계를 수평으로 합쳐서 i행렬 생성:')
d1 = d[:,0].sum()
d2 = d[:,1].sum()
d3 = d[:,2].sum()

e1 = e[0,:].sum()
e2 = e[1,:].sum()
e3 = e[2,:].sum()

ds = np.array([d1,d2,d3])
es = np.array([e1,e2,e3])

i = np.hstack((ds,es))
print(i)

print('h행렬의 첫번째, 세번째 컬럼 수평합계 산출:')
h1sum = h[:,0].sum()
print(h1sum)

h3sum = h[:,2].sum()
print(h3sum)
