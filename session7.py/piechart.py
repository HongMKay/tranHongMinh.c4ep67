from matplotlib import pyplot

#1. prepare data
machine_counts = [18, 4, 2]

#2. prepare labels
machine_names = ["PC", "MAC", "Linus"]

#3. draw pie
pyplot.pie(machine_counts, labels = machine_names, autopct = "%.1f%%", shadow = True, explode = [0, 0.2, 0.2]) 
# autopct để hiện số phần trăm
#explode để tách cái phần của pie ra
pyplot.title("PC vs MAC vs Linux usage")
pyplot.axis("equal") #chỉnh cho hình tròn
#4. Show
pyplot.show()