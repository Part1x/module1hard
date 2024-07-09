grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron',}
sort = sorted(list(students))
finish = {}
for a, b in enumerate(sort):
    finish[b] = sum(grades[a]) / len(grades[a])

print(finish)