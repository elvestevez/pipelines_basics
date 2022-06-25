from macquisition import acquisition as mac
from mwrangling import wrangling as mwr
from manalysis import analysis as man

input_year = int(input("Introduzca año de fabricación: "))

def main():
    df_raw = mac.acquisition('./data/vehicles.csv')
    df_wrangled = mwr.wrangling(df_raw, 1997)
    analyzed = man.analysis(df_wrangled, 'Make', 'Combined MPG','./data/resultfinal.csv')
    print(analyzed)

# Pipeline
if __name__ == '__main__':
    main()
