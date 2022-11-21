print("enter name and age and addrass")
name=input()
age=input()
age=int(age)
address=input()
result1=type(name) is str
result2=type(age) is int
if name==None:
    print("the input is erorr")
print("the name is string",result1)
print("the age is int:",result2)
print("hello mr/ms",{name}," age",{age}," located in",{address},".")
print("thanks for beening one of our community \t Enjoy")