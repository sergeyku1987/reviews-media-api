from django.core.exceptions import ValidationError

def validate_name(name):
    if name == 'me':
        raise ValidationError