import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider, FloatSlider, fixed, VBox, HBox, Label
import ipywidgets as widgets

import helper_functions as hf

def plot_doppeltrapezfluegel(l_a, l_k, AR):
    # Flügeleckpunkte generieren
    points = hf.doppeltrapezfluegel(l_a, l_k, AR)

    # Geometrie plotten
    plt.figure(figsize=(10, 6))
    plt.plot(points[:,0], points[:, 1], '-', color="black")
    plt.vlines(0, -0.5, 0.5, "black", "--")
    plt.xlabel('Spannweite [m]')
    plt.ylabel('Flügeltiefe [m]')
    plt.title('Doppeltrapezflügel')
    plt.axis('equal')
    plt.show()

def widget_doppeltrapezfluegel():
    # Slider
    slider_l_k = VBox([Label('Flügeltiefe Kink'), FloatSlider(value=0.8, min=0, max=1.0, step=0.1)])
    slider_l_a = VBox([Label('Flügeltiefe außen'), FloatSlider(value=0.5, min=0, max=1.0, step=0.1)])
    slider_AR = VBox([Label('Streckung'), FloatSlider(value=10, min=5, max=20, step=1)])

    # Interaktiver plot
    ui = VBox([slider_l_k, slider_l_a, slider_AR])
    ui = VBox([ui], layout=widgets.Layout(justify_content='center'))
    out = widgets.interactive_output(plot_doppeltrapezfluegel, {'l_a': slider_l_a.children[1], 'l_k': slider_l_k.children[1], 'AR': slider_AR.children[1]})

    return HBox([out, ui])

def plot_diskretisierung_doppeltrapez(l_a, l_k, y_lk, AR, s, N):
    points = hf.doppeltrapezfluegel(l_a, l_k, AR)
    
    # Diskretisierung der Halbspannweite
    y_values = np.linspace(-s, s, N+1)
    
    chord_values = [hf.tiefe_doppeltrapez(y, y_lk, l_k, l_a, s) for y in y_values]
    
    # Geometrie plotten
    plt.figure(figsize=(10, 6))
    plt.plot(points[:,0], points[:, 1], '-', color="black")

    # Elementarflügel plotten
    for i in range(N):
        plt.plot([y_values[i], y_values[i]], [-chord_values[i]/2, chord_values[i]/2], 'g-')
    
    plt.vlines(0, -0.5, 0.5, "black", "--")
    plt.xlabel('Spannweite [m]')
    plt.ylabel('Flügeltiefe [m]')
    plt.title('Diskretisierung Doppeltrapezflügel')
    plt.axis('equal')
    plt.grid(True)
    plt.show()


def widget_diskretisierung_doppeltrapez(l_a, l_k, y_lk, AR, s):
    # Slider
    slider_N = VBox([Label('Anzahl der Elementarflügel'), IntSlider(value=30, min=1, max=100, step=1)])

    # Interaktiver plot
    ui = VBox([slider_N])
    ui = VBox([ui], layout=widgets.Layout(justify_content='center'))
    out = widgets.interactive_output(hf.plot_diskretisierung_doppeltrapez, {'l_a': fixed(l_a), 'l_k': fixed(l_k), "y_lk": fixed(y_lk), 'AR': fixed(AR), "s": fixed(s), 'N': slider_N.children[1]})
    return HBox([out, ui])


def plot_auftriebsverteilung(A_j, y_c, s):

    # Erweitere A_distr und y_c am Anfang und Ende um an den tips auf 0 zu plotten
    A_j = np.insert(A_j, 0, 0)
    A_j = np.append(A_j, 0)
    y_c = np.insert(y_c, 0, -s)
    y_c = np.append(y_c, s)

    # Berechne die Fläche unter der berechneten Auftriebsverteilung
    area_distr = np.trapz(A_j, y_c)
    
    # Erzeuge die elliptische Auftriebsverteilung
    y_elliptisch = np.linspace(-s, s, len(y_c))
    A_elliptisch_raw = np.sqrt(1 - (y_elliptisch / s) ** 2)
    
    # Skaliere die elliptische Verteilung so, dass die Flächen gleich sind
    area_elliptisch_raw = np.trapz(A_elliptisch_raw, y_elliptisch)
    scale_factor = area_distr / area_elliptisch_raw
    A_elliptisch = A_elliptisch_raw * scale_factor

    # Plotten der Auftriebsverteilungen
    plt.figure(figsize=(10, 6))
    plt.plot(y_c, A_j, '-', color="black", label='Berechnete Auftriebsverteilung')
    plt.plot(y_elliptisch, A_elliptisch, '--', color="red", label='Elliptische Auftriebsverteilung')
    plt.xlabel('Spannweite [m]')
    plt.ylabel('Auftrieb [N]')
    plt.title('Auftriebsverteilung')
    plt.legend()
    plt.show()