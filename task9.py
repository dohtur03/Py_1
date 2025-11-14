# Calculate the derivative of a given polynomial at a given point

def main():
    result = calculator()
    print(f"{result:.3f}")

def calculator():
    high_d_str, x_v_str = input().split()
    high_degree = int(high_d_str)
    x_value = float(x_v_str)

    coeffs = []
    for _ in range(high_degree + 1):
        c = float(input())
        coeffs.append(c)

    deriv_res = 0.0

    # Calculate using formula: derivative of a*x^n is a*n*x^(n-1)
    for i in range(high_degree):
        coeff = coeffs[i]
        power = high_degree - i
        deriv_res += coeff * power * (x_value ** (power - 1))

    return deriv_res

if __name__ == "__main__":
    main()

