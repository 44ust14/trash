# Based on patent https://www.google.com/patents/US7251579
# Not responsible if you use this for anything other than personal use
from math import sqrt


def realfeel(W,  # windspeed mph
             A,  # pressure mb
             T,  # temperature F
             UV,  # UV Index
             D,  # Dew Point F
             P2,  # preciptation Factor from 0-5
             ):
    if W < 4:
        Wa = W / 2 + 2
    elif W < 56:
        Wa = W
    else:
        Wa = 56

    #	print Wa
    WSP2 = (80 - T) * (0.566 + 0.25 * sqrt(Wa) - 0.0166 * Wa) * ((sqrt(A / 10)) / 10)
    WSP1 = sqrt(W) * ((sqrt(A / 10)) / 10)
    #	print WSP2

    SI2 = UV  # UV index is already in hectoJoules/m^2 ?

    if D >= (55 + sqrt(W)):
        Da = D
    else:
        Da = 55 + sqrt(W)

    #	print Da

    H2 = (Da - 55 - sqrt(W)) ** 2 / 30

    #	print H2

    if T >= 65:
        MFT = 80 - WSP2 + SI2 + H2 - P2
    else:
        MFT = T - WSP1 + SI2 + H2 - P2
    return MFT


print
realfeel(5, 1013, 70, 6, 50, 0)