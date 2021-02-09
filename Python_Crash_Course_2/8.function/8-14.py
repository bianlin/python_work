def make_car(carmaker, model, **carInfo):
	"""包含一辆车的信息"""
	carInfo['carmaker'] = carmaker
	carInfo['model'] = model
	return carInfo

carInfo = make_car('subaru', 'outback', color='blue', tow_package=True)

print(carInfo)