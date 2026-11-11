a = "1111"
b = "1111"
r = ""
h = 0

while a != "" and b != "":
    if int(a[len(a) - 1]) + int(b[len(b) - 1]) + h == 3:
        r = "1" + r
        h = 1
    if int(a[len(a) - 1]) + int(b[len(b) - 1]) + h == 2:
        r = "0" + r
        h = 1
    elif int(a[len(a) - 1]) + int(b[len(b) - 1]) + h == 1:
        r = "1" + r
        h = 0
    elif int(a[len(a) - 1]) + int(b[len(b) - 1]) + h == 0:
        r = "0" + r
        h = 0
    a = a[:-1]
    b = b [:-1]

while a != "":
    if int(a[len(a) - 1]) + h == 3:
        r = "1" + r
        h = 1
    if int(a[len(a) - 1]) + h == 2:
        r = "0" + r
        h = 1
    elif int(a[len(a) - 1]) + h == 1:
        r = "1" + r
        h = 0
    elif int(a[len(a) - 1]) + h == 0:
        r = "0" + r
        h = 0
    a = a[:-1]

while b != "":
    if int(b[len(b) - 1]) + h == 3:
        r = "1" + r
        h = 1
    if int(b[len(b) - 1]) + h == 2:
        r = "0" + r
        h = 1
    elif int(b[len(b) - 1]) + h == 1:
        r = "1" + r
        h = 0
    elif int(b[len(b) - 1]) + h == 0:
        r = "0" + r
        h = 0
    b = b[:-1]

if h == 1:
    r = "1" + r
print(r)

