while True:
    print('Welcome to Python program.')
    print('Menu options are:')
    print('Enter 1 for calculating gallons of paint needed to paint a room')
    print('Enter 2 for calculating Body Mass Index')
    print('Enter any other value to quit the program\n')
    try:
        selection = int(input('Enter menu option: '))
    except ValueError:
        quit()
    if selection == 1:
        #Paint calculation
        print('Welcome to the paint needed calculator.')
        length = float(input('Enter the length of the room: '))
        width = float(input('Enter the width of the room: '))
        height = float(input('Enter the height of the room: '))
        doors = int(input('How many doors are in the room? '))
        windows = int(input('How many windows are in the room? '))
        result = (((width * height) * 2) + ((length * height) * 2) - ((doors * 25) + (windows * 10))) / 315
        print('{result: .2f} gallons of paint are needed to paint a room {width: .2f} feet wide by {length: .2f} feet long by {height: .2f} feet high with {doors} doors and {windows} windows.\n'.format(**locals()))
    elif selection == 2:
        print('Welcome to the body mass index (BMI) calculator.')
        weight = float(input('Enter your weight in pounds: '))
        height = float(input('Enter your height in inches: '))
        result = (weight * 703) / (height * height)
        if result > 30:
            BMI = 'Obese'
        elif result >= 25:
            BMI = 'Overweight'
        elif result >= 18.5:
            BMI = 'Normal'
        else:
            BMI = 'Underweight'
        print('Your BMI is {result: .2f}. According to NIH, you are {BMI}.\n'.format(**locals()))
    else:
        quit()
   