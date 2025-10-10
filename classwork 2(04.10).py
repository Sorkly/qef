
#import inspect

#def greet(name,msg="hello"):
  #  pass

#sig = inspect.signature(greet)
#for param in sig.parameters.values():
 #   print(param.name, param.default)

#def list_checker(var_1):
   # if type(var_1) != str:
       # raise TypeError(
        #    f"Invalid type:"
       # )

#first_var = "hello"
#list_checker(first_var)


def program_checker(prog_1):
    if type(prog_1) != list:
        raise TypeError(
            f"Error type : {type(prog_1)}. ")
    else:
        return f"List is OK: {prog_1}"
    
first_variant = "Hi friend"
program_checker(first_variant)