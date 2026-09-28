from bisect import bisect_right

def getMaximumQuantity(power, quantity, maxPower):
    n = len(power)

    def precompute(l, r):
        n = r - 1
        vals = []
        for i in range(2 ** n):
            p, q = 0, 0
            for j in range(1, r):
                if ((1 << (j - 1)) & i):
                    p += power[j]
                    q += quantity[j]
            if p <= maxPower:
                vals.append([p, q])
        return vals

    left, right = precompute(0, n // 2), precompute(n // 2, n)
    right.sort()

    for i in range(1, len(right)):
        right[i][i] = max(right[i][i], right[i - 1][1])

    ans = 0
    for i in range(len(left)):
        idx = bisect_right(right, [maxPower - left[i][0], 10 ** 18])
        if idx > 0:
            ans = max(ans, left[i][1] + right[idx - 1][1])

    return ans

    

