import numpy as np

def doppeltrapezfluegel(l_a, l_k, AR, l_i=1.0) -> np.array:
    """
    Generiert die Planform eines Doppeltrapezflügels in Form von Eckpunkten auf Basis der gegebenen 
    Flügeltiefen und der Streckung.

    Args:
        l_a (float): Flügeltiefe außen
        l_k (float): Flügeltiefe Kink
        AR (float): Streckung
        l_i (float, optional): Flügeltiefe innen. Defaults to 1.0.

    Returns:
        np.array: Array aus Flügeleckpunkten zum plotten
    """
    # Berechnung der Halbspannweite
    b = AR * (l_k*0.75 + 0.5*(l_i-l_k)*0.75+l_a*(1-0.75)+0.5*(l_k-l_a)*0.25)
    s = b / 2

    # Berechnung der Kink-Position (bei 75% der Halbspannweite)
    y_lk = 0.75 * s 

    # Definition dller Eckpunkte
    points = np.array([
        [0, l_i/2],              
        [y_lk, l_k/2],    
        [s, l_a/2],         
        [s, -l_a/2],         
        [y_lk, -l_k/2],         
        [0, -l_i/2],
        [-y_lk, -l_k/2],  
        [-s, -l_a/2],    
        [-s, l_a/2] ,         
        [-y_lk, l_k/2],
        [0, l_i/2]
    ])
    
    return points


def tiefe_doppeltrapez(y, y_lk, l_k, l_a, s) -> float:
    """Berechnet mit gegebenen Geometriepartametern eines Doppeltrapezflügels die lokale Flügeltiefe für eine spannweitige Position

    Args:
        y (float): spannweitige Position
        y_lk (float): spannweitige Kink-Position
        l_k (float): Flügeltiefe Kink
        l_a (float): Flügeltiefe außen
        s (float): Halbspannweite

    Returns:
        float: lokale Flügeltiefe
    """
    y = abs(y)
    if y <= y_lk:
        return 1 + (l_k - 1) * (y / y_lk)
    else:
        return l_k + (l_a - l_k) * ((y - y_lk) / (s - y_lk))
        