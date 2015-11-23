import seaborn as sns
import pandas as pd
sns.set(style="whitegrid", palette="pastel", color_codes=True)

# load my data
qwi = pd.read_csv('qwi_graph_data.csv')

# Draw a nested violinplot and split the violins for easier comparison
#sns.violinplot(x="quarter", y="EarnS", hue="industry", data=qwi, split=True,
#               inner="quart", palette={52: "b", 54: "y"})


# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(x="quarter", y="EarnS", hue="industry_label.value", data=qwi, split=True,
               inner="quart", palette={"Finance and Insurance": "b", "Professional, Scientific, and Technical Services": "y"})


sns.despine(left=True)
sns.plt.ylim(0,)
sns.plt.title('Avg Quarterly Stable Earnings by Firm and Industry')


sns.plt.show()