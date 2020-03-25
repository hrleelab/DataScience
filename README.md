# DataScience
Implementing simple data analysis

# Python for Data Science
## Basic functions
* 문자열
```python
# 문자열을 str 변수에 담기
str = " 자주 사용되는 파이썬 함수 정리 "

# 앞뒤 공백 제거
str = str.strip()

# 공백으로 문자열 분리
str_list = str.split()

# 슬라이싱으로 문자 가져오기
str[:2]

# startwith로 특정 문자열로 시작하는지 여부 확인
str.startwith("자주")

# in으로 특정 문자열 포함 여부 확인
"함수" in str
```
* 리스트
```python
# 리스트로 분리된 문자열을 다시 공백을 사이에 두고 연결
" ".join(str_list)

# in으로 특정 리스트 원소 포함 여부 확인
"사용" in str_list
```
## Pandas
-  [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/version/1.0.0/getting_started/10min.html)
-  [Pandas_Cheat_Sheet](http://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
```python
import pandas as pd
```
* 데이터 프레임
```python
# DataFrame : 2차원 구조(행렬)
df = pd.DataFrame(
{"a" : [4, 5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])

# Series : 1차원 구조(벡터)
df["a"]

# Series to DataFrame
df[["a"]]

# Subset
df[df["a"] > 4] # Row 기준
df[["a", "b"]] # Column 기준 (2개 이상 가져올 때는 항상 Series가 아닌 DataFrame형식으로 가져와야 함)

# Data 미리 보기
df.head(10) # Select first 10 rows
df.tail(10) # Select last 10 rows
```
* Summarize Data
```python
# categorical values의 빈도 수 (Count number of rows with each unique value of variable)
df['w'].value_counts()

# Count number of rows in DataFrame
len(df)

# Count number of distinct values in a column
df['w'].nunique()

# Basic descriptive statics for each column (or GroupBy)
df.describe()
```
* Reshaping Data
```python
# Sort
df["a"].sort_values()

# Order rows by values of a column (low to high)
df.sort_values("a")

# Order rows by values of a column (high to row)
df.sort_values("a", ascending=False)

# Drop columns from DataFrame
df.drop(["c"], axis=1) # axis=0은 행 기준
df.drop(columns=['Length', 'Height'])
```
* Group Data
```python
# Return a GroupBy object, grouped by values in column named "col"
df.groupby(["a"])["b"].mean() # 컬럼 "a"를 기준으로 컬럼 "b"의 평균값을 구한다
df.groupby(["a"])["b"].agg(["mean", "sum", "count"])
df.groupby(["a"])["b"].describe()

# Pivot table
pd.pivot_table(df, index="a") # 기본 aggregate function은 평균
pd.pivot_table(df, index="a", values="b", aggfunc="sum")
```
* Plotting
```python
df.plot()
df.plot.area() # 면적 색깔
df.plot.bar() # 막대 그래프
df.plot.density() # 밀도 함수
```
