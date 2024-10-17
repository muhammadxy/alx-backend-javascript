<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x01. Python - Async

This project contains some tasks for learning how to use and implement *`Async IO`*, and how to run *`concurrent coroutines`* in *Python* language.

<p align="center">
  <img width="500"
        src="https://i0.wp.com/blog.sqreen.com/wp-content/uploads/2018/02/asyncio@2x.jpg?resize=1024%2C390&ssl=1"
  >
</p>

# Getting Started :running:	
<div style="text-align: justify">

## Table of Contents
* [About](#about)
* [Resources](#resources-books)
* [Requirements](#requirements)
* [Files](#files-file_folder)
* [Tasks](#tasks)
* [Credits](#credits)

## About

- **[Async IO in Python: A Complete Walkthrough](https://intranet.hbtn.io/rltoken/JOCypbl0LYjr1ydVlzyLQQ)** 
- **[asyncio - Asynchronous I/O](https://intranet.hbtn.io/rltoken/P3UTFJncmPC4dB_vcNldDQ)** 
- **[random.uniform](https://intranet.hbtn.io/rltoken/DnVnLImtiAmHkSecFHsf7Q)** 
-  *` async `*  and  *` await `*  syntax
- How to execute an async program with  *` asyncio `* 
- How to run concurrent coroutines
- How to create  *` asyncio `*  tasks
- How to use the  *` random `*  module

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=python+concurrent+coroutines&oq=concurrent+coro&aqs=chrome.2.69i57j0i512j0i22i30l4j0i15i22i30.9365j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=Coroutine+Concurrency+in+Python+3+with+asyncio)

## Requirements
### General
* A  *` README.md `*  file, at the root of the folder of the project, is mandatory
* Allowed editors:  *` vi `* ,  *` vim `* ,  *` emacs `* 
* All files will be interpreted/compiled on Ubuntu 18.04 LTS using  *` python3 `*  (version 3.7)
* All files should end with a new line
* All files must be executable
* The length of files will be tested using  *` wc `* 
* The first line of all files should be exactly  *` #!/usr/bin/env python3 `* 
* The code should use the  *` pycodestyle `*  style (version 2.5.x)
* All functions and coroutines must be type-annotated.
* All modules should have a documentation ( *` python3 -c 'print(__import__("my_module").__doc__)' `* )
* All functions should have a documentation ( *` python3 -c 'print(__import__("my_module").my_function.__doc__)' `*
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method <br>
	(the length of it will be verified)

## More Info
### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-backend-python.git`	
- Access to directory: `cd 0x01-python_async_function`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

### Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. *`Provided by Holberton School`*.
		
---

## Tasks

+ [x] 0\. **The basics of async**

+ **[0-basic_async_syntax.py](./0-basic_async_syntax.py)**

Write an asynchronous coroutine that takes in an integer argument ( *` max_delay `* , with a default value of 10) named  *` wait_random `*  that waits for a random delay 
between 0 and  *` max_delay `* (included and float value) seconds and eventually returns it.

Use the   *` random `*   module.

```bash
$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769

```
---

+ [x] 1\. **Let's execute multiple coroutines at the same time with async**

+ **[1-concurrent_coroutines.py](./1-concurrent_coroutines.py)**

Import *` wait_random `* from the previous python file that you’ve written and write an async routine called *` wait_n `* that takes in 2 int arguments (in this order): 
*` n `*  and  *` max_delay `*. The spawn *` wait_random `*   *` n `*   times with the specified *` max_delay `*.

*` wait_n `* should return the list of all the delays (float values). The list of the delays should be in ascending order without using *` sort() `* because of concurrency.
```bash
$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 
4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

```
---

+ [x] 2\. **Measure the runtime**

+ **[2-measure_runtime.py](./2-measure_runtime.py)**

From the previous file, import   *` wait_n `*   into   *` 2-measure_runtime.py `*.
Create a *` measure_time `* function with integers *` n `* and *` max_delay `* as arguments that measures the total execution time for *` wait_n(n, max_delay) `*, and returns 
*` total_time / n `*.  The function should return a float.

Use the   *` time `*   module to measure an approximate elapsed time.

```bash
$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

$ ./2-main.py
1.759705400466919

```
---

+ [x] 3\. **Tasks**

+ **[3-tasks.py](./3-tasks.py)**

Import   *` wait_random `*   from   *` 0-basic_async_syntax `*.

Write a function (do not create an async function, use the regular function syntax to do this) *` task_wait_random `* that takes an integer *` max_delay `* 
and returns a *` asyncio.Task `*.

```bash
$ cat 3-main.py
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))

$ ./3-main.py
<class '_asyncio.Task'>

```
---

+ [x] 4\. **Tasks**

+ **[4-tasks.py](./4-tasks.py)**

Take the code from *` wait_n `* and alter it into a new function *` task_wait_n `*.  The code is nearly identical to *` wait_n `* except *` task_wait_random `* is being called.

```bash
$ cat 4-main.py
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))

$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]

```
---

## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Alex Orland Arévalo Tribaldos`**  and credits for `group projects` are displayed in the respective `README.md` files.

<3915@holbertonstudents.com>
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Alexoat76)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/aoarevalot)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/Alexoat76/)

## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).
![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)
