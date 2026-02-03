EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(current_time):
    """Retruns the expected time remaining for the lasagna to bake."""
    if current_time == 0:
        return 0
    if EXPECTED_BAKE_TIME - current_time <= 0:
        return 0
    return EXPECTED_BAKE_TIME - current_time
    
    
def preparation_time_in_minutes(number_of_layers):
    """Returns the time it will take to prepare the lasagna base on how many layers you chose to add."""
    return PREPARATION_TIME * number_of_layers
    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates how much time it will take to cook."""
    return elapsed_bake_time + (PREPARATION_TIME* number_of_layers)
    
     
