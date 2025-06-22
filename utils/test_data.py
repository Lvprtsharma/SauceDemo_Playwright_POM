class TestData:
    """Test data constants"""
    
    # Valid credentials
    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"
    PERFORMANCE_GLITCH_USER = "performance_glitch_user"
    VALID_PASSWORD = "secret_sauce"
    
    # Invalid credentials
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "invalid_password"
    
    # Checkout information
    CHECKOUT_INFO = {
        "first_name": "John",
        "last_name": "Doe",
        "postal_code": "12345"
    }
    
    # Expected error messages
    ERROR_MESSAGES = {
        "locked_out": "Epic sadface: Sorry, this user has been locked out.",
        "invalid_credentials": "Epic sadface: Username and password do not match any user in this service",
        "missing_username": "Epic sadface: Username is required",
        "missing_password": "Epic sadface: Password is required"
    }
    
    # Product names
    PRODUCTS = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]