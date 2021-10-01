import pandas as pd

samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')

# 코드를 작성하세요

day = samsong_df['요일']
samsong = samsong_df['문화생활비']
hyundee = hyundee_df['문화생활비']

df = {
    'day': day,
    'samsong': samsong,
    'hyundee': hyundee
}

pd.DataFrame(df)
