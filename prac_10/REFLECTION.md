# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?
My estimates were often slightly optimistic. I tended to underestimate how long it would take to debug or understand new concepts, especially in the earlier weeks.

### How did your estimate accuracy improve or change during the course of the subject?
Over time, my estimates became more realistic as I became better at breaking down tasks and identifying tricky areas. I started accounting for things like time spent reading the instructions or fixing unexpected bugs.

### What did you learn from doing these estimates?
I learned that making accurate estimates takes practice and reflection. Estimating helps me plan better and gives me a clearer idea of how I spend my time and where I need to improve.

## Code Reviews

### What have you learned from being reviewed by other people?

I learned to be more careful with code readability and naming. Seeing how others interpret my code made me more aware of writing clear comments and following style guidelines.

### What have you learned from doing code reviews of other people?

Reviewing others' code helped me spot different approaches to solving problems. It also made me more critical of my own coding style and logic, encouraging me to follow best practices consistently


### Good Code Review 1

[PR: prac_06-car](https://github.com/Fanyiqi25588/cp1404practice)

### Explanation

The code demonstrates clear encapsulation (e.g., _odometer as a protected attribute) and logical handling of fuel/distance in the drive() method. However, input validation is missing (e.g., negative fuel amounts or distances are allowed). Add checks like if amount < 0: raise ValueError(...) to methods like add_fuel() and drive(), and include type hints for clarity.

### Good Code Review 2

[PR: prac_08 - squaring](https://github.com/Fanyiqi25588/cp1404practice)

### Explanation

The UI/logic separation is clean, and error handling catches non-numeric inputs. However, the UI could enforce numeric-only input using input_filter: 'float' in the Kivy file, and empty input should display a user-friendly prompt (e.g., "Enter a number") instead of "Invalid input."

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

I would provide more visual examples or video demos of the more complex practicals like Kivy or Flask, especially for students who are new to those technologies.


### What did you do really well for practicals in this subject?

I was consistent in completing each week’s practicals on time, following the correct coding style, and pushing to GitHub. I also improved a lot in writing testable code and learning how to debug effectively.