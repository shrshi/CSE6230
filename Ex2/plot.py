import matplotlib.pyplot as plt

bandwidth = [10280.353, 11009.174, 10672.358, 5445.943, 5398.171, 5400.236, 5321.330, 3449.514]
num = [2,3,4,5,6,7,8,9]

plt.plot(num, bandwidth, 'r-', label='bandwidth per thread')
plt.plot(num, [102400]*8, 'b-', label='peak theoretical bandwidth')
plt.xlabel('Number of threads')
plt.ylabel('Bandwidth (MB/sec)')
plt.legend(loc='upper right')
plt.title('Plot of bandwidth vs number of threads')

plt.show()

