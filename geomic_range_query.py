def solution(S, P, Q):
    # write your code in Python 3.6
    M = len(P)
    value = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    result = []
    for i in range(M):
        for nuc in value:
            if nuc in S[P[i]: Q[i]+1]:
                result.append(value[nuc])
                break
    return result