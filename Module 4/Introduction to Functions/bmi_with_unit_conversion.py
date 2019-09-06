def feet_m(feet, inches):
    m_per_feet = 0.3048
    m_per_inches = m_per_feet / 12
    
    meters_from_feet = feet * m_per_feet
    meters_from_inches = inches * m_per_inches
    
    return meters_from_feet + meters_from_inches

def lb_kg(lbs):
    kg_per_lb = 0.4536
    return lbs * kg_per_lb

def bmi(height1, height2, weight, system):
    if system == 'imperial':
        metric_height = feet_m(height1, height2)
        metric_weight = lb_kg(weight)
    else:
        metric_height = height1
        metric_weight = weight
    return metric_height/metric_weight**2
