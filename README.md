<h1>Python Performance Benchmarking with Parallelization</h1>
<br>
This project evaluates the performance of different Python implementations (CPython, PyPy, and Jython) by measuring processing speed and analyzing the impact of parallelization on algorithm execution. The tasks involve comparing execution times of these implementations for calculating factorials and evaluating the effects of parallelizing the algorithm.

<h2>Project Overview</h2>
This project aims to answer two main objectives:

<h3>Comparison of Python Implementations:</h3>
Evaluate the performance of different Python implementations (CPython, PyPy, Jython) by calculating factorials of large numbers and measuring their execution times.
<h3>Impact of Parallelization:</h3>
Implement a factorial algorithm both serially and in parallel, using the multiprocessing module.
Measure and compare the execution times of the serial and parallelized versions of the algorithm to analyze the impact of parallelization on processing speed.
<br>
<h2>Files</h2>
<br>

- `serial_fact.py`: Contains the implementation of the serial version of the factorial calculation.  
- `parallel_fact.py`: Contains the parallelized version of the factorial calculation using the `multiprocessing` module.  
- `benchmark.py`: A benchmarking script used to measure the execution times of the different implementations and algorithms.  
- `requirements.txt`: A file listing the Python dependencies required for the project.  
- `README.md`: This file.  

<h2>Results</h2>
The performance of the different Python implementations and the factorial algorithms (serial vs parallel) will be displayed in terms of execution time. You can observe how parallelization and the choice of implementation impact the overall performance.

- Serial execution completed in 97.237 seconds.
- Parallel execution completed in 14.706 seconds.

<h2>Scalability Analysis</h2>
This project also includes an analysis of the scalability of the factorial algorithm with respect to Big O notation, both for the serial and parallel implementations. It evaluates how the algorithm's performance changes with increasing problem size and how parallelization affects its scalability.
