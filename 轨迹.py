# import matplotlib.pyplot as plt
#
# # 轨迹数据
# x = [0, 1, 2, 3, 4, 5]  # X轴坐标
# y = [0, 2, 4, 3, 5, 2]  # Y轴坐标
#
# # 创建轨迹图
# plt.figure(figsize=(8, 6))  # 设置图像大小
# plt.plot(x, y, 'b-', linewidth=2, label='Trajectory')  # 绘制轨迹线
# plt.scatter(x, y, color='r', marker='o', label='Data Points')  # 绘制数据点
# plt.legend()  # 显示图例
# plt.title('Autonomous Driving Trajectory')  # 设置标题
# plt.xlabel('X-axis')  # 设置X轴标签
# plt.ylabel('Y-axis')  # 设置Y轴标签
# plt.grid(True)  # 显示网格线
#
# # 添加额外的绘图元素
# plt.annotate('Start', xy=(x[0], y[0]), xytext=(x[0] + 0.5, y[0] + 1),
#              arrowprops=dict(arrowstyle='->', color='g'), fontsize=10)  # 添加起点注释
# plt.annotate('End', xy=(x[-1], y[-1]), xytext=(x[-1] - 0.8, y[-1] - 1),
#              arrowprops=dict(arrowstyle='->', color='g'), fontsize=10)  # 添加终点注释
#
# # 显示轨迹图
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # 生成轨迹数据
# t = np.linspace(0, 10, 100)  # 时间序列
# x = np.cos(t) + np.random.normal(0, 0.1, size=len(t))  # X轴坐标
# y = np.sin(t) + np.random.normal(0, 0.1, size=len(t))  # Y轴坐标
#
# # 创建轨迹图
# plt.figure(figsize=(8, 6))
# plt.plot(x, y, 'b-', linewidth=2)
# plt.scatter(x, y, color='r', marker='o')
# plt.title('Autonomous Driving Trajectory')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
#
# # 显示轨迹图
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d
#
# # 原始轨迹数据
# t = np.linspace(0, 10, 100)
# x = np.cos(t) + np.random.normal(0, 0.1, size=len(t))
# y = np.sin(t) + np.random.normal(0, 0.1, size=len(t))
#
# # 创建插值函数
# f = interp1d(t, x, kind='cubic')
# g = interp1d(t, y, kind='cubic')
#
# # 生成平滑的轨迹数据
# t_smooth = np.linspace(0, 10, 1000)
# x_smooth = f(t_smooth)
# y_smooth = g(t_smooth)
#
# # 创建轨迹图
# plt.figure(figsize=(8, 6))
# plt.plot(x_smooth, y_smooth, 'b-', linewidth=2)
# plt.scatter(x, y, color='r', marker='o')
# plt.title('Smoothed Autonomous Driving Trajectory')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
#
# # 显示轨迹图
# plt.show()

# import matplotlib.pyplot as plt
#
#
# def generate_trajectory(start_position, target_position, duration, dt):
#     # 初始化轨迹
#     trajectory = [start_position]
#
#     # 计算运动轨迹
#     current_position = start_position
#     t = 0.0
#     while t < duration:
#         # 根据预测或规划算法计算下一个位置
#         # 这里仅作示例，可以根据实际需求替换为具体算法
#         # 假设简单地沿直线移动到目标位置
#         dx = (target_position[0] - current_position[0]) * dt / duration
#         dy = (target_position[1] - current_position[1]) * dt / duration
#         next_position = (current_position[0] + dx, current_position[1] + dy)
#
#         # 更新位置和时间
#         current_position = next_position
#         t += dt
#
#         # 添加到轨迹列表
#         trajectory.append(next_position)
#
#     return trajectory
#
#
# # 设置起始位置和目标位置
# start_position = (0, 0)
# target_position = (10, 10)
#
# # 生成轨迹
# duration = 5.0  # 运动持续时间
# dt = 0.1  # 时间步长
# trajectory = generate_trajectory(start_position, target_position, duration, dt)
#
# # 提取 x 和 y 坐标
# x = [pos[0] for pos in trajectory]
# y = [pos[1] for pos in trajectory]
#
# # 绘制轨迹图
# plt.plot(x, y)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Autonomous Driving Trajectory')
# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 生成随机数据点
x = np.linspace(0, 10, 20)
y = np.sin(x)

# 使用样条插值方法生成平滑曲线
x_new = np.linspace(0, 10, 100)
spl = make_interp_spline(x, y)
y_smooth = spl(x_new)

# 绘制原始数据点和平滑曲线
plt.plot(x, y, 'bo', label='原始数据')
plt.plot(x_new, y_smooth, 'r-', label='平滑曲线')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('平滑曲线示例')
plt.legend()
plt.grid(True)
plt.show()

