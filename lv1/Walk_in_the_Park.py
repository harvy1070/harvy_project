def solution(park, routes):
    x, y = 0, 0
    # park의 S = 시작점이 어딘지 파악하는 for문
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = i
                y = j
                break
    print("1. x = {0}, y = {1}".format(x, y))

    for i in routes:
        a, b = x, y
        print("2. i = {0}, a = {1}, b = {2}".format(i, a, b))
        for j in range(int(i[2])):
            print("3. i = {0}, a = {1}, b = {2}".format(i, a, b))
            if i[0] == 'N' and b != 0 and park[b-1][a] != 'X':
                b -= 1
                if j == int(i[2]) - 1:
                    y = b
            elif i[0] == 'S' and b != len(park)-1 and park[b+1][a] != 'X':
                b += 1
                if j == int(i[2]) - 1:
                    y = b
            elif i[0] == 'W' and a != 0 and park[b][a-1] != 'X':
                a -= 1
                if j == int(i[2]) - 1:
                    x = a
            elif i[0] == 'E' and a != len(park[0]) - 1 and park[b][a+1] != 'X':
                a += 1
                if j == int(i[2]) - 1:
                    x = a
    return [x, y]

park = ["OOS", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]
print(solution(park, routes))
