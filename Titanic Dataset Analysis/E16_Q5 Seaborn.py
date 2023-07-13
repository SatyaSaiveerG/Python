import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
t=sns.load_dataset('titanic')
t=t.dropna(subset=['age','sex','pclass'])
print(t.columns)
age_bin=[0,10,20,30,40,50,60,70,80,90,100]
age_label=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']
t['AgeGroup']=pd.cut(t['age'],bins=age_bin,labels=age_label)
age_survival=t.groupby(['AgeGroup','sex','pclass'])['survived'].mean().reset_index()
plt.subplot(1,2,1)
sns.barplot(data=age_survival,x='AgeGroup',y='survived',hue='sex',errorbar=None)
plt.legend(title='sex')
plt.subplot(1,2,2)
sns.barplot(data=age_survival,x='AgeGroup',y='survived',hue='pclass',errorbar=None)
plt.legend(title='pclass')
plt.show()



