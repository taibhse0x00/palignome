# print gnome banner because we love ASCII art:
print("""
               __
             .-'  |
            /   <\|
           /     \'
           |_.- o-o
           / C  -._)\\
          /',        |
         |   `-,_,__,'
         (,,)====[_]=|
           '.   ____/
            | -|-|_
            |____)_)    
      
\tHey it's Palignome.
""")
print(f"\tHe's here to help you work out if you have a palindrome.\n")

#Get an string from the user:
string = input(f"\tPotential palindrome : ") 
 
# Empty var that we'll use to reverse the string   
reversedstring ="" 
 
# Iterate through the string as a for loop
for i in string: 
    reversedstring = i + reversedstring 
print(f"\tReversed word : {reversedstring}\n" ) 

# if string = itself reversed, then we have a pallindrome, print the output to the user
if(string == reversedstring): 
    print(f"\tIt's a palindrome.\n") 
else: 
    print(f"\tIt's not a palindrome. Sad times.\n")
