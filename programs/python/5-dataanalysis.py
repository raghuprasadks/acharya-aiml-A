import pandas as pd
import matplotlib.pyplot as plt
print("pandas series")
sales =pd.Series([100,200,250,150,300])
print("sales series")
print(sales)
print("data type ",type(sales))
print("shape ",sales.shape)
countries={
    "Country":["India","USA","China","Germany","Japan"],
    "Capital":["New Delhi","Washington DC","Beiging","Berlin","Tokyo"],
    "GDP":[4.1,27,18,4.7,4.2],
    "GDPRank":[5,1,2,4,3],
}
topce = pd.DataFrame(countries)
print("data frame ",topce)
print("shape ",topce.shape)
print("rows ",topce.shape[0],"columns ",topce.shape[1])
print("country")
print(topce["Country"])
print("gdp")
print(topce.GDP)
topc = topce.sort_values("GDPRank",ascending=True)
print(topc)
print("line chart")
plt.title("Top economies in the world")
plt.xlabel("Country")
plt.ylabel("GDP")
#plt.plot(topc.Country,topc.GDP)
#plt.scatter(topc.Country,topc.GDP)
#plt.bar(topc.Country,topc.GDP)
plt.pie(topc.GDP,labels=topc.Country)
plt.show()


