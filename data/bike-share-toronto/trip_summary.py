filename = "trips.csv"
infile = open(filename)
header = infile.readline()
durations = []
durations_min = []
for line in infile:
    line = line.removesuffix('\n')
    row = line.split(',')
    duration = int(row[0])
    durations.append(duration)
    durations_min.append(duration/60)
infile.close()
durations.sort()
durations_min.sort()


print("number of trips:", len(durations))
print("shortest trip:", durations[0], durations[0]/60)
print("longest trip:", durations[-1], durations[-1]/60)
print("mean duration:", sum(durations)/len(durations), sum(durations)/len(durations)/60)
print("median duration:", (durations[len(durations)//2]+durations[(len(durations)-1)//2])/2, (durations[len(durations)//2]+durations[(len(durations)-1)//2])/120)
print("top three longest rides in minutes:", durations_min[-3:])
