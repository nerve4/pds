name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

di = dict()

for lin in handle:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

tmp = list()
for k,v in di.items():
    #print(k,v)
    newt = (v,k)
    tmp.append(newt)

#print(tmp)

tmp = sorted(tmp, reverse=True)
#print('Sorted',tmp[:5])

for v,k in tmp[:5]:
    print(k,v)