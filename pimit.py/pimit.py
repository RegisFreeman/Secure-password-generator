def generate_password_from_name(full_name, total_length=16):
    # Clean input
    cleaned_name = full_name.replace(" ", "")
    if len(cleaned_name) < 4:
        return "Please enter a longer name with more unique characters."

    # Use only unique characters from the name
    base_chars = list(set(cleaned_name))

    # Add predefined digits and specials
    digits = string.digits
    specials = "!@#$%?."

    # Combine allowed character pool
    char_pool = base_chars + list(digits) + list(specials)

    # Generate password from this limited pool
    password = ''.join(random.choices(char_pool, k=total_length))

    return password
