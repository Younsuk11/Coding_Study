import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

#sklearn
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict, cross_validate
from sklearn.metrics import mean_squared_error, mean_absolute_error, roc_curve, accuracy_score, f1_score

import pickle


#preprocessing & pandas
Train = df.drop(["target"], axis = 1)
y = df.target
train_x, train_y, test_X, test_y = train_test_split(Train,y, test_size = 0.2, random_state = 42)

#기본 확인
df.info()
df.columns
df.index

#변수 내 데이터 종류 확인
df.attributes.value_counts(sort = True)
df.attributes.unique()

#변수유형
df.describe()
df = df.astype({"attribute" : "float64"})
df.attribute = df.attribute.astype("category")
df_num = df.select_dtypes(include = ["float64", "int64"])
df_cat = df.select_dtypes(include = "object"

#인덱스 리셋
df.reset_index(drop = True, inplace = True)

#칼럼 제거 
df = df.drop(["attirbute"], axis = 1)

#데이터 확인
df.loc["조건문"]
df.iloc["행 index": "index"]

#merging : 열방향
df_new = df1.merge(df2, on = ["attribute"])


#concat : 단순 합치기
df_total = pd.concat([df_train, df_test], axis = 0)

#중복, 확인, 제거
df.duplicated(["attribute"])
df.drop_duplicateds(["attribtue"], keep = "first", inplace = True)

#결측치 확인
df.isna().sum()
df.isnull().sum()

#결측치 채우기
df.fillna(df.mean())
df.fillna(method = "bfill")
df.fillna(method = "ffill")

#결측치 제거
df.dropna(subset = ["attribute"], inplace = True, axis = 0)
df.dropna(how = "any")# 결측치 있으면 모두 지우기
df.dropna(how = "all")# 모든 변수가 결측치면 지우기
df.dropna(threshold = 3) # 정상값이 3개 미만인 행 지우기

#열 일괄 처리
#map 변수 하나
df.attribute= df.attribute.map(lambda x : function(x))
#apply 변수 여러개
df.attirbute = df.apply(lambda x: function(x.attribute1, x.attirbute2), axis = 1)


#save to excel
with pd.ExcelWriter("excel.xlsx") as writer:
    for key in keys:
        big_df[keys].to_excel(writer, sheet_name = "name", index = False)


#전처리

#수치형 변수 스케일링
scaler = StandardScaler() #MinMaxScaler() #np.log or np.log1p
df_num_train = scaler.fit_transform(df_num_train)
df_num_test = scaler.transform(df_num_test)

#범주형 변수 원핫 인코딩
df_dummies = pd.get_dummies(df_cat, drop_first = True) 
# 하지만, test에는 없는 값이면 없는 것에 대한 열을 만들지 않는다.

encoder = OneHotEncoder()
df_cat_train = encoder.fit_transform(df_cat_train)
df_cat_test = encoder.transform(df_cat_test)

#레이블 인코딩 : 범주형 변수 인코딩, ordinary형으로 만들어준다. -> 이는 잘 안쓴다.


#시계열 데이터 전처리(date에서 년, 월, 일 분리)
df.date = pd.to_dataframe(df.datetime) #변수 열 만들어주기
df.year = df.date.dt.year
df.month = df.date.dt.month
df.day = df.data.dt.dayofweek

#월요일 : 0
pd.date_range(start_date, end_date, freq = "D")



#구간 별로 데이터 라벨링하기
bins = [0,2,8,26,55]
labels = list(map(chr, range(ord("A")+len(bins)-2, ord("A")-1, -1)))
distributors = list(df.distributor.unique())
dis_counts = {}
for dis in distributors:
  dis_counts[dis] = df.distributor.value_counts()[dis]

df["distributor_counts"] = df["distributor"].map(lambda x : dis_counts[x])
df["distributor_group"]  = pd.cut(df.distributor_counts, bins = bins, labels = labels)
df.drop(["distributor", "distributor_counts"], axis = 1, inplace = True)


#EDA 시각화

#corr heatmap
corr = df_num.corr()
sns.heatmap(corr, annot = True)
plt.show()

#matplotlib
#subplot
plt.subplot(2,1,1) # 2x1중에서 1
plt.plot(df_train.attribute)

#크기 조정
plt.figure(figsize = (15,10))

#상위 제목
plt.suptitle("title", fontsize = 20, y = 0.9)

plt.plot(1.98, 0.15, 'ro', t2, f(t2), 'k') 
# x=1.98, y=0.15 에 빨간 점 찍고, x=t2, y=f(t2)에 그림 그려라

#각 축 label
plt.xlabel('x')
plt.ylabel('y blue', fontdict = {'size':15, 'color': 'blue'})


plt.grid(True, color='g', linestyle='--') 
plt.annotate('3rd max', xy=(2, 0.17), xytext=(2.5, 0.6), fontsize=15, arrowprops=dict(facecolor='blue', shrink=0.05))
# 화살표 추가 plt.subplot(2,2,3) 
# 2행 2열에서 세번째 부분 

plt.plot(t2, np.cos(2*np.pi*t2), 'r--', label= 'cos') 
plt.plot(4,1,marker='x', ms=8, mec = 'b', mew = 2) 
# ms: markersize/ mec: markeredgecolor, mew: markeredgewidth 

plt.title('2nd plot') 
plt.legend(loc='best') 
plt.subplot(2,2,(2,4)) 
# 2행 2열에서 두번째, 네번째 부분 

#산점
plt.scatter(data['a'], data['b'], c=data['c'], s=data['d'], cmap='jet')
# c: color, s: size 

plt.title('3rd plot') 
plt.xlabel('x 축') 
plt.ylabel('y 축') 
plt.subplots_adjust(top=0.8, bottom=0.28, left=0.10, right=0.95, hspace=0.5, wspace=0.2) 
# subplot layout 조절 /hspace : subplot간 위아래 공간, wspace : subpot간 좌우 공간 


#roc curve
fpr, tpr, thresholds = roc_curve(Y, predicted_Y, pos_label = 1)
auc = np.trapz(fpr, tpr)
plt.plot(fpr, tpr, label = "label")
plt.xlabel("False positive Rate")
plt.ylabel("True positive Rate")
plt.legend()
plt.show()


#seaborn

sns.scatterplot(x = df_train.attribute, y = df_train.target)

#pair plot
sns.pairplot(df_num)
plt.show()


#sns dataset
iris = sns.load_dataset("iris")    # 붓꽃 데이터
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터
tips = sns.load_dataset("tips")    # 팁 데이터
flights = sns.load_dataset("flights")


#라벨별 평균 비교
mean = df[["target", "attribute"]].groupby(["target"], as_index = False).mean()
sns.barplot(x = "target", y = "attribute", data = mean, color = "color")
plt.show()

#빈도수
sns.countplot(df.attribute)




#모델링
#단순 모델
model = LinearRegression()
model.fit(train_x, train_y)
predicted_y = model.predict(test_x)
score = mean_squared_error(test_y, predicted_y)

##linear regression
beta = model.coef_
intercept = model.intercept_
score_R_square = model.score(train_x, train_y)

#cross validation
#1) Kfold
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold

kf = KFold(n_splits = 5, shuffles = True, random_state = 50)

acc = []
for train_index, test_index in kf.split(Train):
    train_x, test_x = Train[train_index], Train[test_index]
    train_y, test_y = y[train_index], y[test_index]

    model = RandomForestClassifier(n_estimator = 5, random_state =42)
    model.fit(train_x, train_y)
    
    pred_y = model.predict(test_x)

    acc.append(accuracy_score(teest_y, pred_y))


#2) cross_vlidate

cv_model = cross_validate(model, Train ,y, cv = 5, scoring = ("neg_mean_squared_error"), return_train_score = True)
nmae = cv_model["test_score"]
mae = (-1*name).mean()


#3) GridSearchCV
from sklearn.ensemble import ExtraTreesRegressor

extratree = ExtraTreesRegressor(random_state = 42)

                  
param_distribs = {"n_estimators"  : np.arange( 200, 1000, 100) ,"max_features" : np.arange(8,11, 1),
                  "max_depth" : np.arange(5, 20,5) }
                  
gridcv_et = GridSearchCV(extratree, param_grid = param_distribs,cv = 5, scoring = "neg_mean_squared_error", n_jobs = -1, refit = True)

gridcv_et.fit(X_train,y_train)
bm_et_grid = gridcv_et.best_estimator_

bm_et_grid.fit(X_train, y_train)
predictions5 = bm_et_grid.predict(X_val)

#결과:
print("Best estimator:", bm_et_grid)
print(bm_et_grid.feature_importances_)
print(X_train.columns)
visualization(y_val, predictions5)


#model 저장
import pickle
# save
with open('lasso_dinner_lunch.pkl','wb') as f:
    pickle.dump(lasso_dinner_lunch,f)

#load
with open('lasso_dinner_lunch.pkl', 'rb') as f:
    model= pickle.load(f)