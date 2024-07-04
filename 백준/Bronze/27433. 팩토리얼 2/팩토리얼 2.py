def factorial_recursive(n):
    return n*factorial_recursive(n-1) if n>1 else 1

n = int(input())
answer = factorial_recursive(n)
print(answer)