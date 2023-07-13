import seaborn as sns
import matplotlib.pyplot as plt
t=sns.load_dataset('titanic')
print(t.columns)
emb_survival=t.groupby(['embarked'])['survived'].mean().reset_index()
sns.barplot(data=emb_survival,x='embarked',y='survived',hue='embarked')
plt.legend(title='embarked')
plt.show()



