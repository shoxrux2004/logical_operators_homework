def main(a,b,c):
    return (b>a and b<c) or (b<a and b>c)
print(main(2,3,4))
print(main(6,4,5))
print(main(7,6,5))
"""
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """