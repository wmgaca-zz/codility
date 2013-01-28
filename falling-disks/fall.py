'''http://codility.com/cert/view/certD43YXR-NQJ6M64JS5B2ZU3K/details
'''

def solve(A, B):
    if B[0] > A[0]: return 0

    m = {}
    for i, a in enumerate(A):
        if a not in m: m[a] = i

    bottom = len(A)
    result = 0

    for b in B:
        if not bottom or b > A[0]: 
            return result
        bottom -= 1
        for lt in xrange(1, b):
            if lt in m and m[lt] < bottom: bottom = m[lt]
        if A[bottom] < b: bottom -= 1

        result += 1
    
    return result

print solve(A=[5, 6, 4, 3, 6, 2, 3], B=[2, 3, 5, 2, 4])
