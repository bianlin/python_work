import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	# 创建一个RandomWalk实例
	rw = RandomWalk()
	rw.fill_walk()
	# 将所有点都绘制出来
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(10, 6))
	point_numbers = range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, linewidth=3)

	plt.show()

	keep_running = input("Make another walk? (y/n):")
	if keep_running == 'n':
		break