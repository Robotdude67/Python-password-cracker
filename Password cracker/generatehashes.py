import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def hash_passwords_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        passwords = file.readlines()

    with open(output_file_path, 'w') as output_file:
        for password in passwords:
            password = password.strip()
            hashed_password = hash_password(password)
            output_file.write(f"Password: {password} => Hash: {hashed_password}\n")

# Run the function with file paths
hash_passwords_from_file('commonpasswords.txt', 'Usernamehashes.txt')

