import seaborn as sns
import matplotlib.pyplot as plt
t=sns.load_dataset('titanic')
print(t.columns)
survival=t.groupby('pclass')['survived'].mean().reset_index()
sns.barplot(data=survival,x='pclass',y='survived')
plt.show()


