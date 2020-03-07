------------------------------------------------------------------------------------------------------------------------
---------------------------------------------- Snake Problem -----------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

This project calculates all possible paths of sanke for a given grid and specifc length of snake.

The project is implemented in python 3.7.

Pybuilder is used to build the project.

Tips to build and run the project.

Project structure
snake
  |-----src
  |       |-----main
  |       |        |-----python
  |       |        |        |-----lib
  |       |        |               |-----__init__.py
  |       |        |               |-----Snakeproblem.py
  |       |        |-----scripts
  |       |                 |-----snake
  |       |-----unittest
  |                 |-----python
  |                          |-----Snake_tests.py
  |-----build.py
  |-----build.sh
  |-----Readme.md
  |-----setup.py
  |-----SnakePaths.py 

1. Build the project using command 
   username@ubuntu:~/snake$ . build.sh
   
   This will create a virtual environment and download python3.7 and pybuilder.
   Then pybuilder takes charge and build the project and also run the test cases.
   
2. Run the project using following command
   (venv)username@ubuntu:~/snake$ snake 1 1 1
   Here 1st and 2nd arguments indicate number of rows and columns respectively and 3rd arguments indicate length of snake.
                           
   
Some test cases are written and tested. Please feel free to add your test cases.
The project builds with 100% coverage.

Incase if you want skip all the build process and  want to run the project, just run SnakePath.py with arguments.
  username@ubuntu:~/snake$ python3 SnakePaths.py 1 1 1
  

Note: Since recursion is used in the implementation, it requires high processor for higher snake length with higher grid size.

If you have any questions please contact me.
asiregerenataraj@gmail.com 