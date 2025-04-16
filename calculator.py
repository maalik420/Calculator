import art

print(art.logo)
condition = True
calculator_on = True

while calculator_on:
    switch = input('Want to perform your calculation?, yes or no?')
    if switch == 'yes':
        calculator_on = True
    else:
        calculator_on = False
        print('Thankyou!')
        break
    n1 = int(input('Enter the first number:'))
    n2 = int(input('Enter the second number:'))

    while condition:
        def add(n1, n2):
            return n1 + n2
        def sub(n1, n2):
            return n1 - n2
        def multi(n1, n2):
            return n1 * n2
        def div(n1, n2):
            return n1/n2

        choice = str(input('Enter your choice: '))
        calculator = {
            '+': add,
            '-': sub,
            '*': multi,
            '/': div
        }

        result = calculator[choice](n1,n2)
        print(f'The result of the operation is: {result}')

        want_to_continue = input('Do you want to continue with the calculated result? yes/no ?')

        if want_to_continue == 'yes':
            n1 = result
            n2 = int(input('Enter the new second number:'))
        else:
            print('Thank you !!')
            break
