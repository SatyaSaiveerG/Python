import seaborn as sns
import matplotlib.pyplot as plt
t=sns.load_dataset('titanic')
print(t.columns)
survival=t.groupby('sex')['survived'].mean().reset_index()
sns.barplot(data=survival,x='sex',y='survived')
plt.show()


