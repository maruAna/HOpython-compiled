# file: prueba.py
import ctypes as C
math = C.CDLL('./milibreria.so')

print "*********************************************"
print "                add_two.c"
print "*********************************************"

#suma de enteros
print "---------suma int--------"
#math.add_int.argtypes(C.c_int, C.c_int)
math.add_int.restypes = C.c_int
a=5
b=10
resultEntero = math.add_int(a, b)
print "Resultado: ", resultEntero
print "---------suma int--------"

print "\n"

#suma de float
print"------------suma float---------------"
math.add_float.argtypes = (C.c_float, C.c_float)
math.add_float.restype = C.c_float
c = 5.9
d = 7.5
resultFloat = math.add_float(c, d)
print "Resultado: ", resultFloat
print"------------suma float---------------"                          

print "\n"

#suma por referencia (int)
print "----------suma por ref int ---------------"
math.add_int_ref.argtypes = (C.POINTER(C.c_int), C.POINTER(C.c_int), C.POINTER(C.c_int))
math.add_int_ref.restype = C.c_int
e= 5
f= 7
resultRefInt =C.c_int(0)
math.add_int_ref(C.byref( C.c_int(e)), C.byref(C.c_int(f)), C.byref(resultRefInt))
print "Resultado: ", resultRefInt
print"------------suma por ref int---------------"   

print "\n"

#suma por referencia (float)
print "----------suma por ref float ---------------"
math.add_float_ref.argtypes = (C.POINTER(C.c_float), C.POINTER(C.c_float), C.POINTER(C.c_float))
math.add_float_ref.restype = C.c_float
g= 5.5
h= 7.7
resultRefFloat = C.c_float(0)
math.add_float_ref(C.byref(C.c_float(g)), C.byref(C.c_float(h)), C.byref(resultRefFloat))
print "Resultado: ", resultRefFloat
print"------------suma por ref float---------------"   

print "\n"

print "*********************************************"
print "                arrays.c"
print "*********************************************"
print "\n"

#suma de vectores (int)
print "-----------suma de vectores int-----------"
math.add_int_array.restype = C.c_int
tam = 4
arre1 = (C.c_int * tam)(1,2,3,4)
arre2 = (C.c_int * tam)(5,6,7,8)
arreResul = (C.c_int * tam)(0,0,0,0)

math.add_int_array(C.byref(arre1), C.byref(arre2), C.byref(arreResul), C.c_int(tam))
print "arreResul: ", [x for x in arreResul]
print "-----------suma de vectores int-----------"

print "\n"

#producto de vectores (float)
print "-----------producto de vectores float-----------"
math.dot_product.restype = C.c_float
tam = 4
arre1 = (C.c_float * tam)(1,2,3,4)
arre2 = (C.c_float * tam)(5,6,7,8)

result = math.dot_product(C.byref(arre1), C.byref(arre2), C.c_int(tam))
print "Resultado: ", result
print "-----------producto de vectores-----------"