mathScores = [60, 70, 10, 20, 81, 63, 1521]
print(sum(mathScores))
print(max(mathScores))
s = sum(mathScores)
l = len(mathScores)
print(s/l)
mathScores.append(63)
del mathScores[0:2]
print(mathScores)
mathScores[2] = 100
print(mathScores)
print(100 in mathScores)

ls = [[1, 2, 3],[4, 5, 6]]
print(ls[0][0])
print(sorted(mathScores))