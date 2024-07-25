from Variable_Sort import VariableSort

def main():
    VariableSorter = VariableSort()
    while True:
        UserInput = input("Enter a Variable (or 'stop'):")
        if UserInput.lower() == 'stop':
            break
        try: # check if integer
            if UserInput.isdigit():
                VariableSorter.add_variables(int(UserInput))
            elif UserInput.replace('.','',1).isdigit() and UserInput.count('.') < 2:
                VariableSorter.add_variables(float(UserInput)) #check if float 
            else:
                VariableSorter.add_variables(UserInput)
        except (ValueError, TypeError) as e:
            print(e)

    print("Strings:", VariableSorter.get_strings()) #prints string integer and float
    print("Integers:", VariableSorter.get_integers())
    print("Floats:", VariableSorter.get_floats())

if __name__ == "__main__":
    main()