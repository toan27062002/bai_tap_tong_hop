a = int(input('nhap a = '))
b = int(input('nhap b = '))

def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
print('UCLN cua',a,'va ',b,'la :',uscln(a,b))