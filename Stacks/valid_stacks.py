"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed_index = 0
        popped_index = 0
        stack = []
        if len(popped) > len(pushed):
            return False
        while pushed_index < len(pushed) + 1 and popped_index < len(popped):
            if popped_index == len(popped):
                return True
            elif pushed_index == len(pushed):  # 5
                # print('Done Pushing!')
                for i in range(len(popped) - popped_index):
                    if stack[-1] != popped[popped_index]:
                        return False
                    else:
                        stack.pop()
                        popped_index += 1
            elif len(stack) > 0 and stack[-1] == popped[popped_index]:
                stack.pop()
                popped_index += 1
            elif pushed[pushed_index] != popped[popped_index]:
                stack.append(pushed[pushed_index])
                pushed_index += 1
            else:
                pushed_index += 1
                popped_index += 1
            # print(stack)
            # print(pushed_index, popped_index)
        return True


# pushed       popped      pushed_index   popped_index   stack
# [2, 1, 0]    [1, 2, 0]        0              0         []
