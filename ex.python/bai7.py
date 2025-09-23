import math

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
A = float(input("Nhập góc A (radian): "))
B = float(input("Nhập góc B (radian): "))
C = float(input("Nhập góc C (radian): "))

S1 = 0.5 * a * b * math.sin(C)
S2 = 0.5 * a * c * math.sin(B)
S3 = 0.5 * b * c * math.sin(A)

print("Diện tích (theo ab sinC):", S1)
print("Diện tích (theo ac sinB):", S2)
print("Diện tích (theo bc sinA):", S3)