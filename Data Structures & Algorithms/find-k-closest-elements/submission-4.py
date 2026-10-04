class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        R = k - 1

        diff = sum(abs(x - arr[i]) for i in range(k))
        best_diff = diff
        best_L = L

        while R + 1 < len(arr):
            diff -= abs(x - arr[L])
            L += 1

            R += 1
            diff += abs(x - arr[R])

            if diff < best_diff:
                best_diff = diff
                best_L = L

        return arr[best_L:best_L + k]
        