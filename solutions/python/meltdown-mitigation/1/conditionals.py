"""Functions to prevent a nuclear meltdown."""

CAP = 500000
SECONDS = 1.0
NEUTRON_MIN = 500
TEMPERATURE_CAP= 800


def is_criticality_balanced(temperature, neutrons_emitted):
    total = temperature * neutrons_emitted
    if temperature < TEMPERATURE_CAP and neutrons_emitted > NEUTRON_MIN and total < CAP:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    calculated = (generated_power/ theoretical_max_power)*100
    if calculated >= 80.0:
        return "green"
    elif calculated <= 80.0 and calculated >= 60.0:
        return "orange"
    elif calculated < 60.0 and calculated >= 30.0:
        return "red"
    else:
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = (temperature * neutrons_produced_per_second)
    
    if product < (threshold * 0.90):
        return "LOW"
    elif (threshold * 0.9) <= product <= (threshold * 1.1):
        return "NORMAL"
    else:
        return "DANGER"
        
    """Assess and return status code for the reactor.
    
    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    pass
