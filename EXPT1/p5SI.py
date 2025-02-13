p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest(per annum): "))
t = float(input("Enter the Number of Years: "))

si = (p * r * t) / 100

print(f"Simple Interest on the principal amount of {p} @ {r}% per annum for {t} years is: {si}")