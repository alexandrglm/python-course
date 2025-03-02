 # 03-104: Combining all Arguments types into one Function

def greeting(time_of_day, *args, **kwargs):
    print(f'Hi {' '.join(args)}, I hope that you\'re having a good {time_of_day}.\n')

    if kwargs:
        print('Your daily tasks are:\n')

        for key, val in kwargs.items():
            print(f'{key} => {val}')

greeting(
    'Morning', 
    'Homer', 'J.', 'Simpson', 
    first = 'Prepare Coffee',
    second = 'Login',
    third = 'Wait for further instructions'
    )