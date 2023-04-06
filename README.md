<!--hide-->
# The Excuse Generator CLI (in python)
<!--endhide-->

Disneyland for procrastinators and lazy people. 

This project is ideal to are avoiding someone annoying, it takes no more than 20 lines of code, and it can save you for the rest of your life!

![this exact same picture](https://github.com/breatheco-de/exercise-excuse-generator-python-cli/blob/master/preview.gif?raw=true)

## The Goal

We wanted a project that used very little Python but still with a very fun application, the excuse generator takes 20 lines of code, is super simple to understand and is the perfect first-ish project for any beginner developer.

## Instructions

Please create a python script that generates an excuse each time it is runned.

## Discuss with your classmates the strategy first

How can we generate an excuse? How are sentences built?

![Excuse generator explanation](https://github.com/breatheco-de/tutorial-project-excuse-generator-javascript/blob/master/explanation.gif?raw=true)

The idea is to generate each part of the sentence randomly to come up with great excuses!

## 🌱  How to start this project

Do not clone this repository.

1. The first step to start coding is cloning the [python boilerplate](https://github.com/4GeeksAcademy/flask-rest-hello) on your local computer or gitpod.

a) If using Gitpod (recommended) you can clone the boilerplate by [clicking here](https://github.com/4GeeksAcademy/flask-rest-hello).

b) If working locally, type the following command from your command line: 
```sh
git clone https://github.com/4GeeksAcademy/flask-rest-hello`.
````
2. Run the app by typing on the terminal:
```bash
$ python3 app.py
```

💡 Important: Remember to create a new repository, update the remote (`git remote set-url origin <your new url>`), and upload the code to your new repository using `add`, `commit`, and `push`.

## Hint

1. Create an `app.py` file with one excuse hard-coded in one variable.
2. The excuse must be in a variable:
```python
excuse = 'The dog eat my homework when I finished'
```
3. Using python, create a function that generates and returns a random excuse with the following structure:
```python
who = ['the dog','my granma','his turtle','my bird']
what = ['eat','pissed','crushed','broked']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']
```
4. To create a consistent excuse, you have to concatenate one item from each array in the proper order.
5. Print the excuse on the console using the `print` function.


## Technologies

Python.

## Fundamentals

This exercise covers the following fundamentals:

1. Running python files.
2. How to work with Lists (arrays).
3. Generating random numbers.
4. Concatenating strings.
5. Using functions (at least a bit).
