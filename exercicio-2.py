listadois = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ordeminversa = []
for i in range (0, len(listadois))
ordeminversa.append(listadois[len(listadois)-1])
listadois.pop()

print(ordeminversa)