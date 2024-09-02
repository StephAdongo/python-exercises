# lets store a favorite number
favorite_number = 42
print("My favorite number is {favorite_number}")

#how about a word(string)
greeting = "Hello world"
print(greeting)

#and a true/false value (boolean)
is_python_fun = True
print("is python fun? {is_python_fun}")
 
temperature = 30
if temperature > 25:
    print("It's hot outside! Wear shorts")
elif temperature >15:
    print("It's warm outside.Maybe a light jacket")
else:
    print("Brr! It's cold outside! Bundle up")

    #Defining a function
def greet(name):
    return "Hello, {name}!"

#using the function
print(greet("Steph"))
print(greet("Bob"))
