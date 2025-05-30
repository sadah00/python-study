pin=5552
attempts=3

for i in range(1,attempts+1):
    trial=input('enter pin: ')
    if trial==pin:
        print("Correct pin")
        break
    else:
        rem_attempts=attempts-i
        if rem_attempts>0:
            print(f"Incorrect pin {rem_attempts} attempts left")
        else:
            print("SIM blocked")