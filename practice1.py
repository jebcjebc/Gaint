grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
print(grades[2])
C = sum(grades[0]) / len(grades[0])
E = sum(grades[1]) / len(grades[1])
M = sum(grades[2]) / len(grades[2])
print(C, E, M)
grades.append([94, 90, 96])
grades[0].append(60)
print(grades)
print('-------------------------------------------')

gradesTuple = ((5, 14, 7), (23, 36, 28), (88, 80, 92))
print(gradesTuple[2])
C1 = sum(gradesTuple[0])/len(gradesTuple[0])
E1 = sum(gradesTuple[1])/len(gradesTuple[1])
M1 = sum(gradesTuple[2])/len(gradesTuple[2])
print(C1, E1, M1)
Stuple = ((94, 90, 96),)
grades = gradesTuple + Stuple
print(grades)
print('-------------------------------------------')

gradesDict = {'chinese':[5, 14, 7], 'english':[23, 36, 28], 'math':[88, 80, 92]}
print(gradesDict['math'])
C2 = sum(gradesDict['chinese'])/len(gradesDict['chinese'])
E2 = sum(gradesDict['english'])/len(gradesDict['english'])
M2 = sum(gradesDict['math'])/len(gradesDict['math'])
print(C2, E2, M2)
gradesDict['science'] = [94, 90, 96]
print(gradesDict)
print('-------------------------------------------')

allStudents = {'John', 'Eva', 'Jill', 'Eric', 'Andy', 'Albert', 'Polina', 'Kristin', 'Angela' }
danceClub = {'John', 'Eva', 'Jill', 'Eric', 'Andy'}
guitarClub = {'Eric', 'Andy', 'Albert', 'Polina', 'Kristin'}
print(danceClub & guitarClub)
print(guitarClub-danceClub)
print(allStudents-(guitarClub | danceClub))
print('-------------------------------------------')

