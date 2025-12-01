
f = open("sample.txt", "r")
line = f.readline()
routerIDs = {}
hopTTLs = {}
while line.strip():
    tcpExtract = line.split()
    nextLine = f.readline()
    if "ICMP" in nextLine: 
        end = float(tcpExtract[0])
        currentIP = nextLine.split()[0]
        nextLine2 = f.readline()
        pid = nextLine2.split()[6][:-1]
        currRTT = round((end - routerIDs[pid][0]) * 1000, 3)
        routerIDs[pid].append(currRTT)
        hopTTLs[routerIDs[pid][1]] = currentIP
        f.readline()
    else:
        start = float(tcpExtract[0])
        currTTL = tcpExtract[5][:-1]
        pid = tcpExtract[7][:-1]
        routerIDs[pid] = [start, currTTL]
    line = f.readline()
output = ""
currTTL = ""
for pid in routerIDs:
    if len(routerIDs[pid]) == 3:
        if routerIDs[pid][1] != currTTL:
            currTTL = routerIDs[pid][1]
            print("TTL " + currTTL)
            output += "TTL " + currTTL + "\n"
            print(hopTTLs[currTTL])
            output += hopTTLs[currTTL] + "\n"
        print("{rtt:.3f} ms".format(rtt = routerIDs[pid][2]))
        output += "{rtt:.3f} ms".format(rtt = routerIDs[pid][2]) + "\n"
f.close()
with open("test.txt", "w") as file:
    file.write(output)