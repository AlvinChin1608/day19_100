# day19_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner stage and later on intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

------------------------
## Higher-Order Functions
In Python, a higher-order function is a function that either:

- Takes one or more functions as arguments, or
- Returns a function as its result.
  
These functions are called "higher-order" because they operate on other functions, either by taking them as arguments or by returning them. This is a powerful feature that allows for greater flexibility and modularity in code.

**Passing Functions as Arguments Without Parentheses**

When you pass a function as an argument to another function, you do not include parentheses. This is because you want to pass the function itself, not the result of calling the function. Including parentheses would call the function and pass its return value instead.

```python
def greet():
    print("Hello, world!")

def call_function(func):
    func()

call_function(greet)  # Correct: Pass the function itself
# Output: Hello, world!

call_function(greet())  # Incorrect: Calls the function immediately and passes None
```
In the correct example, call_function(greet) passes the greet function itself to call_function, which then calls greet. In the incorrect example, greet() is called immediately, and the result (None) is passed to call_function.

This concept is essential in event-driven programming, such as setting up event listeners in graphical user interfaces (GUIs) or games. When you set an event handler, you pass the function reference without parentheses, so it is called only when the event occurs.
