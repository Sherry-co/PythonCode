# 模拟多次随机漫步 while循环
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    # plt.plot(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues, edgecolor='none', s=1)
    # 模拟花粉在水滴表明运动的路径
    plt.plot(rw.x_values, rw.y_values, linewidth=2)
    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
