def has_passed(score):
    """Determine whether a recorded score meets the pass mark."""
    
    if type(score) is not int:
        raise TypeError("invalid argument type")
        
    if not 0 <= score <= 100:
        raise ValueError("argument outside permitted range")

    return score >= 50
