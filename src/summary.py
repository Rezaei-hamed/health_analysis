import pandas as pd

def summary(df):
    """
    Input: a DataFrame with columns "age", "weight", "height", "systolic_bp", "cholesterol"
    Outpput: aggregated metrics in a DataFrame, with mean values, medians, smallest and largest values for columns mentioned in function input.
    """
    age  = df['age']
    weight = df['weight']
    height = df['height']
    cholesterol = df['cholesterol']
    systolic = df['systolic_bp']

    summary = pd.DataFrame({
        "Age": [age.mean(), age.median(), age.min(), age.max()],
        "Weight": [weight.mean(), weight.median(), weight.min(), weight.max()],
        "Height": [height.mean(), height.median(), height.min(), height.max()],
        "Cholesterol": [cholesterol.mean(), cholesterol.median(), cholesterol.min(), cholesterol.max()],
        "Blood Pressure": [systolic.mean(), systolic.median(), systolic.min(), systolic.max()],
    }, index=["Mean","Median","Min", "Max"])

    return summary.round(1)