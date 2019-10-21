import random as rm

def det(mat):
	#ожидается квадратная матрица
	order = len(mat)
	if order == 1: return mat[0][0]
	elif order == 2:
		return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
	else:
		total = 0
		for x in range(len(mat[0])):
			tm = []
			for l in mat[1:]:
				tl = l[:]
				del tl[x]
				tm.append(tl)
			total += mat[0][x]*((-1)**(2+x))*det(tm)
		return total


x, y = rm.randint(2, 10), rm.randint(2, 10);

matrix = [[rm.randint(2,99) for x in range(x)] for m in range(y)]

matrix = [[3,2,7,1, 3], [4,1,3,2,2], [7,5,4,8,7], [0,7,2,1,0],[-15,9,11,8,-11]]

s = str(matrix).replace("[", "{")
s = s.replace("]", "}")
print(s)

if len(matrix) == len(matrix[0]):
	print(det(matrix))
else: 
	print("БЕЗ ОПРЕДЕЛИТЕЛЯ")
	

'''elif order == 3:
		return mat[0][0]*mat[1][1]*mat[2][2]+mat[0][2]*mat[1][0]*mat[2][1]+mat[0][1]*mat[1][2]*mat[2][0]-mat[0][2]*mat[1][1]*mat[2][0]-mat[0][0]*mat[1][2]*mat[2][1]-mat[0][1]*mat[1][0]*mat[2][2]'''
