from sklearn.linear_model import LinearRegression
from scipy.stats import chi2 as chisqr
from scipy import stats as stats
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, r2_score
linreg = LinearRegression()

X = final_df['Imdb_Score']
y = final_df['Worldwide Box Office']
model = sm.OLS(y, X).fit()
predictions = model.predict(X)
model.summary()

from sklearn.model_selection import train_test_split
Y = final_df['Worldwide Box Office'].values.reshape(-1, 1)
X = final_df['Imdb_Score'].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,random_state=10)
linreg.fit(X_train,y_train)
pred = linreg.predict(X_test)
print(linreg.coef_)
print(linreg.intercept_)
plt.scatter(y_test,pred)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, pred)))

y = final_df['Imdb_Score'].values.reshape(-1, 1)
x = final_df['Worldwide Box Office'].values.reshape(-1, 1)
linreg.fit(x,y)
y_pred = linreg.predict(x)
linreg.score(x,y)

fig,ax = plt.subplots()
ax.scatter(x, y, color='green')
ax.plot(x, y_pred, color='black')
x_label = 'Imdb Ratings Score'

#Multiple Regression with all three ratings
reg = LinearRegression()
reg.fit(X_train[['Rotten_Score','Metacritic_Score','Imdb_Score']], y_train)
y_predicted = reg.predict(X_test[['Rotten_Score','Metacritic_Score','Imdb_Score']])
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_predicted))
print('R²: %.2f' % r2_score(y_test, y_predicted))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_predicted)))

y = final_df[['Metacritic_Score','Rotten_Score','Imdb_Score']].values.reshape(-1,1)
x = final_df['Worldwide Box Office'].values.reshape(-1,1)
linreg.fit(x,y)
y_pred = linreg.predict(x)
linreg.score(x,y)
