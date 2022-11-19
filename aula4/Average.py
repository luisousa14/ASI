import ReadLogFile

def AverageTime(visit):
    sites = {}
    for key, value in visit.items():
        num_utli = len(value.keys())
        total_tempo = 0
        for key1, value1 in value.items():
            total_tempo += value1[1]
        sites[key] = float(total_tempo/num_utli)
    print(sites)



AverageTime(ReadLogFile.Read("weblog.txt"))
