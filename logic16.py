def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (a>9999 and a<1000000)
print(main(15234))
print(main(777))