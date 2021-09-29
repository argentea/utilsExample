print("this is main.py")

from pyCode.pyAdd import pyAdd

a = pyAdd(10, 20)
print("python add")
print(a.add())

import build.pybindCmake as m 

b = m.Cadd(1, 3)
print(b.add())

