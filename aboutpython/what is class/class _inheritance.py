class Person:
		def __init__(self, name,age):
				self.name = name
				self.age = age

		def eat(self):
				print('{}은 {}를 먹습니다.'. format(self.name, food))
		
		def sleep(self, minute):
				print('{}은 {}분동안 잡니다.'. format(self.name, minute))

		def work(self, minute):
				print('{}은 {}분동안 준비를 합니다.'. format(self.name, minute))

class Student(Person):
		def __init__(self,name,age):
				self.name = name
				self.age = age
		def work(self, minute):
				super().work(minute) # 부모 클래스의 기능을 사용한다.
				print('{}은 {}분동안 공부를 합니다.'. format(self.name, minute))
				# -> 결과를 확인해보면, 부모 클래스도 이행하면서 자식 클래스의 기능도 이행한다.

class Employee(Person): # Person에서 상속받는 것이다.
		def __init__(self, name, age):
				self.name = name
				self.age = age

		def work(self, minute):
				print('{}은 {}분동안 축구를 합니다.'. format(self.name, minute))

# 오버라이딩 개념
Mount = Employee('Mount', 27)
Mount.eat('pizza')
Mount.work(60)

'''if 부모 클래스의 기능이 필요하다고하면?
-> 오버라이딩을 하면 부모 클래스의 기능이 사라진다. 부모 클래스의 기능을 일부 사용하고 싶다면?
super를 이용하자.
'''
