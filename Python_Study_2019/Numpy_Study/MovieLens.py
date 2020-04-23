import  pandas as pd
import  numpy as np

#pd.read_table读取文件
unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('D:\\PythonProject\\hanlp_study\\pydata-book-2nd-edition\\datasets\\movielens\\users.dat',sep='::',header=None,names=unames)
rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('D:\\PythonProject\\hanlp_study\\pydata-book-2nd-edition\\datasets\\movielens\\ratings.dat',sep='::',header=None,names=rnames)
mnames=['movie_id','title','genres']
movies=pd.read_table('D:\\PythonProject\\hanlp_study\\pydata-book-2nd-edition\\datasets\\movielens\\movies.dat',sep='::',header=None,names=mnames)
# print(users[:5])
# print(users)
# print(type(ratings))#<class 'pandas.core.frame.DataFrame'>

#pd.merge多表链接
data=pd.merge(pd.merge(ratings,users),movies)
# print(data)
# print(data.info)#表基本信息（维度、列名称、数据格式、所占空间等）
# print(type(data))#<class 'pandas.core.frame.DataFrame'>
# print(data.dtypes)#列格式
# print(data.shape)#维度查询 #(1000209, 10)
print(data.columns)#列名称
#print(data.head()) #默认前10行数据
# data.tail()  #默认后10 行数据


#pd.pivot_table和数据透视表类似功能
#mean_ratings=pd.pivot_table(data,index=['title'],columns='gender',values=['rating'],aggfunc=np.mean,np.sum)
mean_ratings=data.pivot_table('rating',index='title',columns='gender',aggfunc=['mean'])
#values=rating值是电影评分,index=title索引是电影标题，列是gender,计算类型是平均值和总分
#index可以是多个，相当于groupby里的字段
# print(mean_ratings)

#groupby,size()分类计数
ratings_by_title=data.groupby('title').size()
#print(ratings_by_title)

#index索引，取出计数大于250条记录的电影
active_titles=ratings_by_title.index[ratings_by_title>=250]
#print(active_titles)
mean_ratings=mean_ratings.loc[active_titles,:]#ix是dataframe切片功能
#print(mean_ratings)

#sort_index 排序
top_female_ratings=mean_ratings.sort_values(by=['F'],ascending=False)#按'F'列排序
print(top_female_ratings)

# sorted_by_diff=mean_ratings.sort_index(by='diff')
# print(sorted_by_diff)