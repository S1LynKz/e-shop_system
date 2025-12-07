class Validator:
    @staticmethod
    def validate_string(value):
        if not isinstance(value, str) or not value:
            raise ValueError(f'Must be a non_empty string. Got: {value}')
        return value
    
    @staticmethod
    def validate_positive_number(value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f'Must be a positive integer or float. Got: {value}')
        return value
    
    @staticmethod
    def validate_user_id(user_id):
        if not isinstance(user_id, int) or user_id < 0:
            raise ValueError('User ID must be a positive integer')
        return user_id
    
    @staticmethod
    # Make password validator better (Requirements that go green or red if meets requirement)
    def validate_password(password):
        if not isinstance(password, str) or not password or not len(password) > 7 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            raise ValueError('Pasword must be a string of length 8 or more and must contain at least 1 number and letter')
        return password