import time, sys, os
w = ("add","sub","mult","div","divn")

set_LANG = ("Wrong number\n",\
	"Language selected\n",\
	"언어가 설정 되었습니다\n",\
	"言語が設定されてい\n","")
'''
			# 모든 원소가 0인 5x5리스트 생성
			Matrix = [[0]*5 for i in range(5)]

			# 인덱스로 접근해서 값 변경
			Matrix[0][0] = 1
			Matrix[4][0] = 5

			#출력
			print Matrix[0][0] # prints 1
			print Matrix[4][0] # prints 5
'''
# setAsk_KOR[0] = Header
setAsk_LANG = [
	["\n\tCALCULATOR 1.2.2 계산기입니다.",\
		"\n\tThis is CALCULATOR 1.1.2",\
		"\n\tCALCULATOR 1.2.2 計算機です."],\
	["다음을 입력해 주세요",	"Enter Number",	"数字を入力してください"],\
	["첫번째 숫자:",		"First number:", 	"最初の数字:"],\
	["두번째 숫자:", 	"Second number",	"第二の数字:"],\
	["계산법 (더하기=1,빼기=2,곱하기=3,나누기(소수)=4,나누기=5):",\
		"Calculation (add=1,sub=2,mult=3,div(float)=4,div=5):",\
		"計算 (プラス=1,マイナス=2,乗算=3,除算(小数)=4,除算=5):"],\
	["답은",	"Answer is", "答えは"],\
	["입니다", " ...", "です"],\
	["잘못된 숫자입니다", "Wrong Number", "誤った数字です"],\
]

print(setAsk_LANG[4][2])

'''
def chooLANG():
	global lang; 	lang = 4
	while lang > 3 or lang == 0:
		print("Please select language")
		lang = (int(input("English=1, 한국어=2 日本語=3 : ")))

		if lang >= 1 and lang <=3 :		print(set_LANG[lang])
		else:
			print(set_LANG[0])		# wrong message = 0
			time.sleep(2)
			os.system('cls')

			chooLANG()

def add(a,b):
	re = a + b
	print(a,"+",b,"=",re)
	return re

def sub(a,b):
	re = a - b
	print(a,"-",b,"=",re)
	return re

def mult(a,b):
	re = a * b
	print(a,"*",b,"=",re)
	return re

def div(a,b):
	re = a / b
	print(a,"/",b,"=",re)
	return re

def divn(a,b):
	re = a // b
	print(a,"//",b,"=",re)
	return re

def ask_KOR():
	global a,b,c
	if lang is 2:
		print (setAsk_KOR[0])			# "\n\tCALCULATOR 1.2.2 계산기입니다."
		print ("\n","-"*60)
		print (setAsk_KOR[1])			# "다음을 입력해 주세요"

		a = (int(input(setAsk_KOR[2])))	# "첫번째 숫자:",\
		b = (int(input(setAsk_KOR[3])))	# "두번째 숫자:",\
		c = (int(input(setAsk_KOR[4])))	# ""계산법 (더하기=1,빼기=2,곱하기=3,나누기(소수)=4,나누기=5):"\

def run_KOR():
	if c >= 1 and c <=5 :	print(setAsk_KOR[c],add(a,b),setAsk_KOR[c]) # 답은~, 입니다.
	else:
		print(setAsk_KOR[7])	# 잘못된 숫자입니다 = setAsk_KOR[7]
		ask_KOR()


def main():
	chooLANG()
	if lang == 1:
		ask_ENG()
		run_ENG()

	elif lang == 2:
		ask_KOR()
		run_KOR()

	elif lang == 3:
		ask_JAP()
		run_JAP()

main()
'''
