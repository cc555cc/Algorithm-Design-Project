from UI import render_ui
from soh_model import train
import pandas as pd

def main():
    file = pd.read_excel('PulseBat Dataset.xlsx')
    train(file)
    render_ui()

  
if __name__ == "__main__":
    main()