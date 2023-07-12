def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a//10000
    y=a//1000%10
    z=a//100%10
    l=a//10%10
    m=a%10
    return (x>y and y>z and z>l and l>m)
print(main(12345))
print(main(76532))