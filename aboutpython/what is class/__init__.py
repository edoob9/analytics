# <방법1>
# 값을 바꿀 수는 있다.
class Person:
		def __init__(self):
				print(self, 'is generated')
				# Person이라는 타입이 가지는 속성이 2가지가 있고, 속성은 name,age이다.
				self.name = 'Kate'
				self.age = 31

p1 = Person()
p2 = Person()

p1.name = 'maddison'
p1.age = 28
print(p1.name, p1.age)
# ----------------------------------------------

# <방법2> 
# 객체를 생성함과 동시에 바로 속성값을 할당
class Person:
		def __init__(self, name, age): # default 파라미터 값 설정 가능하다. How? age=10이런 형식으로
				print(self, 'is generated')
				# Person이라는 타입이 가지는 속성이 2가지가 있고, 속성은 name,age이다.
				self.name = name
				self.age = age
				# 이름이 self일 필요는 없지만 위치는 항상 맨 처음의 parameter이며 관례적으로 self사용

# 객체 2개를 생성한다
p1 = Person('Mount', 22)
p2 = Person('James', 24)
# 값이 신기하게 나올 것이다. 0x10787... => 객체가 현재 상주하고 있는 메모리 주소로 p1,p2의 저장공간이 다르기 때문에 다른 값이 출력된다.
