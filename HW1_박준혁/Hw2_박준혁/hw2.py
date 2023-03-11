name = 'My name is junhyeok'

len(name)
for i in range(9) : 
    print("My name is junhyeok")
print(name[0])
print(name[:4])
print(name[-4:])


outStr = ""
count, i = 0, 0

name = 'My name is junhyeok'
count  = len(name)
for i in range(0, count) :
    outStr += name[count - (i+1)]
print(outStr)

print(name[1:count-1])

print(name.upper())
print(name.lower())
print(name.replace('a', 'e'))
print("Hello")