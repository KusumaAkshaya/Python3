#q1
name = input("Enter your name: ")
print("Hello, " + name)

#q2
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

num3 = num1 + num2 
print("sum is ", num3)

#q3
num = int(input("Enter a number: "))
print(num-1, num+1)

#q4
print("The Quick Brown Fox jumps over the Lazy Dog")
print("                    and                    ")
print("Pack my box with Five Dozen Liquor Jugs")

#q5
fName = input("Enter your first name: ")
#print("\nThanks")
lName = input("Enter your last name: ")

#print("\n" + fName + " " + lName)
print(fName, lName)

#q6
print('F', 'U', sep='', end='')
print('N')

print('25', '12', '1997', sep='-', end='\n')
print('Red', 'Green', 'Blue', sep=',', end='@')

print("debasis")
print("debasis")

#q7

print("Two digit value : %2d, Float value : %5.2f" % (1, 354.1772))
print("Total students : %3d, Boys : %2d" % (240, 120))
print("Octal of %2d is %7.3o" % (25, 25))
print("Gravitational constant, G = %10.3E" % (6.6743e-11))

#q8
programming = "Coding"
python = "python3"
print('I love {} for "{}"!'.format('Python','Programming', 'for', 'Data Analytics'))
print('{1} and {0}'.format('Kusuma', 'Akshaya'))
print('{1} and {2}'.format('kusuma', 'akshaya', 'jyothika'))
print(f"I love {programming} in \"{python}!\"")
