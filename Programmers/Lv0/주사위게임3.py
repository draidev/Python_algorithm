from collections import Counter

def solution(a, b, c, d):    
    # Count frequency of each number
    counts = Counter([a, b, c, d])
    items = list(counts.items())
    items.sort(key=lambda x: -x[1])  # Sort by frequency, descending
    
    if len(items) == 1:
        # All four numbers are the same
        p = items[0][0]
        return 1111 * p
    elif len(items) == 2:
        if items[0][1] == 3:
            # Three numbers are p, one is q
            p = items[0][0]
            q = items[1][0]
            return (10 * p + q) ** 2
        else:
            # Two numbers are p, two numbers are q
            p = items[0][0]
            q = items[1][0]
            return (p + q) * abs(p - q)
    elif len(items) == 3:
        # One number repeats twice, the others are different
        p = next(x[0] for x in items if x[1] == 2)
        others = [x[0] for x in items if x[1] == 1]
        q, r = others[0], others[1]
        return q * r
    elif len(items) == 4:
        # All numbers are different
        return min(a, b, c, d)

    return answer