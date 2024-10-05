#DEFINIRANJE FUNKCIJE

def calculate(h,mph):
    return (h*mph)


print("Upiši broj radnih sati:")
h = float(input())
print("Upiši koliko si plaćen po satu:")
mph = float(input())

print(calculate(h,mph))

