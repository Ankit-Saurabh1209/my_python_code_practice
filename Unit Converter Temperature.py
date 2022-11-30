print("..........Unit Converter..........")
print("Enter 0 for Celcius to Fahrenheit or 1 for Fehrenheit to Celcius")

# C = Fahrenheit
# C = celcius
#Degree_Symbol = "\u00B0"
choose = input("Celcius to Fahrenheit or Fehrenheit to Celcius: ")

if choose == "0":
    C = float(input("Enter the value in (C):"))
    F = (C * 9 / 5) + 32
    print(F, "F\u00B0")

if choose == "1":
    F = float(input("Enter the value in (F):"))
    C = (F - 32) * 5 / 9
    print(C, "C\u00B0")

