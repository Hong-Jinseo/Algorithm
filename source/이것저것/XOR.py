
s = list(map(int, input().split()))

result1 = s[0] ^ s[1]
print("2진수 : ", bin(result1), "=", bin(s[0]), "XOR", bin(s[1]))
print("s[0] ^ s[1] : ", result1)

print()

result2 = s[0] ^ s[1] ^ s[2]
print("2진수 : ", bin(result2), "=", bin(s[0]), "XOR", bin(s[1]), "XOR", bin(s[2]))
print("s[0] ^ s[1] ^ s[2] : ", result2)
