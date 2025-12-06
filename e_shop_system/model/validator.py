class Validator:
    @staticmethod
    def validate_string(value, field_name):
        if not isinstance(value, str) or not value:
            raise ValueError(f'{field_name} must be a non_empty string. Got: {value}')
        return value
    
    @staticmethod
    def validate_positive_number(value, field_name):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f'{field_name} must be a positive integer or float. Got: {value}')
        return value
    
    @staticmethod
    def validate_user_id(user_id):
        if not isinstance(user_id, str) or not user_id or not user_id.isalnum():
            raise ValueError('User ID must be an alphanumeric string')
        return user_id
    
    @staticmethod
    # Make password validator better (Requirements that go green or red if meets requirement)
    def validate_password(password):
        if not isinstance(password, str) or not password or not len(password) > 7 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            raise ValueError('Pasword must be a string of length 8 or more and must contain at least 1 number and letter')
        return password