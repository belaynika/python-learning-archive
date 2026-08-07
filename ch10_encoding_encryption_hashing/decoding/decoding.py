# DESCRIPTION: Retrieving data from a text file and decoding them so that the data can be used in a downstream 
# application. 

# cd ch10_encoding_encryption_hashing
# cd decoding

# Options: data01.txt , data02.txt , data03.txt

import base64



def main():
    decode_data()

def decode_data():

    # Open file

    user_file = input("File name? ")

    with open(user_file, 'r') as file:
        file_content = file.read()

    # Get data

    decoded_message = base64.b64decode(file_content)
    
    
    # Output decoded data

    print(decoded_message)

    
main()