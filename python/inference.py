import pandas as pd
import numpy as np
from tensorflow import keras
import math

environment_input_data_path = "./ev_data.csv" #인풋 데이터 경로
environment_input_data_path = "./environmentsB.csv" #인풋 데이터 경로
environment_input_df = pd.read_csv(environment_input_data_path)

early_input_data_path = "./growth_data.csv" #초기 생육 데이터 경로
early_input_data_path = "./p_b_growth_data.csv" #초기 생육 데이터 경로
early_input_df = pd.read_csv(early_input_data_path)

output_data_name = "output.csv" #출력데이터 이름

model_path = "./vvsb_preTest_model" #모델 경로
model = keras.models.load_model(model_path)


## 환경 데이터 전처리
input_x = environment_input_df.loc[:,"datetime":"innerSolar"]
input_x['date'] = input_x['datetime'].str[:10] 
input_x = input_x.groupby('date').mean()
input_x = input_x.reset_index(drop=False)

input_x['date'] = pd.to_datetime(input_x['date'])
input_x = input_x.set_index(['date'])

input_x = input_x.resample('W').mean()

# print(input_x) #<=확인 필요시 주석 해제

input_x = input_x.loc[:,'supplyEC':].to_numpy()
input_x = input_x.reshape(len(input_x),1,6)


# 모델에 데이터 삽입후 결과값 도출
predict_y = model.predict(input_x)
predict_y = predict_y.reshape(len(predict_y),9)

predict_y = np.insert(predict_y, 0,early_input_df.iloc[0,2:].to_numpy(),axis=0)


for i in range(1, len(predict_y)):
    for j in range(9):
        if predict_y[i-1][j] + predict_y[i][j] < 0 :
            if i == len(predict_y)-1:
                pass
            else:
                predict_y[i+1][j] = predict_y[i+1][j]+predict_y[i][j]
            predict_y[i][j] = 0
        else:
            predict_y[i][j] = predict_y[i][j] + predict_y[i-1][j]

for i in range(len(predict_y)):
    for j in range(9):
        if j == 4 or j == 6 or j == 7 or j == 8:
            predict_y[i][j] = math.ceil(predict_y[i][j])
            
            
result = pd.DataFrame(predict_y)

result.set_axis(labels=['초장(mm)','엽장(mm)','엽폭(mm)','엽병장(mm)','엽수(개)','관부직경(mm)','화방꽃수(소화수)(개)','착과수(개)','최종화방차수(차)'], axis = 1)
result.to_csv(output_data_name)


