## BMI Calculator
## BMI = Weight / (Height x Height)
## < 19 : Thinness
## entre 20 y 25: Normal
## entre 26 y 30: Overweight
## > 30 : Obesity

weight = float(input('enter your weight in kilograms: '))
heightInCM = int(input('enter your height in centimetres: '))
heightInM = heightInCM / 100

imc = weight / (heightInM * heightInM)

print('Your BMI is ' + str(imc))

if imc < 20:
    print('You are thin')
if imc >= 20 and 25:
    print('You are normal')
if imc >= 26 and 30:
    print('You are overweight')
if imc >= 30:
    print('You have obesity') 
