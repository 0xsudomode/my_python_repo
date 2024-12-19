#!/usr/bin/env python3

class bankAccount():
	def __init__(self,credit = 0):
		self.credit = credit
		print(f'initial credit {credit}')

	def deposit(self,amount):
		self.credit = amount
		print(f'user has deposit {amount}$')

	def withdraw(self,amount):
		self.credit -= amount
		print(f'user has widthdraw {amount}$')

	def balance(self):
		print(f'current user credit {self.credit}$')


user1 = bankAccount()
user1.deposit(1000)
user1.withdraw(300)
user1.balance()
