filename = "mini-trips-4.csv"
infile = open(filename)
header = infile.readline() 
durations = []
for line in infile:
    line = line.removesuffix('\n')
    row = line.split(',')
    duration = int(row[0])
    durations.append(duration)
infile.close()

durations.sort() 

print("trips:", len(durations))
print("shortest trip:", durations[0])
print("longest trip:", durations[-1])
print("mean duration:", sum(durations)/len(durations))
print("median duration:", (durations[len(durations)//2]+durations[(len(durations)-1)//2])/2)



