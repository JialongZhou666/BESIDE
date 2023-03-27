import random

perturbated_rate = 0.2
edge_num = 19349
perturbated_edge_id = random.sample(range(0, edge_num), int(edge_num * perturbated_rate))
cnt = 0
print("pertubated_edge_id=", perturbated_edge_id)

with open("bitcoinalpha0320.txt.map.train", 'r') as f1:
    line = f1.readline()
    print("line[-3:-2]=", line[-3:-2])
    if cnt in perturbated_edge_id:
        if line[-3:-2] == " ":
            print("line[-3:-2]==' '")
            with open("bitcoinalpha0320_poisoned_20.txt.map.train", 'a') as f2:
                f2.write(line[0:-3] + " -1\n")
        elif line[-3:-2] == "-":
            print("line[-3:-2]==-")
            with open("bitcoinalpha0320_poisoned_20.txt.map.train", 'a') as f2:
                f2.write(line[0:-3] + " 1\n")
    else:
        with open("bitcoinalpha0320_poisoned_20.txt.map.train", 'a') as f2:
                f2.write(line)
    while line is not None and line != '':
        cnt += 1
        line = f1.readline()
        print("line[-3:-2]=", line[-3:-2])
        if cnt in perturbated_edge_id:
            print("cnt=", cnt)
            if line[-3:-2] == " ":
                print("line[-3:-2]==' '")
                with open("bitcoinalpha0320_poisoned_20.txt.map.train", 'a') as f2:
                    f2.write(line[0:-3] + " -1\n")
            elif line[-3:-2] == "-":
                print("line[-3:-2]==-")
                with open("bitcoinalpha0320_poisoned_20.txt.map.train", 'a') as f2:
                    f2.write(line[0:-3] + " 1\n")
        else:
            with open("bitcoinalpha0320_poisoned_20.txt.map.train", 'a') as f2:
                    f2.write(line)