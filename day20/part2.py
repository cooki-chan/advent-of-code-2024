input = open('day20/inp.txt').read().split('\n')

start = []
for row, data in enumerate(input):
    for col, dat in enumerate(data):
        if dat == "S":
            start = [row, col]
            break

curr = start
currVal = "S"
points = [start.copy()]

while not currVal == "E":
    print(len(points))
    tests = [[1, 0], [-1, 0], [0,1], [0, -1]]
    for i in tests:
        test = [curr[0]+i[0], curr[1]+i[1]]
        if test not in points and input[test[0]][test[1]] in ".E":
            points.append(test)
            curr = test
            currVal = input[test[0]][test[1]]

print()
def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

out = set()
for currentID in range(len(points)):
    print(currentID)
    for test in range(currentID+1, len(points), 1):
        if abs(dist(points[currentID], points[test])) <= 20: 
            if abs(currentID - test + dist(points[currentID], points[test])) >= 100:
                out.add((tuple(points[currentID]), tuple(points[test])))
print()
print(out)
print(len(out))