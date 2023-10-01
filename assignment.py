import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("Employee.csv")
DataFrame=pd.DataFrame(data)
dfh=DataFrame.head(20)
dfh.plot(x="Education",y="ExperienceInCurrentDomain",kind="bar",title="Employee Experience in the field",xlabel="Education", ylabel="Experience")
plt.show()