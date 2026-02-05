MAXN = 400000


is_prime = [True] * (MAXN + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAXN ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN + 1, i):
            is_prime[j] = False


t = int(input())
for _ in range(t):
    n = int(input())

    if n < 5:
        print(-1)
        continue

    odds = [i for i in range(1, n + 1, 2)]
    evens = [i for i in range(2, n + 1, 2)]

    last_odd = odds[-1]
   
    first_even = -1
    for e in evens:
        if not is_prime[last_odd + e]:
            first_even = e
            break

   
    evens.remove(first_even)
    ans = odds + [first_even] + evens

    print(*ans)