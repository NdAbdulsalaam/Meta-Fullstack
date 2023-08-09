# Lab Instructions: Import and Scope

So far, you've learned the different ways in which you can use import statements to import other Python files, modules and packages.   
You have also seen the different ways in which you can import specific functions using different formats of import.   
In this assignment you'll learn and practice how to use import to bring external code within the direct scope of the project.

 <br>

> ### **Tips: Before you Begin**
> #### **To view your code and instructions side-by-side**, select the following in your VSCode toolbar:
> - View -> Editor Layout -> Two Columns
> - To view this file in Preview mode, right click on this README.md file and `Open Preview`
> - Select your code file in the code tree, which will open it up in a new VSCode tab.
> - Drag your assessment code files over to the second column. 
> - Great work! You can now see instructions and code at the same time. 
> - Questions about using VSCode? Please see our support resources [here](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
> #### **To run your Python code**
> - Select your Python file in the Visual Studio Code file tree 
> - You can right click the file and select "Run Python File in Terminal" 
>   or run the file using the smaller   
    play button in the upper right-hand corner 
>   of VSCode.  
    (Select "Run Python File in Terminal" in the provided button dropdown)
> - Alternatively, you can follow lab instructions which use python3 commands to run your code in terminal.
> 

<br>

## Exercise Objectives:
- Use the import statement to import a built-in package in Python.
- Use the import statement to call a function present in another Python file. 
<br><br>

## Instructions

1.  Open the file jsongenerator.py present inside project folder.

2. Import a built-in package called `json` 
   
3. Import the following from a file called employee.py:
   - A function called `details` 
   - Variables called `employee_name`, `age` and `title`
<br><br>

4. Implement the `create_dict()` function that returns a dictionary given employee information.   
Create and return a dictionary with three key-value pairs where:
    - Keys are string variables: `"first_name"` `“age”` and `“title”`  
     and their respective values are `employee_name`, `age` and `title` variables that we have imported from the employee module. 
    - Be sure to cast the values to the expected types.
<br><br>

5. Use a function called `dumps()` from the json module using dot notation and pass the `employee_dict` dictionary that we have created to it.   
Return its value to a variable named `json_object`. 

    The format of the same should look like:
    ```
    variable = json.dumps(dict) 
    ```

6. Complete the `write_json_to_file()` function
    - Use a built-in function called `open()` and pass the `output_file` argument and `“w”` to it.   
    Return the value of this function to a variable named newfile.
    -   Call a function called `write()` over this variable newfile. Pass the `json_object` variable you created in Step 5 inside it.
    - Close this file by calling a built-in function `close()` directly on newfile. You don’t need to pass any arguments here. 
<br><br>


7. Save the files

8. Open the terminal to execute the files

9. Run the code using the command (within project directory)
   ```
    python3 jsongenerator.py 
    ```

<br>


## Final Step: Let's submit your code!
Nice work! To complete this assessment:
- Save your file through File -> Save 
- Select "Submit Assignment" in your Lab toolbar. 

Your code will be autograded and return feedback shortly on the "Grades" tab.  
You can also see your score in your Programming Assignment "My Submission" tab.
<br> <br> 




# NEW

# Lab Instructions: Write a test

In this exercise, you'll learn how to create test cases for a given block of code using PyTest.  

You will be checking the accuracy of a string input to a given function against some conditions and writing two functions:
- **The first function** will check if the length of the input string is within a   
specific limit of words and characters. 
- **The second function** will check if the basic grammar of the string is well-defined.
 <br><br>

> ### **Tips: Before you Begin**
> #### **To view your code and instructions side-by-side**, select the following in your VSCode toolbar:
> - View -> Editor Layout -> Two Columns
> - To view this file in Preview mode, right click on this README.md file and `Open Preview`
> - Select your code file in the code tree, which will open it up in a new VSCode tab.
> - Drag your assessment code files over to the second column. 
> - Great work! You can now see instructions and code at the same time. 
> - Questions about using VSCode? Please see our support resources [here](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
> #### **To run your Python code**
> - Select your Python file in the Visual Studio Code file tree 
> - You can right click the file and select "Run Python File in Terminal" 
>   or run the file using the smaller   
    play button in the upper right-hand corner 
>   of VSCode.  
    (Select "Run Python File in Terminal" in the provided button dropdown)
> - Alternatively, you can follow lab instructions which use python3 commands to run your code in terminal.
> 

<br>

## Objective of this activity:   
Ensure the string variables that will be passed as arguments to the code are within a specified length and have a well-defined structure.<br><br>

## Instructions:

1. Open the `test_spellcheck.py` file inside the project folder.

2. Import the `pytest` and `spellcheck` modules.
3. Comment out the beta variable using # symbol for now. 
4. Next, complete the `test_length()` and `test_struc()` functions.   
   These two functions use input_value to check if the functions defined in spellcheck behave correctly. 
5.  In `test_length()` function, you must add two assert statements.   
    In each assert statement you first need to call the required function from the spellcheck file that you imported,  
    and then check against some conditions. For example, the format will be similar to the following against some condition:
    ```
    assert spellcheck.some_function(input_value)
    ```
    - 5.1: Add the first assert statement over `function word_count()` from the main code which asserts that the returned value is less than 10.
    - 5.2: Add the second assert statement over `function char_count()` from the main code which asserts that the returned value is less than 50. 
<br><br>

6. In the second function `test_struc()`, you must add two assert statements. The first assert statement checks if the first character is in upper case.  
The second assert statement checks if the sentence or the string variable passed ends with a dot (“.”) 
    - Add the first assert statement over function `first_char()` from the main code.  
      Now call a built-in function `isupper()` directly over it, such as `function_name.isupper()`. 
    - `isupper()` function returns True if it is called over an upper-case character and False if called over a lower-case character.  
      For example, `"A".isupper()` returns `True` and `"a".isupper()` returns `False`.
    - Add the second assert statement over the function `last_char()`from the main code and compare it to `“.” ` 
<br><br>

7. Save the files.
8. Open the terminal to execute the files.
9. Run the code using the following command (within the  project directory):
    ```
    python3 -m pytest test_spellcheck.py 
    ```
10. Both the tests should pass in this case.  


- **BONUS STEP:**<br>
Pass the variable beta instead of alpha in all four of the functions.  
The result should now show one passed and one failed test.  

<br>

> **Tips**<br>
> Be sure to double check some common mistakes made in this process 
  below before submitting!  
> - Forgetting to import the `pytest` and `main` code file
> - Not passing the variable names correctly
> 
<br>


## Final Step: Let's submit your code!
Nice work! To complete this assessment:
- Save your file through File -> Save 
- Select "Submit Assignment" in your Lab toolbar. 

Your code will be autograded and return feedback shortly on the "Grades" tab.  
You can also see your score in your Programming Assignment "My Submission" tab.
<br> <br> 