Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
f=open('D:/pythonclass/tet.stl')
a=f.readlines()
for x in a:
    if 'vertex' in x
    
SyntaxError: expected ':'
for x in a:
    if 'vertex' in x:
        print(x)

        
      vertex 0.0 0.0 0.0

      vertex 1.0 0.0 0.0

      vertex 0.0 0.0 1.0

      vertex 0.0 0.0 0.0

      vertex 0.0 1.0 0.0

      vertex 1.0 0.0 0.0

      vertex 0.0 0.0 0.0

      vertex 0.0 0.0 1.0

      vertex 0.0 1.0 0.0

      vertex 1.0 0.0 0.0

      vertex 0.0 1.0 0.0

      vertex 0.0 0.0 1.0

for x in a:
    if 'vertex' in x:
        print(x)
        b=x.split()

        
      vertex 0.0 0.0 0.0

      vertex 1.0 0.0 0.0

      vertex 0.0 0.0 1.0

      vertex 0.0 0.0 0.0

      vertex 0.0 1.0 0.0

      vertex 1.0 0.0 0.0

      vertex 0.0 0.0 0.0

      vertex 0.0 0.0 1.0

      vertex 0.0 1.0 0.0

      vertex 1.0 0.0 0.0

      vertex 0.0 1.0 0.0

      vertex 0.0 0.0 1.0

for x in a:
    if 'vertex' in x:
        
        b=x.split()
        b

        
['vertex', '0.0', '0.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
['vertex', '0.0', '0.0', '0.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
for x in a:
    if 'vertex' in x:

        b=x.split()
        print(b)

        
['vertex', '0.0', '0.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
['vertex', '0.0', '0.0', '0.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
for x in a:
    if 'vertex' in x:

        b=x.split()
        print(b)
        h=b[1:]
        d=[float(e) for e in b]
        d

        
['vertex', '0.0', '0.0', '0.0']
Traceback (most recent call last):
  File "<pyshell#20>", line 7, in <module>
    d=[float(e) for e in b]
ValueError: could not convert string to float: 'vertex'
for x in a:
    if 'vertex' in x:

        b=x.split()
        print(b)
        h=b[1:]
        d=[float(e) for e in h]

        
['vertex', '0.0', '0.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
['vertex', '0.0', '0.0', '0.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '1.0', '0.0', '0.0']
['vertex', '0.0', '1.0', '0.0']
['vertex', '0.0', '0.0', '1.0']
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        print(d)

        
[0.0, 0.0, 0.0]
[1.0, 0.0, 0.0]
[0.0, 0.0, 1.0]
[0.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[1.0, 0.0, 0.0]
[0.0, 0.0, 0.0]
[0.0, 0.0, 1.0]
[0.0, 1.0, 0.0]
[1.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[0.0, 0.0, 1.0]
z=[]
y=z.append(d)


print(y)
None

for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        print(d)

        
[0.0, 0.0, 0.0]
[1.0, 0.0, 0.0]
[0.0, 0.0, 1.0]
[0.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[1.0, 0.0, 0.0]
[0.0, 0.0, 0.0]
[0.0, 0.0, 1.0]
[0.0, 1.0, 0.0]
[1.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[0.0, 0.0, 1.0]

f=[]
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)

        
f
[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
len(f)
12
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)

        
len(f)
24
f=[]
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)

        
def dist(point1,point2):
    d=((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**.5
    return d

def dist(point1,point2):
    d=((point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2)**.5
    return d

def area(side1,side2,side3)
SyntaxError: expected ':'
def area(side1,side2,side3):
    s=(side1+side2+side3)/2
    A=(s*(s-side1)*(s-side2)*(s-side3))**.5
    return A

for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)

            

f=[]
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)
            f.clear()

            
f
[]
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)
            f.clear()
    

        
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)
            f.clear()

            
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)
            f.clear()
    else:
        print('skipped')

        
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
skipped
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)
            f.clear()
        else:
            print('innerskipped')
    else:
        print('skipped')

    
skipped
skipped
skipped
innerskipped
innerskipped
skipped
skipped
skipped
skipped
innerskipped
innerskipped
skipped
skipped
skipped
skipped
innerskipped
innerskipped
skipped
skipped
skipped
skipped
innerskipped
innerskipped
skipped
skipped
skipped
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)
            f.clear()
        else:
            print('innerskipped')
        m=27
        print(m)
    else:
        print('skipped')
    n=90
    print(n)for x in a:
        if 'vertex' in x:

            b=x.split()
            h=b[1:]
            d=[float(e) for e in h]
            f.append(d)
            if len(f)==3:
                P1,P2,P3=f
                side1=dist(P1,P2)
                side2=dist(P2,P3)
                side3=dist(P3,P1)
                trianglearea=area(side2,side1,side3)
                f.clear()
                
SyntaxError: invalid syntax

totalarea=0
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)
            f.clear()
            totalarea=totalarea+trianglearea

            
totalarea
2.3660254037844384
f
[]
for x in a:
    if 'vertex' in x:

        b=x.split()
        h=b[1:]
        d=[float(e) for e in h]
        f.append(d)
        if len(f)==3:
            P1,P2,P3=f
            side1=dist(P1,P2)
            side2=dist(P2,P3)
            side3=dist(P3,P1)
            trianglearea=area(side2,side1,side3)
            f.clear()
        else:
            print('innerskipped')
        m=27
        print(m)
    else:
        print('skipped')
    n=90
    print(n)

    
skipped
90
skipped
90
skipped
90
innerskipped
27
90
innerskipped
27
90
27
90
skipped
90
skipped
90
skipped
90
skipped
90
innerskipped
27
90
innerskipped
27
90
27
90
skipped
90
skipped
90
skipped
90
skipped
90
innerskipped
27
90
innerskipped
27
90
27
90
skipped
90
skipped
90
skipped
90
skipped
90
innerskipped
27
90
innerskipped
27
90
27
90
skipped
90
skipped
90
skipped
90
>>> def dist(point1,point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    d=((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**.5
    d=((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**.5
