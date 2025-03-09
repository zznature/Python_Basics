def parameter_demo(normal_param, *args, default_param="default", **kwargs):
    """
    Demonstrates different ways of passing parameters in Python
    
    Parameters:
    - normal_param: A regular required parameter
    - *args: Variable-length positional arguments (tuple)
    - default_param: Optional parameter with default value
    - **kwargs: Variable-length keyword arguments (dictionary)
    """
    print(f"Regular parameter: {normal_param}")
    
    print("\nPositional *args (tuple):")
    for i, arg in enumerate(args):
        print(f"  args[{i}]: {arg}")
    
    print(f"\nDefault parameter: {default_param}")
    
    print("\nKeyword **kwargs (dictionary):")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# Example 1: Basic usage
print("Example 1: Basic required parameter")
parameter_demo("Hello")
print("\n" + "-"*50)

# Example 2: With positional args
print("Example 2: With positional args")
parameter_demo("Hello", 1, 2, 3)
print("\n" + "-"*50)

# Example 3: With default parameter specified
print("Example 3: With default parameter specified")
parameter_demo("Hello", 1, 2, default_param="custom")
print("\n" + "-"*50)

# Example 4: With kwargs
print("Example 4: With kwargs")
parameter_demo("Hello", name="Alice", age=30, job="Developer")
print("\n" + "-"*50)

# Example 5: Full example with all parameter types
print("Example 5: Full example with all parameter types")
parameter_demo("Hello", 1, 2, 3, default_param="custom", name="Alice", age=30, job="Developer")
print("\n" + "-"*50)

# Example 6: Unpacking existing collections
print("Example 6: Unpacking existing collections")
numbers = [0, 'a', 2, [3], {4}]
info = {"name": "Bob", "age": 25, "city": "New York"}
parameter_demo("Hello", *numbers, **info, default_param="custom")