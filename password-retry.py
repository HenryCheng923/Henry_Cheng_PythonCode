#練習密碼判斷程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入3次
#如果正確 就印出"登入成功!"
#如果不正確 就印出 "密碼錯誤! 還有__次機會!"


password = 'a123456'
count_pwds = 3
pwd = input('請輸入密碼： ')
#pwd = int(pwd)
while count_pwds > 0:

	if pwd == password:
		print('登入成功!')
		break
	elif pwd != password and count_pwds > 1:
		count_pwds = count_pwds - 1 
		print("密碼錯誤! 還有",count_pwds,"次機會")
		pwd = input('請輸入密碼： ')
	else:
		print('已錯誤三次無法登入!')
		break	
		