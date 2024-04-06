#x = input("What is a x?")
#y = input("What is a y?")
#z = int(x) + int(y)
#print(z)
r = 12
print(float(r))
e = 12.1
b = 12.5
c = e + b
print(round(c))

def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    return n * n
main()