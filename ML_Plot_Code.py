import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("AEP_hourly.csv")
df.index = pd.to_datetime(df['Date Time'], format="%d-%m-%Y %H:%M")

dset = df
dset['Month'] = pd.to_datetime(df['Date Time']).dt.month
dset['Year'] = pd.to_datetime(df['Date Time']).dt.year
dset['Date'] = pd.to_datetime(df['Date Time']).dt.date
dset['Time'] = pd.to_datetime(df['Date Time']).dt.time
dset['Day'] = pd.to_datetime(df['Date Time']).dt.day_name()
dset = df.set_index("Date Time")
dset.index = pd.to_datetime(dset.index)

fig = plt.figure()
sns.lineplot(x = dset["Year"], y = dset["AEP_MW"], data = df)
sns.distplot(dset['AEP_MW'])
fig = plt.figure()
sns.lineplot(x = dset['Time'].astype(str), y = dset['AEP_MW'], data = df)

ndset = dset[["AEP_MW"]].resample('D').mean()
ndset.shape

test_data = ndset.tail(100)
Train_Set = ndset.iloc[:,0:1]
Train_Set = Train_Set[:-60]

sc = MinMaxScaler(feature_range=(0, 1))
Train = sc.fit_transform(Train_Set)

X_Train = []
Y_Train = []

for i in range(60,Train.shape[0]):
    X_Train.append(Train[i-60:i])
    Y_Train.append(Train[i])

X_Train = np.array(X_Train)
Y_Train = np.array(Y_Train)

Model = Sequential()

Model.add(LSTM(units = 50, return_sequences = True, input_shape = (X_Train.shape[1], 1)))
Model.add(Dropout(0.2))

Model.add(LSTM(units = 50, return_sequences = True))
Model.add(Dropout(0.2))

Model.add(LSTM(units = 50, return_sequences = True))
Model.add(Dropout(0.2))

Model.add(LSTM(units = 50))
Model.add(Dropout(0.2))

Model.add(Dense(units = 1))

Model.compile(optimizer = 'adam', loss = 'mean_squared_error')

Model.fit(X_Train, Y_Train, epochs = 50)
D_Tot = pd.concat((ndset[["AEP_MW"]], test_data[["AEP_MW"]]), axis=0)

inputs = D_Tot[len(D_Tot) - len(test_data) - 60:].values

inputs = inputs.reshape(-1,1)
inputs = sc.transform(inputs)
X_test = []
for i in range(60, 160):
    X_test.append(inputs[i-60:i])
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
predicted_stock_price = Model.predict(X_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

True_MegaWatt = test_data["AEP_MW"].to_list()
Predicted_MegaWatt  = predicted_stock_price
dates = test_data.index.to_list()

Machine_Df = pd.DataFrame(data={
    "Date":dates,
    "TrueMegaWatt": True_MegaWatt,
    "PredictedMeagWatt":[x[0] for x in Predicted_MegaWatt ]
})

x = dates
y = True_MegaWatt
y1 = Predicted_MegaWatt
plt.plot(x,y, color="green")
plt.plot(x,y1, color="red")
