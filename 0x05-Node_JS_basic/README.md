<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/JavaScript-yellow.svg"/>
<img src="https://img.shields.io/badge/NodeJS-gold.svg"/>
<img src="https://img.shields.io/badge/Express-darkslategray.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---

# 0x05. NodeJS Basics

This project contains some tasks for learning how to use and implement *` JavaScript `*  using **` NodeJS `**. Use the *` NodeJS `* modules for read files and create ` HTTP server `, and create advanced routes with *`Express JS`*.
<p align="center">
  <img width="300"  
        src="https://www.logigroup.com/images/modules/technologies/framework/nodejs.gif"
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

This project contains some tasks for learning how to use and implement *` JavaScript `*  using **` NodeJS `**.
* use *` NodeJS modules `*
* use specific Node JS module to read files
* use  **` process `**  to access command line arguments and the environment
* create a small *` HTTP server `* using *` Node JS `*
* create a small *` HTTP server `* using *` Express JS `*
* create advanced routes with *` Express JS `*
* use ES6 with Node JS with **` Babel-node  `**
* use **` Nodemon `** to develop faster

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=node+js&oq=node+&aqs=chrome.1.69i57j0i512l2j69i59j0i512l6.4230j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=node+js+basic)

- **[Node JS getting started](https://intranet.hbtn.io/rltoken/DcP3Mvp4st08_8RGxT11Ig)** 
- **[Process API doc](https://intranet.hbtn.io/rltoken/xdZZgCUIj8kqQzMHDMpLkA)** 
- **[Child process](https://intranet.hbtn.io/rltoken/2FSssvsPuFlCWJqz8acWNA)** 
- **[Express getting started](https://intranet.hbtn.io/rltoken/U4UHPnPu2Vq6cVOxIUQbpg)** 
- **[Mocha documentation](https://intranet.hbtn.io/rltoken/jkRkBlp2AU51K07YQFQoPg)** 
- **[Nodemon documentation](https://intranet.hbtn.io/rltoken/KYwR79CwgDACz7QhtbpTZg)** 

## Requirements
### General
- Allowed editors: *` vi `*, *` vim `*, *` emacs `* ,  *` Visual Studio Code `*  
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using  *` node `*  (version 12.x.x)
- All files should end with a new line
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code use the  *` js `*  extension
- The code will be tested using  *` Jest `*  and the command  **` npm run test `** 
- The code will be verified against lint using ESLint
- The code needs to pass all the tests and lint. Verify the entire project running  *` npm run full-test `* 
- All the functions/classes must be exported by using this format:  *` module.exports = myFunction; `*

## More Info
## Configuration files
Use these files for the following tasks

### database.csv
```bash
firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS
```

<details>
  <summary><h3>package.json :floppy_disk:</h3></summary>

```javascript
{
  "name": "node_js_basics",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "test": "./node_modules/mocha/bin/mocha --require babel-register --exit",
    "dev": "nodemon --exec babel-node --presets babel-preset-env ./server.js ./database.csv"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1"
  },
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "nodemon": "^2.0.2",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}

```
</details>

<details>
  <summary><h3>babel.config.js :floppy_disk:</h3></summary>

```javascript
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};

```
</details>

<details>
  <summary><h3>.eslintrc.js :floppy_disk:</h3></summary>

```javascript

module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};

```
</details>

---

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-backend-javascript.git`	
- Access to directory: `cd 0x05-Node_JS_basic`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

### Tests :heavy_check_mark:

+ **[tests](./tests)**: Folder of test files. *`Provided by Holberton School`*.
		
---

## Tasks

+ [x] 0\. **Executing basic javascript with Node JS**

+ **[0-console.js](./0-console.js)**

In the file  *` 0-console.js `*, create a function named  *` displayMessage `*   that prints in   *` STDOUT `*   the string argument.

```javascript

const displayMessage = require('./0-console');

displayMessage("Hello NodeJS!");

```
```bash
$ node 0-main.js
Hello NodeJS!
$

```
---
+ [x] 1\. **Using Process stdin**

+ **[1-stdin.js](./1-stdin.js)**

Create a program named   *` 1-stdin.js `*   that will be executed through command line:
* It should display the message  *` Welcome to Holberton School, what is your name? `*  (followed by a new line)
* The user should be able to input their name on a new line
* The program should display  *` Your name is: INPUT `* 
* When the user ends the program, it should display  *` This important software is now closing `*  (followed by a new line)

Requirements:
* Your code will be tested through a child process, make sure you have everything you need for that

```bash
$ node 1-stdin.js 
Welcome to Holberton School, what is your name?
Bob
Your name is: Bob
$ 
$ echo "John" | node 1-stdin.js 
Welcome to Holberton School, what is your name?
Your name is: John
This important software is now closing
$ 

```
---

+ [x] 2\. **Reading a file synchronously with Node JS**

+ **[2-read_file.js](./2-read_file.js)**

Using the database   *` database.csv `*   (provided in project description), create a function   *` countStudents `*   in the file   *` 2-read_file.js `* 
* Create a function named  *` countStudents `* . It should accept a path in argument
* The script should attempt to read the database file synchronously
* If the database is not available, it should throw an error with the text  *` Cannot load the database `* 
* If the database is available, it should log the following message to the console  *` Number of students: NUMBER_OF_STUDENTS `* 
* It should log the number of students in each field, and the list with the following format:  *` Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES `* 
* CSV file can contain empty lines (at the end) - and they are not a valid student!

```javascript
const countStudents = require('./2-read_file');

countStudents("nope.csv");

```
```bash
$ node 2-main_0.js
2-read_file.js:9
    throw new Error('Cannot load the database');
    ^

Error: Cannot load the database
...
$
$ cat 2-main_1.js
const countStudents = require('./2-read_file');

countStudents("database.csv");

$ node 2-main_1.js
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
$ 

```
---

+ [x] 3\. **Reading a file asynchronously with Node JS**

+ **[3-read_file_async.js](./3-read_file_async.js)**

Using the database   *` database.csv `*   (provided in project description), create a function   *` countStudents `*   in the file   *` 3-read_file_async.js `* 
* Create a function named  *` countStudents `* . It should accept a path in argument (same as in  *` 2-read_file.js `* )
* The script should attempt to read the database file asynchronously
* The function should return a Promise
* If the database is not available, it should throw an error with the text  *` Cannot load the database `* 
* If the database is available, it should log the following message to the console  *` Number of students: NUMBER_OF_STUDENTS `* 
* It should log the number of students in each field, and the list with the following format:  *` Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES `* 
* CSV file can contain empty lines (at the end) - and they are not a valid student!

```javascript
const countStudents = require('./3-read_file_async');

countStudents("nope.csv")
    .then(() => {
        console.log("Done!");
    })
        .catch((error) => {
        console.log(error);
    });

```
```bash
$ node 3-main_0.js
Error: Cannot load the database
...
$
```
```javascript

const countStudents = require('./3-read_file_async');

countStudents("database.csv")
    .then(() => {
        console.log("Done!");
    })
        .catch((error) => {
        console.log(error);
    });
console.log("After!");

```
```bash
$ node 3-main_1.js
After!
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Done!
$ 

```

**Tips**:
* Using asynchronous callbacks is the preferred way to write code in Node to avoid blocking threads

---

+ [x] 4\. **Create a small HTTP server using Node's HTTP module**

+ **[4-http.js](./4-http.js)**

In a file named   *` 4-http.js `*  , create a small HTTP server using the   *` http `*   module:
* It should be assigned to the variable  *` app `*  and this one must be exported 
* HTTP server should listen on port 1245
* Displays  *` Hello Holberton School! `*  in the page body for any endpoint as plain text

In terminal 1:
```bash
$ node 4-http.js
...
```

In terminal 2:

```bash
$ curl localhost:1245 && echo ""
Hello Holberton School!
$ 
$ curl localhost:1245/any_endpoint && echo ""
Hello Holberton School!
$ 

```
---

+ [x] 5\. **Create a more complex HTTP server using Node's HTTP module**

+ **[5-http.js](./5-http.js)**

In a file named   *` 5-http.js `*  , create a small HTTP server using the   *` http `*   module:
* It should be assigned to the variable app and this one must be exported
* HTTP server should listen on port 1245
* It should return plain text
* When the URL path is  *` / `* , it should display  *` Hello Holberton School! `*  in the page body
* When the URL path is  *` /students `* , it should display  *` This is the list of our students `*   followed by the same content as the file <br>  *` 3-read_file_async.js `*  (with and without the database) - the name of the database must be passed as argument of the file
* CSV file can contain empty lines (at the end) - and they are not a valid student!

Terminal 1:
```bash
$ node 5-http.js database.csv

```
In terminal 2:

```bash
$ curl localhost:1245 && echo ""
Hello Holberton School!
$ 
$ curl localhost:1245/students && echo ""
This is the list of our students
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
$ 

```
---

+ [x] 6\. **Create a small HTTP server using Express**

+ **[6-http_express.js](./6-http_express.js)**

Install Express and in a file named   *` 6-http_express.js `*  , create a small HTTP server using Express module:
* It should be assigned to the variable  *` app `*  and this one must be exported 
* HTTP server should listen on port 1245
* Displays  *` Hello Holberton School! `*  in the page body for the endpoint  *` / `*
 
In terminal 1:

```bash
$ node 6-http_express.js
...
```

In terminal 2:

```bash
$ curl localhost:1245 && echo ""
Hello Holberton School!
$ 
$ curl localhost:1245/any_endpoint && echo ""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Cannot GET /lskdlskd</pre>
</body>
</html> 
$ 

```
---

+ [x] 7\. **Create a more complex HTTP server using Express**

+ **[7-http_express.js](./7-http_express.js)**

In a file named   *` 7-http_express.js `*  , recreate the small HTTP server using  *` Express `* :
* It should be assigned to the variable app and this one must be exported
* HTTP server should listen on port 1245
* It should return plain text
* When the URL path is  *` / `* , it should display  *` Hello Holberton School! `*  in the page body
* When the URL path is  *` /students `* , it should display  *` This is the list of our students `*  followed by the same content as the file <br> *` 3-read_file_async.js `*  (with and without the database) - the name of the database must be passed as argument of the file
* CSV file can contain empty lines (at the end) - and they are not a valid student!

Terminal 1:

```bash
$ node 7-http_express.js database.csv
...
```

In terminal 2:

```bash
$ curl localhost:1245 && echo ""
Hello Holberton School!
$ 
$ curl localhost:1245/students && echo ""
This is the list of our students
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
$ 

```
---

+ [x] 8\. **Organize a complex HTTP server using Express**

- **[full_server/utils.js](./full_server/utils.js)**
- **[full_server/controllers/AppController.js](./full_server/controllers/AppController.js)**
- **[full_server/controllers/StudentsController.js](./full_server/controllers/StudentsController.js)**
- **[full_server/routes/index.js](./full_server/routes/index.js)**
- **[full_server/server.js](./full_server/server.js)**

Obviously writing every part of a server within a single file is not sustainable. Let’s create a full server in a directory named   *` full_server `*.
Since you have used ES6 and Babel in the past projects, let’s use   *` babel-node `*   to allow to use ES6 functions like   *` import `*   or   *` export `*.

#### 8.1 Organize the structure of the server
* Create 2 directories within:
*  *` controllers `* 
*  *` routes `* 
* Create a file  *` full_server/utils.js `* , in the file create a function named  *` readDatabase `*  that accepts a file path as argument:
* It should read the database asynchronously
* It should return a promise
* When the file is not accessible, it should reject the promise with the error
* When the file can be read, it should return an object of arrays of the firstname of students per fields

#### 8.2 Write the App controller
Inside the file   *` full_server/controllers/AppController.js `*  :
* Create a class named  *` AppController `* . Add a static method named  *` getHomepage `* 
* The method accepts  *` request `*  and  *` response `*  as argument. It returns a 200 status and the message  *` Hello Holberton School! `*
 
#### 8.3 Write the Students controller
Inside the file   *` full_server/controllers/StudentsController.js `*  , create a class named   *` StudentsController `*. Add two static methods:
The first one is   *` getAllStudents `*:

* The method accepts  *` request `*  and  *` response `*  as argument
* It should return a status 200
* It calls the function  *` readDatabase `*  from the  *` utils `*  file, and display in the page:
* First line:  *` This is the list of our students `* 
* And for each field (order by alphabetic order case insensitive), a line that displays the number of students in the field, and the list of first names (ordered by appearance in 
	the database file) with the following format:  *` Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES `* 
* If the database is not available, it should return a status 500 and the error message  *` Cannot load the database `*
 
The second one is   *` getAllStudentsByMajor `*:

* The method accepts  *` request `*  and  *` response `*  as argument
* It should return a status 200
* It uses a parameter that the user can pass to the browser  *` major `* . The  *` major `*  can only be  *` CS `*  or  *` SWE `*. If the user is passing another parameter, 
	the server should return a 500 and the error  *` Major parameter must be CS or SWE `* 
* It calls the function  *` readDatabase `*  from the  *` utils `*  file, and display in the page the list of first names  for the students (ordered by appearance in the database file) 
	in the specified field  *` List: LIST_OF_FIRSTNAMES_IN_THE_FIELD `* 
* If the database is not available, it should return a status 500 and the error message  *` Cannot load the database `*
 
#### 8.4 Write the routes
Inside the file   *` full_server/routes/index.js `*:
* Link the route  *` / `*  to the  *` AppController `* 
* Link the route  *` /students `*   and  *` /students/:major `* to the *` StudentsController `*

#### 8.5 Write the server reusing everything you created
Inside the file named   *` full_server/server.js `*  , create a small Express server:
* It should use the routes defined in  *` full_server/routes/index.js `* 
* It should use the port  *` 1245 `*
 
#### 8.6 Update package.json (if you are running it from outside the folder full_server)
If you are starting node from outside of the folder   *` full_server `*  , you will have to update the command   *` dev `*   by: 
*` nodemon --exec babel-node --presets babel-preset-env ./full_server/server.js ./database.csv `*
 
**Warning**:

* Don’t forget to export your express app at the end of  *` server.js `*  ( *` export default app; `* )
* The database filename is passed as argument of the  *` server.js `*  BUT, for testing purpose, you should retrieve this filename at the execution (when  *` getAllStudents `*  or  
	*` getAllStudentsByMajor `* are called for example)

In terminal 1:

```bash
$ npm run dev
...
```
In terminal 2:

```bash
$ curl localhost:1245 && echo ""
Hello Holberton School!
$ 
$ curl localhost:1245/students && echo ""
This is the list of our students
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
$ 
$ curl localhost:1245/students/SWE && echo ""
List: Guillaume, Joseph, Paul, Tommy
$ 
$ curl localhost:1245/students/French -vvv && echo ""
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 1245 (#0)
> GET /students/SWES HTTP/1.1
> Host: localhost:1245
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 500 Internal Server Error
< X-Powered-By: Express
< Date: Mon, 06 Jul 2020 03:29:00 GMT
< Connection: keep-alive
< Content-Length: 33
<
* Connection #0 to host localhost left intact
Major parameter must be CS or SWE
$ 

```

If you want to add test to validate your integration, you will need to add this file: *` .babelrc `*

<details>
  <summary><h3>.babelrc :floppy_disk:</h3></summary>

```javascript
{
    "presets": [["env", {"exclude": ["transform-regenerator"]}]]
}

```
</details>


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
