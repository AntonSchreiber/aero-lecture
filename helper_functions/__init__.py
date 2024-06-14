from .aerodynamics import lifting_line_method, vortex_lattice_method
from .plotting import plot_doppeltrapezfluegel, widget_doppeltrapezfluegel, plot_diskretisierung_doppeltrapez, widget_diskretisierung_doppeltrapez, plot_auftriebsverteilung
from .helper import doppeltrapezfluegel, tiefe_doppeltrapez

__all__ = [
    "lifting_line_method", 
    "vortex_lattice_method",

    "plot_doppeltrapezfluegel",
    "widget_doppeltrapezfluegel"
    "plot_diskretisierung_doppeltrapez",
    "widget_diskretisierung_doppeltrapez",
    "plot_auftriebsverteilung"

    "doppeltrapezfluegel",
    "tiefe_doppeltrapez"
]