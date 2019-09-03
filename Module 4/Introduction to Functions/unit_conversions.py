metersInMiles = 1609.344
KmInMiles = metersInMiles / 1000
litersPerGallon = 3.785411784

def l100kmtompg(liters):
    literPerKm = liters/100
    gallonPerKm = literPerKm / litersPerGallon
    gallonPerMile = gallonPerKm * KmInMiles
    mpg = 1 / gallonPerMile
    return mpg

def mpgtol100km(miles):
    gallonPerMile = 1 / miles
    gallonPerKm = gallonPerMile / KmInMiles
    literPerKm = gallonPerKm * litersPerGallon
    literPer100Km = literPerKm * 100
    return literPer100Km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
