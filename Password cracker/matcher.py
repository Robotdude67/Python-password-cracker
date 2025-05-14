def find_password_from_hash(hash_to_find, hashed_file_path):
    try:
        with open(hashed_file_path, 'r') as file:
            for line in file:
                # Each line looks like: Password: password123 => Hash: abc123...
                if "=> Hash: " in line:
                    password_part, hash_part = line.strip().split(" => Hash: ")
                    if hash_part == hash_to_find:
                        password = password_part.replace("Password: ", "")
                        return password
        return None
    except FileNotFoundError:
        print("Error: Hashed password file not found.")
        return None

# Get hash input from user
user_hash = input("Enter the SHA-256 hash to search for: ").strip()

# Search for the hash in the output file
matched_password = find_password_from_hash(user_hash, 'Usernamehashes.txt')

if matched_password:
    print(f"Match found! Original password: {matched_password}")
else:
    print("No match found.")


    
