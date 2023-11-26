import phonenumbers
from phonenumbers import carrier, timezone, geocoder

def is_valid_phonenumber(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

while True:
    phone_number = input("Enter a phone number: ")

    if is_valid_phonenumber(phone_number):
        parsed_number = phonenumbers.parse(phone_number, None)
        carrier_name = phonenumbers.carrier.name_for_number(parsed_number, "en")
        timezone_info = phonenumbers.timezone.time_zones_for_number(parsed_number)
        geocoder_info = phonenumbers.geocoder.description_for_number(parsed_number, "en")
        region_code = phonenumbers.region_code_for_number(parsed_number)
        phone_number_type = phonenumbers.number_type(parsed_number)
        print(f"Valid phone number! The number's carrier name is {carrier_name}, the timezone is: {timezone_info}, the geocoder is: {geocoder_info}. the region code is: {region_code}. The type is: {phonenumbers.number_type(parsed_number)}")
    else:
        print("Invalid phone number. Please enter a valid phone number.")