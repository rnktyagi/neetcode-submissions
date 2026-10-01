class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if not stack:
                stack.append(i)

            elif stack[-1] < 0 or i > 0:
                stack.append(i)

            else:
                while stack and stack[-1] > 0 and abs(i) > abs(stack[-1]):
                    stack.pop()

                if not stack or stack[-1] < 0:
                    stack.append(i)

                elif abs(stack[-1]) == abs(i):
                    stack.pop()

        return stack

