#brute force sollution
a = 26

x = 0
y = 1

while a > x*x and a > y*y:
    x += 1
    y += 1

if a == y*y:
    print(str(y) + " brute force sollution")
else:
    print(str(x) + " brute force sollution")

#solution using binary search, levá a pravá strana se budou posouvat k sobě, dokud se nebudou rovnat

l, r = 0, a

while l <= r:
    m = l + (r -l) // 2
    if m * m > a:
        r = m - 1
    elif m * m < a:
        l = m + 1
        res = m
    else:
        print(str(m) + " binary search sollution")
        break
print(str(res) + " binary search sollution")