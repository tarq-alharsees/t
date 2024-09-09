# this is supoed to be the check out page on a booking website 

print("Welcome to the Grand Hotel")

def guests_info():
    suffix = input("Suffix: ")
    first_name = input("Please state your first name: ")
    middle_name = input("Please state your middle name: ")
    last_name = input("Please state your last name: ")
    return suffix, first_name, middle_name, last_name 
# what is this "return" function

email = input("Email address: ")
number_of_nights = int(input("Number of nights (150 AED per night): "))
night_price = 150

number_of_guests = int(input("Number of guests: "))

# To store the details of all guests
guest_details = []
# what is this ^
for _ in range(number_of_guests):
    guest_details.append(guests_info())
#what is this ^

# print the details of the first guest
suffix, first_name, middle_name, last_name = guest_details[0]

# Receipt, why are they using these types of prenthises 
print(f"{suffix} {first_name} {last_name}, an e-mail has been successfully sent to {email}, containing your confirmation booking. TOTAL PRICE: {night_price * number_of_nights:.2f} AED")



