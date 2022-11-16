import pandas as pd
import matplotlib.pyplot as plt


class Set_match1:
    def __int__(self):
        pass

    def dataframe(self):
        data = {
            "calories": [420, 380, 390],
            "duration": [50, 40, 45]
        }
        df = pd.DataFrame(data, index=["day1", "day2", "day3"])

        print(df)
        print(df.loc["day2"])

    def series(self):
        a = [1, 7, 2]

        myvar = pd.Series(a, index=["x", "y", "z"])

        print(myvar)

obj = Set_match1()
obj.dataframe()
obj.series()
