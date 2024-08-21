import pandas as pd

df = pd.read_excel("./prev_growthdata.xlsx", engine='openpyxl')

df_of_b = df[df['시설아이디'].str.contains('B농가')]
df_of_c = df[df['시설아이디'].str.contains('C농가')]
df_of_d = df[df['시설아이디'].str.contains('D농가')]
df_of_e = df[df['시설아이디'].str.contains('E농가')]
# 농장별 분류
df_of_b.to_csv('b_growth_sample.csv', index = False)
df_of_c.to_csv('c_growth_sample.csv', index = False)
df_of_d.to_csv('d_growth_sample.csv', index = False)
df_of_e.to_csv('e_growth_sample.csv', index = False)
# 수치 종류를 행으로

p_df_of_b = pd.DataFrame({})
p_df_of_c = pd.DataFrame({})
p_df_of_d = pd.DataFrame({})
p_df_of_e = pd.DataFrame({})

n_growthDataTypes = 9

p_df_of_b['시설아이디'] = df_of_b['시설아이디'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_b['생육주사'] = df_of_b['생육주사'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_b['조사일자'] = df_of_b['조사일자'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_b['표본번호'] = df_of_b['표본번호'][::n_growthDataTypes].reset_index(drop=True)

p_df_of_b['초장(mm)'] = df_of_b.loc[df_of_b['조사항목'] == '초장', ['조사항목값']].reset_index(drop=True)
p_df_of_b['엽장(mm)'] = df_of_b.loc[df_of_b['조사항목'] ==  '엽장', ['조사항목값']].reset_index(drop=True)
p_df_of_b['엽폭(mm)'] = df_of_b.loc[df_of_b['조사항목'] == '엽폭', ['조사항목값']].reset_index(drop=True)
p_df_of_b['엽병장(mm)'] = df_of_b.loc[df_of_b['조사항목'] == '엽병장', ['조사항목값']].reset_index(drop=True)
p_df_of_b['엽수(개)'] = df_of_b.loc[df_of_b['조사항목'] == '엽수', ['조사항목값']].reset_index(drop=True)
p_df_of_b['관부직경(mm)'] = df_of_b.loc[df_of_b['조사항목'] == '관부직경', ['조사항목값']].reset_index(drop=True)
p_df_of_b['화방꽃수(소화수)(개)'] = df_of_b.loc[df_of_b['조사항목'] == '화방 꽃수(소화수)', ['조사항목값']].reset_index(drop=True)
p_df_of_b['착과수(개)'] = df_of_b.loc[df_of_b['조사항목'] == '착과수', ['조사항목값']].reset_index(drop=True)
p_df_of_b['최종화방차수(차)'] = df_of_b.loc[df_of_b['조사항목'] == '최종화방차수', ['조사항목값']].reset_index(drop=True)



p_df_of_c['시설아이디'] = df_of_c['시설아이디'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_c['생육주사'] = df_of_c['생육주사'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_c['조사일자'] = df_of_c['조사일자'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_c['표본번호'] = df_of_c['표본번호'][::n_growthDataTypes].reset_index(drop=True)

p_df_of_c['초장(mm)'] = df_of_c.loc[df_of_c['조사항목'] == '초장', ['조사항목값']].reset_index(drop=True)
p_df_of_c['엽장(mm)'] = df_of_c.loc[df_of_c['조사항목'] ==  '엽장', ['조사항목값']].reset_index(drop=True)
p_df_of_c['엽폭(mm)'] = df_of_c.loc[df_of_c['조사항목'] == '엽폭', ['조사항목값']].reset_index(drop=True)
p_df_of_c['엽병장(mm)'] = df_of_c.loc[df_of_c['조사항목'] == '엽병장', ['조사항목값']].reset_index(drop=True)
p_df_of_c['엽수(개)'] = df_of_c.loc[df_of_c['조사항목'] == '엽수', ['조사항목값']].reset_index(drop=True)
p_df_of_c['관부직경(mm)'] = df_of_c.loc[df_of_c['조사항목'] == '관부직경', ['조사항목값']].reset_index(drop=True)
p_df_of_c['화방꽃수(소화수)(개)'] = df_of_c.loc[df_of_c['조사항목'] == '화방 꽃수(소화수)', ['조사항목값']].reset_index(drop=True)
p_df_of_c['착과수(개)'] = df_of_c.loc[df_of_c['조사항목'] == '착과수', ['조사항목값']].reset_index(drop=True)
p_df_of_c['최종화방차수(차)'] = df_of_c.loc[df_of_c['조사항목'] == '최종화방차수', ['조사항목값']].reset_index(drop=True)




p_df_of_d['시설아이디'] = df_of_d['시설아이디'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_d['생육주사'] = df_of_d['생육주사'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_d['조사일자'] = df_of_d['조사일자'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_d['표본번호'] = df_of_d['표본번호'][::n_growthDataTypes].reset_index(drop=True)

p_df_of_d['초장(mm)'] = df_of_d.loc[df_of_d['조사항목'] == '초장', ['조사항목값']].reset_index(drop=True)
p_df_of_d['엽장(mm)'] = df_of_d.loc[df_of_d['조사항목'] ==  '엽장', ['조사항목값']].reset_index(drop=True)
p_df_of_d['엽폭(mm)'] = df_of_d.loc[df_of_d['조사항목'] == '엽폭', ['조사항목값']].reset_index(drop=True)
p_df_of_d['엽병장(mm)'] = df_of_d.loc[df_of_d['조사항목'] == '엽병장', ['조사항목값']].reset_index(drop=True)
p_df_of_d['엽수(개)'] = df_of_d.loc[df_of_d['조사항목'] == '엽수', ['조사항목값']].reset_index(drop=True)
p_df_of_d['관부직경(mm)'] = df_of_d.loc[df_of_d['조사항목'] == '관부직경', ['조사항목값']].reset_index(drop=True)
p_df_of_d['화방꽃수(소화수)(개)'] = df_of_d.loc[df_of_d['조사항목'] == '화방 꽃수(소화수)', ['조사항목값']].reset_index(drop=True)
p_df_of_d['착과수(개)'] = df_of_d.loc[df_of_d['조사항목'] == '착과수', ['조사항목값']].reset_index(drop=True)
p_df_of_d['최종화방차수(차)'] = df_of_d.loc[df_of_d['조사항목'] == '최종화방차수', ['조사항목값']].reset_index(drop=True)



p_df_of_e['시설아이디'] = df_of_e['시설아이디'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_e['생육주사'] = df_of_e['생육주사'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_e['조사일자'] = df_of_e['조사일자'][::n_growthDataTypes].reset_index(drop=True)
p_df_of_e['표본번호'] = df_of_e['표본번호'][::n_growthDataTypes].reset_index(drop=True)

p_df_of_e['초장(mm)'] = df_of_e.loc[df_of_e['조사항목'] == '초장', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
p_df_of_e['엽장(mm)'] = df_of_e.loc[df_of_e['조사항목'] ==  '엽장', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
p_df_of_e['엽폭(mm)'] = df_of_e.loc[df_of_e['조사항목'] == '엽폭', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
p_df_of_e['엽병장(mm)'] = df_of_e.loc[df_of_e['조사항목'] == '엽병장', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
p_df_of_e['엽수(개)'] = df_of_e.loc[df_of_e['조사항목'] == '엽수', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
p_df_of_e['관부직경(mm)'] = df_of_e.loc[df_of_e['조사항목'] == '관부직경', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
p_df_of_e['화방꽃수(소화수)(개)'] = df_of_e.loc[df_of_e['조사항목'] == '화방 꽃수(소화수)', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
p_df_of_e['착과수(개)'] = df_of_e.loc[df_of_e['조사항목'] == '착과수', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
p_df_of_e['최종화방차수(차)'] = df_of_e.loc[df_of_e['조사항목'] == '최종화방차수', ['조사항목값']].reset_index(drop=True).apply(pd.to_numeric)
#print(p_df_of_b.head())


p_df_of_b = p_df_of_b[['생육주사','조사일자','초장(mm)','엽장(mm)','엽폭(mm)','엽병장(mm)','엽수(개)','관부직경(mm)','화방꽃수(소화수)(개)','착과수(개)','최종화방차수(차)']].groupby('조사일자').mean()
p_df_of_c = p_df_of_c[['생육주사','조사일자','초장(mm)','엽장(mm)','엽폭(mm)','엽병장(mm)','엽수(개)','관부직경(mm)','화방꽃수(소화수)(개)','착과수(개)','최종화방차수(차)']].groupby('조사일자').mean()
p_df_of_d = p_df_of_d[['생육주사','조사일자','초장(mm)','엽장(mm)','엽폭(mm)','엽병장(mm)','엽수(개)','관부직경(mm)','화방꽃수(소화수)(개)','착과수(개)','최종화방차수(차)']].groupby('조사일자').mean()
p_df_of_e = p_df_of_e[['생육주사','조사일자','초장(mm)','엽장(mm)','엽폭(mm)','엽병장(mm)','엽수(개)','관부직경(mm)','화방꽃수(소화수)(개)','착과수(개)','최종화방차수(차)']].groupby('조사일자').mean()

p_df_of_b.to_excel('p_b_growth_data.xlsx')
p_df_of_c.to_excel('p_c_growth_data.xlsx')
p_df_of_d.to_excel('p_d_growth_data.xlsx')
p_df_of_e.to_excel('p_e_growth_data.xlsx')


p_df_of_b.to_csv('p_b_growth_data.csv')
p_df_of_c.to_csv('p_c_growth_data.csv')
p_df_of_d.to_csv('p_d_growth_data.csv')
p_df_of_e.to_csv('p_e_growth_data.csv')


#농장 c는 트레이닝 데이터

