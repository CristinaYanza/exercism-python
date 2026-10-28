"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""

    if temperature >= 800:
        return False
    elif neutrons_emitted <= 500:
        return False
    elif temperature * neutrons_emitted >= 500000:
        return False
    else:
        return True

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""
    generated_power = voltage * current 
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else: 
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    criticality = temperature * neutrons_produced_per_second

    if criticality < threshold * 0.9:
        return "LOW"
    elif criticality <= threshold * 1.1:
        return "NORMAL"
    else:
        return "DANGER"