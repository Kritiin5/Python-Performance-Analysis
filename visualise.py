import matplotlib.pyplot as plt

implementations = ['CPython', 'PyPy', 'Jython']
execution_times = [0.0033, 0.0009, 0.0532]  

plt.bar(implementations, execution_times, color=['blue', 'green', 'orange'])
plt.xlabel('Python Implementations')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison of Python Implementations')
plt.show()
