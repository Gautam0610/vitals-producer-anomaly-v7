import random

def generate_realistic_vitals():
    body_temp = round(random.uniform(36.5, 37.5), 1)  # Celsius
    heart_rate = random.randint(60, 100)  # BPM
    systolic_pressure = random.randint(110, 140)  # mmHg
    diastolic_pressure = random.randint(70, 90)  # mmHg
    breaths_per_minute = random.randint(12, 20)  # Breaths per minute
    oxygen_saturation = random.randint(95, 100)  # %
    blood_glucose = random.randint(70, 140)  # mg/dL

    return {
        'body_temp': body_temp,
        'heart_rate': heart_rate,
        'systolic_pressure': systolic_pressure,
        'diastolic_pressure': diastolic_pressure,
        'breaths_per_minute': breaths_per_minute,
        'oxygen_saturation': oxygen_saturation,
        'blood_glucose': blood_glucose
    }

def generate_anomalous_vitals():
    # Generate extremely unrealistic values for heart_rate and breaths_per_minute
    heart_rate = random.randint(150, 220)  # Very high BPM
    breaths_per_minute = random.randint(30, 50)  # Very high breaths per minute

    return {
        'body_temp': round(random.uniform(36.5, 37.5), 1), 
        'heart_rate': heart_rate,
        'systolic_pressure': random.randint(110, 140),  # mmHg
        'diastolic_pressure': random.randint(70, 90),  # mmHg
        'breaths_per_minute': breaths_per_minute,
        'oxygen_saturation': random.randint(95, 100),  # %
        'blood_glucose': random.randint(70, 140)  # mg/dL
    }
