import seaborn as sns
import matplotlib.pyplot as plt
t=sns.load_dataset('titanic')
print(t.columns)
survival=t.groupby(['sex','pclass'])['survived'].mean().reset_index()
sns.barplot(data=survival,x='pclass',y='survived',hue='sex')
plt.show()



