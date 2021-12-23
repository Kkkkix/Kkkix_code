def triangles():
    first_row = [1]
    current = first_row.copy()
    for n in range(10):
        yield current
        temp = [1]
        for x in range(len(current)-1):
            temp.append(current[x]+current[x+1])
        temp.append(1)
        current = temp.copy()
    return 'done'