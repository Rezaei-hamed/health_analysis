import matplotlib.pyplot as plt

def bonus_plot_bp_age(df, ax):
    """
    Bonusgraf från del 1: En scatterplot som visar ålder mot blodtryck, med rullande medel och punkter uppdelade efter kön.
    Jag ändrade koden från ax.figure() till fig, ax = plt.subplots() och la till ax som argument.
    Funktionen returnerar fig och ax.


    Bonus graf från del 1: En scatterplot ålder vs blodtryck, med rullande medel, och könsfördelade punkter för extra nyans.
    Fick ändra på koden från ax.figure() till fig, ax = ax.subplots(), och lägga till ax som input argument.
    Returnerar fig, ax.
    """
    colors = df.sex.map({"F":"green", "M":"blue"})
    ax.scatter(df['age'], df['systolic_bp'], c=colors, alpha=0.75, label="Person Values")
    ax.set_title("Ålder (by gender) VS Blodtryck")
    ax.set_xlabel("Age")
    ax.set_ylabel("Blood pressure")

    # Lägga till rullande medel
    sorted = df[['age','systolic_bp']].sort_values('age') # sortera åldrarna stigande.
    roll_mean = sorted['systolic_bp'].rolling(window=25).mean() # 30 första värden visar där rullande medel ska starta.

    ax.plot(sorted['age'], roll_mean, linewidth=2.5, label="Rolling mean value")