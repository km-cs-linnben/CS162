def fib_efficient(n):
    """Recursive fibonacci that remembers previous values."""
    if n not in fib_dict:
        # recursive case, store in the dictionary
        fib_dict[n] = fib_efficient(n-1) + fib_efficient(n-2)
    return fib_dict[n]
