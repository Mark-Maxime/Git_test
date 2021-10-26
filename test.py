class A:
  def __init__(self,name,age):
    self.name=name
    self.age=age
# p1=A("Aung Aung","36")
# print(p1.name)
# print(p1.age)
  def myfunc(self):
    print("Hello Mr. ",self.name)
p1=A("Aung Aung", "33")
p1.myfunc()


class B:
  "Document Information"
print(B.__doc__)
help(B)

class C:
  "Python programming Apporach."
  def __init__(self,n):
    self.n=n
  def func(self):
    print("Name :", self.n)
a=C("Kyaw Kyaw")
a.func()

class D:
  def __init__(self):
    self.n="Maung Maung"
  def func(self):
    self.id="12345"
a1=D()
a1.func()
print(a1.__dict__)