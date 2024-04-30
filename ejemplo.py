import turtle  
  
# print the default  
# position i.e; (0.0, 0.0) 
print(turtle.pos()) 
  
# forward turtle by 150 pixels 
turtle.forward(150) 
  
# print current position  
# i.e; (150.0, 0.0) 
print(turtle.pos()) 
  
# forward turtle by 150 pixels 
# after taking turn right 
# by 90 degrees 
turtle.right(90) 
turtle.forward(150) 
  
# print position (after next move) 
# i.e; (150.0, -150.0) 
print(type(tupleturtle.pos()))