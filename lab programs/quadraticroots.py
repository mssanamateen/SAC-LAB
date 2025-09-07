import math
def quadratic_roots(a, b, c):
    """Return nature and roots of quadratic equation."""
    D = b**2 - 4*a*c
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        return "Real and distinct", (root1, root2)
    elif D == 0:
        root = -b / (2*a)
        return "Real and equal", (root,)
    else:
        real = -b / (2*a)
        imag = math.sqrt(abs(D)) / (2*a)
        return "Imaginary", (f"{real}+{imag}i", f"{real}-{imag}i")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
nature, roots = quadratic_roots(a, b, c)
print("Nature of roots:", nature)
print("Roots:", roots)
