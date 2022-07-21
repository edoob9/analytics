class Counter:
		def __init__(self):
				self.num = 0

		def increment(self): # 1씩 증가시키는 함수 
				self.num += 1
		def reset(self): # 초기화
				self.num = 0
		def print_current_value(self):
				print('현재값은', self.num)

c1 = Counter()
c1.print_current_value()
c1.increment()
c1.increment()
c1.print_current_value()

c1.reset()
c1.print_current_value()

# ---------------------------
# Method type
class Math:
		# (아래처럼 속성이 없는 클래스 = self가 할게 없다)
		# 인스턴스 레벨의 내부적으로 유지할 데이터가 없다 - 전달된 데이터를 처리만 해서 반환만 하면되는 클래스
		@staticmethod
		def add(a,b):
				return a+b
		@staticmethod # 인스턴스 메소드가 아니기 때문에 static하게 동작하기 때문에 클래스 이름을 이용해서 사용할 수 있다. -> How?
		def multiply(a,b):
				return a*b

# m = Math() -> 필요가 없다.
# m.add(10,20)
Math.add(10,20)
