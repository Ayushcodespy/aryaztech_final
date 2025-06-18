import re

def validate_name(name):
    if not name:
        return "Name is required."
    
    # Allow letters and spaces, but not digits or special characters
    if not re.match(r'^[A-Za-z ]+$', name):
        return "Name must contain only letters and spaces."

    return None  # Valid


def validate_email(email):
    if not email:
        return "Email is required."
    # Email regex pattern
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return "Invalid email format."
    return None  # Return None if valid

def validate_message(message):
    if not message:
        return "Message is required."
    if len(message) < 10:
        return "Message must be at least 10 characters long."
    return None  # Return None if valid


def contactFormValidate(name, email, message):
    # Validate each field
    name_error = validate_name(name)
    if name_error:
        return name_error

    email_error = validate_email(email)
    if email_error:
        return email_error

    message_error = validate_message(message)
    if message_error:
        return message_error

    # If all validations pass, return a success message
    return True
