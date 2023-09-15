
counter = 0
def memoize(f):
    cache = {}
    
    def inner(num):
        if num not in cache:
            cache[num]= f(num)
            return cache[num]
        return inner


@memoize
def fibonacci2(num):
    if num <= 1:
        return 1
    return fibonacci2(num - 1) + fibonacci2(num - 2)

fibonacci2(100)   


@memoize
def count(num):
    if num ==1:
        return 1
    return fibonacci2(num-1) *num

    
count(100)

def count_calls(func):
        def helper(*args):
            helper.calls +=1
        return func(*args)
        helper.calls = 0


def fibonacci(self, n):
    cache = {}
    def recur_fibonacci(n):
        if n in cache:
            return cache[n]

        if n < 2:
            result = n
        else:
            result = recur_fibonacci(n-1) + recur_fibonacci(n-2)

        # put result in cache for later reference.
        cache[n] = result
        return result

    return recur_fibonacci(n)
