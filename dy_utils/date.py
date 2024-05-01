import datetime

# 给定时间戳
given_timestamp = 5374572

# 获取当前时间的时间戳
current_timestamp = datetime.datetime.now().timestamp()

# 计算时间差（以秒为单位）
time_difference_seconds = current_timestamp - given_timestamp

# 转换为适当的时间单位
time_difference = datetime.timedelta(seconds=time_difference_seconds)

print("给定时间戳距当前时间的时间差为:", time_difference)
