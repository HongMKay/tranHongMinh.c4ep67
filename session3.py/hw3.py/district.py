dis = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
pop = [150300, 247100, 333300, 266800, 420900, 318000]
max_pop = max(pop)
min_pop = min(pop)
a = pop.index(max_pop)
b = pop.index(min_pop)

print("Index of max pop district: ",a)
print("Index of min pop district: ",b)
print("Max pop district: ",dis[a])
print("Min pop district: ",dis[b])

area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]

mat_do = []
for i in range (6):
    n = pop[i]/area[i]
    mat_do.append(int(n))
print("Mật độ dân số của các quận: ",mat_do)
ave_mdo = sum(mat_do)/len(dis)
print("Mật độ dân cư trung bình: ", ave_mdo)