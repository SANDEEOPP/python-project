# Assignment
# print ODD in descending order
r=[]
def print_odd_desc(*a):
    for n1 in a:
        if n1%2!=0:
          r.print(n1) 
    r.sort()
    r.reverse()
    print(r)
print_odd_desc(1,2,33,5,7,6)
print_odd_desc(1,2,33,6,7,8,9,51,12,99)