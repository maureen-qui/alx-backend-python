<<<<<<< HEAD
Toggle navigation
Curriculum
Short Specializations
Average: 64.39%
We're moving to Discord!
In a few days, we will be leaving Slack in favor of Discord 🎉
Click here for more information
0x02. Python - Async Comprehension
=======

Curriculum
Short Specializations
Average: 72.44%
We're moving to Discord!
In a few days, we will be leaving Slack in favor of Discord 🎉
Click here for more information
0x01. Python - Async
>>>>>>> d560a4ad4fbdbfdf5c882f32ccaa9f423b67d395
Python
Back-end
 By: Emmanuel Turlay, Staff Software Engineer at Cruise
 Weight: 1
<<<<<<< HEAD
 Project will start Oct 9, 2023 6:00 AM, must end by Oct 12, 2023 6:00 AM
 Checker was released at Oct 10, 2023 12:00 AM
=======
 Project will start Oct 9, 2023 6:00 AM, must end by Oct 10, 2023 6:00 AM
 Checker was released at Oct 9, 2023 12:00 PM
>>>>>>> d560a4ad4fbdbfdf5c882f32ccaa9f423b67d395
 An auto review will be launched at the deadline


Resources
Read or watch:

<<<<<<< HEAD
PEP 530 – Asynchronous Comprehensions
What’s New in Python: Asynchronous Comprehensions / Generators
Type-hints for generators
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

How to write an asynchronous generator
How to use async comprehensions
How to type-annotate generators
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5.x)
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
All your functions and coroutines must be type-annotated.
Tasks
0. Async Generator
mandatory
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.
=======
Async IO in Python: A Complete Walkthrough
asyncio - Asynchronous I/O
random.uniform
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

async and await syntax
How to execute an async program with asyncio
How to run concurrent coroutines
How to create asyncio tasks
How to use the random module
Requirements
General
A README.md file, at the root of the folder of the project, is mandatory
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
All your files must be executable
The length of your files will be tested using wc
The first line of all your files should be exactly #!/usr/bin/env python3
Your code should use the pycodestyle style (version 2.5.x)
All your functions and coroutines must be type-annotated.
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Tasks
0. The basics of async
mandatory
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Use the random module.
>>>>>>> d560a4ad4fbdbfdf5c882f32ccaa9f423b67d395

bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

<<<<<<< HEAD
async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

bob@dylan:~$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206, 1.0067279479988345, 1.3783306401737838]
Repo:

GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
File: 0-async_generator.py
   
1. Async Comprehensions
mandatory
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())

bob@dylan:~$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916, 7.713335177885325, 7.673533267041574]
=======
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 0-basic_async_syntax.py
   
1. Let's execute multiple coroutines at the same time with async
mandatory
Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.

bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
The output for your answers might look a little different and that’s okay.
>>>>>>> d560a4ad4fbdbfdf5c882f32ccaa9f423b67d395

Repo:

GitHub repository: alx-backend-python
<<<<<<< HEAD
Directory: 0x02-python_async_comprehension
File: 1-async_comprehension.py
   
2. Run time for four parallel comprehensions
mandatory
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
=======
Directory: 0x01-python_async_function
File: 1-concurrent_coroutines.py
   
2. Measure the runtime
mandatory
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
>>>>>>> d560a4ad4fbdbfdf5c882f32ccaa9f423b67d395

bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

<<<<<<< HEAD
import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

bob@dylan:~$ ./2-main.py
10.021936893463135

Repo:

GitHub repository: alx-backend-python
Directory: 0x02-python_async_comprehension
File: 2-measure_runtime.py
=======
measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 2-measure_runtime.py
   
3. Tasks
mandatory
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.

bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

bob@dylan:~$ ./3-main.py
<class '_asyncio.Task'>
Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 3-tasks.py
   
4. Tasks
mandatory
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.

bob@dylan:~$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

bob@dylan:~$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
Repo:

GitHub repository: alx-backend-python
Directory: 0x01-python_async_function
File: 4-tasks.py
>>>>>>> d560a4ad4fbdbfdf5c882f32ccaa9f423b67d395
   
Copyright © 2023 ALX, All rights reserved.
