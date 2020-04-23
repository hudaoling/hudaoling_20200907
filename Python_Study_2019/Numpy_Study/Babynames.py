import pandas as pd
import  matplotlib
import  pylab
import  numpy as np
names1880=pd.read_csv('D:\\PythonProject\\hanlp_study\\pydata-book-2nd-edition\\datasets\\babynames\\yob1880.txt',names=['name','sex','births'])
#print(names1880[:10])
#print(names1880.dtypes,names1880.info)

#groupby.sum是分类汇总，size是分类计数
# print(names1880.groupby('sex').sum())
# print(names1880.groupby('sex').size())

#--------将所有出生文件（1880-2011）打开为一个文件names--------
years=range(1880,2011)
pieces=[]
columns=['name','sex','births']
for year in years:
    path='D:\\PythonProject\\hanlp_study\\pydata-book-2nd-edition\\datasets\\babynames\\/yob%d.txt'%year
    frame=pd.read_csv(path,names=columns)
    frame['year']=year
    pieces.append(frame)
    #print(pieces)
names=pd.concat(pieces,ignore_index=True)#将所有读取文件连接起来

#--------分组计算的方法----------
# print(names.year.value_counts())#按年计数
# print(names.sex.value_counts())#按性别计数
# print(names.groupby(['sex']).size())#size()和value_counts()功能相同
# max_groupby_year_sex=names.groupby(['year','sex']).max()  #按年/性别分组的，最大计数
#print(max_groupby_year_sex)
# mean_groupby_year_sex=names.groupby(['year','sex']).mean()#按年/性别分组的，算平均值
# print(mean_groupby_year_sex)
#print(names.groupby(['year']).agg(['max','min','mean']))
#agg是调用系统函数，apply调用用户自定义函数

#--------pivot_table数据透视，统计不同性别不同年份的出生人数（年趋势）--------
# total_births=names.pivot_table('births',index='year',columns='sex',aggfunc=['sum'])
# #print(total_births)
# total_births.plot(title='Total births by sex and year')
# pylab.show()

#--------groupby分组聚合函数,每个名字占所有初生儿名字的比率--------
def add_prop(group):
    births=group.births.astype(float)
    group['prop']=births/births.sum()
    return group
names=names.groupby(['year','sex']).apply(add_prop)
#print(names)
#print(np.allclose(names.groupby(['year','sex']).prop.sum(),1))  #验证占比总和是否是1


#--------取出top1000--------
def get_top1000(group):
    return group.sort_values(by=['births'],ascending=False)[:1000]
grouped=names.groupby(['year','sex'])
top1000=grouped.apply(get_top1000)

boys=top1000[top1000.sex=='M']
girls=top1000[top1000.sex=='F']
#print(boys,"&&&",girls)
total_births=top1000.pivot_table('births',index='year',columns='name',aggfunc=sum)
subset=total_births[['John','Harry','Mary','Marilyn']]
subset.plot(subplots=True,figsize=(12,10),grid=False,title='Number of births per year')
pylab.show()
