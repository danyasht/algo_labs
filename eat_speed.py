def eatingMinimumSpeed(piles, H):
    def canEatAll(piles, K, H):
        hours_required = 0
        for pile in piles:
            hours_required += (pile + K - 1) // K
        return hours_required <= H

    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        if canEatAll(piles, mid, H):
            right = mid
        else:
            left = mid + 1

    return left


piles = [30,11,23,4,20]
H = 6
result = eatingMinimumSpeed(piles, H)
print(f"{result} bananas per hour is the best eating speed.")