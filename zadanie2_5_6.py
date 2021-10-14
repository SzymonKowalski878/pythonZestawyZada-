class Calculator:
    def add(self,a,b):
        return a+b

    def difference(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b


class ScienceCalculator(Calculator):
    def pow(self,a,b):
        return pow(a,b)

t = ScienceCalculator()

print(t.add(1,2));
print(t.difference(1,2))
print(t.multiply(1,3))
print(t.divide(1,2))
print(t.pow(2,3))

