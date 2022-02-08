from pathlib import Path
import pandas as pd


data_dir_name ="AWS"
filename="Wet Station Table1.xlsx"
this_dir=Path.cwd()
data_dir=this_dir.parent/Path(data_dir_name)
data=data_dir/Path(filename)

xls = pd.ExcelFile(str(data))
df1 = pd.read_excel(xls, 'Sheet1',header=4)
df2 = pd.read_excel(xls, 'Sheet2',header=1)
