# GENERAL INFORMATION ON STRING METHOD  

     Python provides many built-in string methods to manipulate and analyze text. 
     In this project we'll see in detail on what the major string methods are, what they do and what the major syntax is for most of these.
     
     According to chatgpt there are about 6 major uses of these string methods.  
     These are: Case Manipulation Methods, Searching & Checking Methods, Modifying & Replacing Methods,  
     Formatting Methods, Splitting & Joining Methods and finally, Checking Character Types.  

     Here we'll try to see some of the string methods mentioned below with their corresponding examples. 

           str.lower() ; str.upper() ; str.title() ; str.capitalize() ; str.swapcase() ; str.find() ; str.index() ;  
           str.startswith() ; str.endswith() ; str.count() ; str.replace() ; str.strip() ; str.lstrip() ;  
           str.rstrip() ; str.split() ; str.join() ; str.isalpha() ; str.isdigit() ; str.isalnum() ; str.isspace() ;  
           str.format() ; f-strings ; len()= ; str.encode() ; str.islower() ; str.isupper()




###  BASIC SYNTAX FORMAT

The basic syntax for many of the above methods is   **result = string.method(optional_parameters)**. 
However, you can add starting and ending index numbers for several types of the methods mentioned. 

***Example:***  Running this code can give us a clear definition of what the parameters do.  
>text = "Hello World"  
>print(text.lower())  # "hello world"  **#output will be  "hello world"**  
>print(text.find("o", 5))  # 7    **#output will be "7"**  
>print(text.replace("Hello", "Hi", 1))  # "Hi World"  **#output will be "Hi World"**



   
   


# STR.CAPITALIZE()

 is used to convert the first letter of a string to uppercase while making all other letters lowercase. 




# STR.CASEFOLD()
 
It is used in Python to convert a string to lowercase. I will try to show in this file how it relates with other string method called "lower"

## Examples

In the examples of .py file, I'll try forcase their main differences, that is between lower and casefold.  
**For example,**  
>on the first part of the code we can see that both convert the string to lowercase.  
>Next, we can see that for special characters the lower case doesn't change the string but  
>the casefold changes the character to other small letters. This makes casefold better for  
>the case of multilanguage cases.




# STR.SWAPCASE()

As the name basucally implies, it is used to swap the case of the letters is a given word or sentences.




# STR.TITLE()

This is one of the string methods used to change the first letter of every word to capital  
letter. As the name implies it is mostly used for writing strings that are used as title.




# STR.UPPER()

This method is used to change every letter of a given string to uppercase. 




# STR.STARTSWITH() AND STR.ENDSWITH()

## str.startswith

This is a method that checks if a string starts with a specified prefix.  
It returns a boolean output, either True if it does or else False.  
It is used to avoid unnecessary processing by quickly checking the beginning of a string.

## str.endswith

This on the other hand checks if a string ends in a specified suffix. Just as str.startswith it returns a boolean value.




# STR.FIND() ; STR.INDEX() AND STR.COUNT()

## str.find()

Is a method used for checking if a substring exists in a string. It is also used in finding the position of a substring to extract information.  
It returns the **lowest index** of substring or else returns **-1** if the string is not found.


## str.count()

This returns the **number of times** a string is mentioned or appears.


## str.index()

The main difference between str.find() and str.index() is that str.index returns **ValueError** if the string does nto exist.