#BMI值計算公式
#BMI值計算公式:    BMI = 體重(公斤) / 身高2(公尺2)

weight = input("請輸入您的體重：")
height = input("請輸入您的身高：")
weight = int(weight)
height = int(height) / 100 # 換成公尺
bmi = (weight / (height ** 2))
print("您的BMI數值為：", bmi)

if bmi < 18.5 : 
	print("體重過輕")
elif bmi >= 18.5 and bmi < 24:
	print("正常範圍")
elif bmi >= 24 and bmi < 27:
	print("過重")
elif bmi >=27 and bmi < 30:
	print("輕度肥胖")
elif bmi >=30 and bmi < 35:
	print("中度肥胖")
else:
	print("重度肥胖") 

