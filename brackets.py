def solution(S):
    # write your code in Python 3.6
    stack = []
    reverse = {'{': '}', '[': ']', '(': ')'}
    N = len(S)
    if N == 0:
        return 1
    if N % 2 == 1:
        return 0
    for s in S:
        if s in reverse:
            stack.append(s)
        else:
            if len(stack) >= 1 and reverse[stack[-1]] == s:
                stack.pop(-1)
    result = 0
    if len(stack) == 0 and (s not in reverse):
        result = 1
    return result