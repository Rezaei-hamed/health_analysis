# klassen som skapar grafer och räknar ut statistik ( plotter.py och summary.py i src packetet )

# importera dataclass, lite mindre robust men lättare skriven.
from dataclasses import dataclass
import pandas as pd, matplotlib.pyplot as plt


# att importera in  summary och plotter funktionerna in i  src paketet

from .summary import summary
from .plotter import make_plots

@dataclass
class Analysis_class:
    """
    Skapa ett objekt som innehåller en numerisk sammanfattning och genererar tre olika diagram.
    """
    df: pd.DataFrame

    def assign_plots(self):
        """
        Använder funktioner från 'plotter.py' för att ge attribut till ett Analysis_class-objekt.
        """
        make_plots(self.df)

    def assign_summary(self):
        """
        Använder funktion från 'summary.py' för att ge ett DataFrame-attribut till ett Analysis_class-objekt.
        """
        return summary(self.df)
