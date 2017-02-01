"""
Це приклад невеликої програми для малювання кругів і квадратів.
Вам потрібно на основі цієї програми зробити невелику "танцювальну" сценку з
використанням кругів, квардратів і трикутників. Зробити все це потрібно в
об’єктно-орієнтованому стилі.

Які класи потрібно реалізувати:

- Багатокутник (на його основі зробити квадрат і правильний трикутник)
-- клас повинен вміти відрисовувати себе
-- переміщатися в деякому напряику заданому координатами x, y
-- збільшуватися (необов’язково)
-- повертатися (необов’язково)

- Квардрат (успадковується від багаткутника)
-- метод __init__ приймає координати середини, ширину і колір

- Трикутник (успадковується від багатокутника)
-- метод __init__ приймає координати середини, довжини сторони і колір

- Коло
-- метод __init__ приймає координати середини, радіус і колір
-- клас повинен вміти відрисовувати себе
-- преміщатися в деякому напрямку заданому координатами x, y
-- збільшуватися (необов’язково)

Також рекомендую створити додатковий клас Vector для представлення
точок на площині і різних операцій з ними - додавання, множення на число,
віднімання.


Із створених класів потрібно скласти якусь динамічну сцену.
"""

import turtle
import time
import random


class Polygon:
	'''Багатокутник.

	Містить функції для побудови, переміщення та збільшення для будь-яких багатокутників'''
	def __init__(self, num_sides, x, y, length, color):
		self.num_sides = num_sides
		self.x = x
		self.y = y
		self.length = length
		self.color = color

	#малює багатокутник
	def draw_polygon (self):
		ttl.penup() 
		ttl.setpos(self.x, self.y) 
		ttl.pendown() 
		ttl.color(self.color)
		angle = 360/self.num_sides        #кут на який повинна повернутись черепаха
	
		for i in range(self.num_sides):
			ttl.forward(self.length) 
			ttl.right(angle)
	
	#переміщує багатокутник на вказані позиції
	def move_polygon(self, q, r):
		self.x = q
		self.y = r
		self.draw_polygon

	#збільшує багатокутник на вказаний коефіцієнт
	def zoom(self, coef):
		self.coef = coef
		self.length = self.length * self.coef
		self.draw_polygon


class Square(Polygon):
	'''Квадрат.

	Наслідує функції для побудови, переміщення та збільшення квадрата. '''
	num_sides = 4
	def __init__(self, x, y, length, color):
		self.x = x
		self.y = y
		self.length = length
		self.color = color


class Triangle(Polygon):
	'''Рівносторонній трикутник.

	Наслідує функції для побудови, переміщення та збільшення трикутника. '''
	num_sides = 3
	def __init__(self, x, y, length, color):
		self.x = x
		self.y = y
		self.length = length
		self.color = color
		

class Circle:  
	'''Коло.

	Містить функції для побудови, переміщення та збільшення кола'''                               										
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
	# малює коло
	def draw_circle(self):
		ttl.penup() 
		ttl.setpos(self.x, self.y) 
		ttl.pendown() 
		ttl.color(self.color) 
		ttl.circle(self.radius) 
	#переміщує коло на вказані позиції
	def move_circle(self, q, r):
		self.x = q
		self.у = r
	#збільшує коло на вказаний коефіцієнт
	def zoom_circle(self, coef):
		self.coef = coef
		self.radius = self.radius * self.coef
		self.draw_circle

# Черепашка
turtle.tracer(0, 0) 
turtle.hideturtle() 

ttl = turtle.Turtle() 
ttl.hideturtle() 

# Динамічна сцена
def main():
	squa = Square(0,0,40,'red')
	circ = Circle(0,0,40,'green')
	triangle = Triangle(0,0,20,'blue')

	square_x = 0
	square_y = 0
	triangle_x = 0
	triangle_y = 0
	circle_x = 0
	circle_y = 0

	while True:
		time.sleep(0.5) 
		ttl.clear() 

		squa.draw_polygon()
		triangle.draw_polygon()
		circ.draw_circle()
		
		squa.move_polygon(square_x,square_y)
		triangle.move_polygon(triangle_x,triangle_y)
		circ.move_circle(circle_x, circle_y)

		circ.zoom_circle(random.randint(1,2))

		turtle.update() 
		
		square_x += random.randint(-40,40) 
		square_y += random.randint(-40,40)
		triangle_x += random.randint(-40,40)
		triangle_y += random.randint(-40,40)
		circle_x += random.randint(-10,10)
		circle_y += random.randint(-10,10)

if __name__ == '__main__':
    main()