def caching_fibonacci():
    """
    Creates and returns a Fibonacci function with caching.

    The inner function 'fibonacci' computes the n-th Fibonacci number recursively.
    It uses the 'cache' dictionary to store already computed Fibonacci numbers.
    If a value has been computed before, it is returned immediately from the cache,
    which significantly improves performance for repeated calls.

    Returns:
        function: The 'fibonacci' function that computes the n-th Fibonacci number.
    """
    cache = {}  # A dictionary to store already computed Fibonacci numbers

    def fibonacci(n: int) -> int:
        """
        Recursively computes the n-th Fibonacci number using caching.

        Args:
            n (int): The position in the Fibonacci sequence.
                     For n <= 0, returns 0; for n == 1, returns 1.

        Returns:
            int: The n-th Fibonacci number.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Compute the n-th Fibonacci number recursively
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Example usage
if __name__ == '__main__':
    fib = caching_fibonacci()
    print(fib(5))   # 5
    print(fib(10))  # 55
    print(fib(15))  # 610
    print(fib(20))  # 6765
