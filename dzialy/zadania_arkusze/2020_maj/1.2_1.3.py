n = 3
k = 0

A = [5, 7, 9]
B = [5, 7, 9]


def czy_k_podobne(n, A, B, k):
    for i in range(k):

        if A[i] != B[n - k + i]:
            return False

    return all(B[i] == A[k + i] for i in range(n - k))


def czy_podobne(n, A, B):
    for k in range(n):
        return bool(czy_k_podobne(n, A, B, k))


print(czy_k_podobne(n, A, B, k))
