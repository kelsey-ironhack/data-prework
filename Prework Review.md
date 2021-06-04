# Jack Gibbons

Hello Jack! You have finished the Prework, and you did it in a very good way, congrats! Keep working on your code, it seems that you have understood the logic behind it. 

Let's check these exercises! 

## 1. Snail and the well 

In this exercise you had to work essentially with `while` loops and `if` conditions. In general, you did it well and tried to complete all the bonus questions, great!

The main question is almost perfect, but the correct answer is adding an if condition for the distance lost during the night. Also, you have to delete the substract of the nightly_distance. It will be something like this:
```python
while snail_position <= well_height:
    days += 1
    snail_position += daily_distance
    if snail_position <= well_height:
        snail_position -= nightly_distance
```
In the bonus you should have continued with the same logic as in the above question. You almost got it if you had repeated the same structure. 

Finally, the min. displacement is based only in the days that the snail has moved to surpass the well. 

## 2. Duel of sorcerers

Good work here, it seems that you understood really well how dictionaries and lists work. 

Looking at your code, when you store a value in a variable is not needed to put it on parenthesis. Great that you used the `zip`function for this assignment, it will be helpful in the future surely. 

In this case, you didn't have to put the equal operator in the if, elif conditions because it will result in a tie for each sorcerer. Be careful, because the total number of spells is just the length of gandalf or saruman variables, not the sum of both. 

In exercise 4 think about the idea that before, you have created two variables as empty lists to use them. If gandalf power was bigger than saruman power you had to sum a win to gandalf's list and restart the saruman's counter to 0 and vice versa. 

Good work finding the `statistics` library, it is very helpful for this kind of operations. 

## 3. Bus

Great, you resolved this assignment really good, congrats!
It's really cool that you are discovering all this libraries, such as itertools, just in the Prework, but in this case it's not really useful. 

When you use `itertools.chain`, it creates a list with all the in-and-out values. As the variable `stops`is a list, you have to calculate the length of the list to know the total number of stops. 

## 4. Robin Hood

Wow! You used a list comprehension in such a difficult task, well done!!

You did an amazing job here, nothing else to say in this assignment. 

## 5. Temperature

Good work here again! Just check the operators when the problem ask you about greater/greater than...
If you want to keep clear these concepts, check this link:
https://www.w3schools.com/python/python_operators.asp
If afterwards you have any doubt about it, tell me without any problem!

Your work in the bonus here is great!

## 6. Rock, paper, scissors

Here we go with the last assignment! 

First of all, you don't need to import a library every time that you use it. Importing whatever library one time is enough for python and you save a little bit of time. 

You did it pretty good defining a function, but take in count that you had to do the same in the following questions after exercise number 6. 
Great that you use `continue` and `break` to do the function more robust. 

Overall you have shown great skills with while loops in this assignment, congrats! 

One way to optimize your code here is creating a dictionary with the possible results (which not end in a tie) between the user and the computer.
It will be something like this in question #8:
```python
def check_winner(cpu, player):
    rules = {'rock': 'scissors', 'paper': 'rock', 'scissors':'paper'}
    if rules[cpu] == player:
        return 1
    elif rules[player] == cpu:
        return 2
    return 0
```

In this assignment is really important to create functions that have to be called in next questions. With this method you will save a lot of time. If you have some of it, I encourage you to try it helped by the function above and try the bonus aswell. Great work!
