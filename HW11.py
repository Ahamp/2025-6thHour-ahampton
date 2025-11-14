#Name:
#Class: 6th Hour
#Assignment: HW11

#1. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg


#import random library
import random
#Create a temperature variable, give it a value (random from 1 to 30).
temp_var = random.randint(1,30)
print(temp_var)
#Make an if statement to see if temperature variable is above 20
#   - If yes, print it's hot
#   - If no, bring it to next if statement
if temp_var >20:
    print("It is Hot")
elif temp_var > 10:
    print("It is Mild")
else:
    print("It is Cold")

#Make an if statement to see if temperature variable is above 10
#   - If yes, print it's mild
#   - If no, print it's cold

#Print "Thank you!" and end the code
print("Thank you")