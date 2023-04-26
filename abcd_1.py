def ram(a, b, c):
    if(b**2 >= 4 * a* c):
        r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

    else:
        print("결과가 허수입니다.")
    return r1, r2
