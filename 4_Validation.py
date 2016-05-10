# Interlude - Validation
users_guess=0
attempts=0
prompt="Enter a number between 1 and 6 inclusive"

while not(1 <= users_guess <=6):
    try:
        attempts +=1
        users_guess= int(input(prompt))
        if not (1 <= users_guess <= 6):
            raise ValueError()
    except ValueError:
        prompt="Invalid entry. It must be 1 to 6"

print("You took {} attempts to enter a correct number".format(attempts))
