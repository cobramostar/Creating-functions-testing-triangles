
# https://edube.org/learn/pe-1/creating-functions-testing-triangles-3

# 4.5.1.4 Kreiranje funkcija | ispitivanje trokuta

# 4.5.1.4 Creating functions | testing triangles

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b and a>0 and b>0 and c>0
    
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    list_2 = [a ,b ,c]
    list_2.sort()
    return list_2[-1] ** 2 == list_2[0] ** 2 + list_2[1] ** 2


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
    if is_a_right_triangle(a, b, c):
        print('Yes, it can be a right triangle.')
    else:
        print('No, it can\'t be a right triangle.')
else:
    print('No, it can\'t be a triangle.')
