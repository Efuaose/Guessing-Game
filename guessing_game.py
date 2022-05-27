first_Number = 10

user_guess = input('Enter your guess: ')
type_of_user_guess = type(user_guess)

#print(type_of_user_guess)

user_guess = int(user_guess)

#print(type(user_guess))

if user_guess == first_Number:
    print("Congratulations The number is: " + str(first_Number))

if user_guess < first_Number:
    print("Your guess is not correct. Try higher")

if user_guess > first_Number:
    print("Your guess is not correct. Try lower")
