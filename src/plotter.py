import matplotlib.pyplot as plt

def make_plots(df):
    """
    Input: a DataFrame with columns "sex", "weight", "systolic_bp", and "smoker".
    Output: a figure with 3 subplots, side by side. 
    To the right, a bar graph of how many smokers and non-smokers there are.
    In the center, a box plot of grouped gender weights.
    To the left, a histogram of blood pressure frequency.
    """
    fig, ax = plt.subplots(1,3, figsize=(7,3)) # 3 plots i samma figur

    # Plot till höger 
    # (stapeldiagram: andelen smoker)
    quantity_smokers = df['smoker'].value_counts()        # räknar hur många 'smoker' eller 'non smoker'
    ax[2].bar(quantity_smokers.index, quantity_smokers.values, edgecolor="black", color=["blue","red"])
    ax[2].set_title("Hur många som röker")

    # Plot i mitten 
    # (boxplot, weight by  gender)
    gender_weights = [df[df['sex']=="M"]['weight'], df[df['sex']=="F"]['weight']]            # lista med män's vikt och kvinnor's vikt
    ax[1].boxplot(gender_weights, tick_labels=['Male','Woman'])
    ax[1].set_title("weight by gender - distribution")

    # Plot längst till vänster 
    # (histogram över blodtryck)
    ax[0].hist(df["systolic_bp"], bins=25, edgecolor="black",color="cyan")
    ax[0].set_title("Blodtryck: distribution of values")

    fig.tight_layout()
    # plt.show()

    return fig, ax