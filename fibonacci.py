_cache = {}
def fibonacci(n):
    #if n == 1 or n == 2:
    #     return 1
    # if n > 2:
    #     return (fibonacci(n-1) + fibonacci(n-2))
    # Write your code here.
    
    if n in _cache:
        return _cache[n]
    if n == 1 or n == 2:
         return 1
    elif n > 2:
        return (fibonacci(n-1) + fibonacci(n-2))
    _cache[n] = value
    return value
