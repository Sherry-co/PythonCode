alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x_position: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] ==  'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#这个外星人的速度一定很快
	x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))
# 删除键值对
alien_1 ={'color': 'green','points': 5}
print(alien_1)
del alien_1['points']
print(alien_1)
