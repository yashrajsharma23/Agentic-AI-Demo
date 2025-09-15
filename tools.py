import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from typing import Dict, Any
import os

class DataAnalysisTools:
    def __init__(self):
        self.current_df = None

    def load_csv(self,file_path:str) -> str:
        try:
            self.current_df=pd.read_csv(file_path)
            info = f"Loaded CSV with {len(self.current_df)} rows and {len(self.current_df.columns)} Columns\n"
            info += f"Columns: {', '.join(self.current_df.columns)}\n"
            info += f"Data Types:\n{self.current_df.dtypes}"
            return info
        except Exception as e:
            return f"Error loading CSV: {str(e)}"

    def get_summary_stats(self) -> str:
        if self.current_df is None:
            return "No data loaded, please load a CSV first."

        return str(self.current_df.describe())
    
    def create_visualization(self, chart_type: str, x_column:str, y_column:str =None )-> str:
        if self.current_df is None:
            return "No data loaded, please load a CSV first."
        
        try:
            if chart_type =="histogram":
                plt.fugure(figsize=(10,6))
                plt.hist(self.current_df[x_column], bins=30)
                plt.title(f"Histogram of {x_column}")
                plt.xlabel(x_column)
                plt.ylabel("Frequency")
                plt.savefig("visualization.png")
                plt.close()

            elif chart_type=="scatter" and y_column:
                fig = px.scatter(self.current_df, x=x_column, y=y_column,
                                 title=f"Scatter plot: {x_column} vs {y_column}")
                fig.write_html("Visualization.html")

            return f"Created {chart_type} visualization saved as visualization.png/html"
        except Exception as e:
            return f"Error creating visualization: {str(e)}"