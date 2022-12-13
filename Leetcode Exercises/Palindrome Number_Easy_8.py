n = int(input("Enter a number: "))
r = []
for i in range(len(str(n))):
    result = n%10
    r.append(result)
    n = n // 10
for j in range(len(r)):
    if r[j] == r[len(r)-1-j]:
        print("True")
        break
    else:
        print("False")
        break

