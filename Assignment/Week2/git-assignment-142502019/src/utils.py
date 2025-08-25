def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0

def factorial(n):
    """Compute factorial of n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    print("Is 4 even?", is_even(4))
    print("Factorial of 5:", factorial(5))
