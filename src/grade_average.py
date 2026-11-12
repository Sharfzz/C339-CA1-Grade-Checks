def calculate_average(mark_one, mark_two):
    """Calculate the arithmetic mean of two equally weighted marks."""
    
    if type(mark_one) is not int or type(mark_two) is not int:
        raise TypeError("invalid argument type")
        
    if not 0 <= mark_one <= 100 or not 0 <= mark_two <= 100:
        raise ValueError("argument outside permitted range")

    return (mark_one + mark_two) // 2
