from survey import AnonymousSurvey

# 定义一个问题，并创建一个调查
question = '你说的第一种语言是什么'
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("输入q退出")
while True:
	response = input("语言：")
	if response == 'q':
		break
	my_survey.store_response(response)

print("\n感谢每个参与调查的人。")
my_survey.show_results()