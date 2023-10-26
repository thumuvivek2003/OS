data = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2,1,2,0,1,7,0] 
capacity = 3
s = set()
indexes = {}
faults = 0
for i,page in enumerate(data):
    print(f"Searching for {page} in {s} having {indexes}")
    if len(s)<capacity:
        if page not in s:
            print(" : Fault")
            s.add(page)
            faults += 1
    else:
        if page not in s:
            print(" : Fault")
            faults += 1
            lru = float("inf")
            for frame in s:
                if indexes[frame]<lru:
                    val = frame
                    lru = indexes[frame]
            s.remove(val)
            s.add(page)
    indexes[page] = i
print(faults)

