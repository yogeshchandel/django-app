from rest_framework.exceptions import ValidationError

def validate_username(value):
    if (not value.isalnum()) or len(value) < 3:
        raise ValidationError("Username must be at least 3 characters long and contain only alphanumeric characters.")
    
 
def validate(value):
    value = value.strip()
    if not value:
        raise ValidationError("This field cannot be empty or just whitespace.")   
    return value