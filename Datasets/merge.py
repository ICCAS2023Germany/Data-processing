import os
import pandas as pd

# 디렉토리 경로 설정
directory_path = 'your path'

# 빈 DataFrame 생성
merged_df = pd.DataFrame()

# 디렉토리 내의 모든 .csv 파일을 순회하면서 DataFrame에 추가
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory_path, filename)
        df = pd.read_csv(filepath)
        merged_df = pd.concat([merged_df, df])

# 중복된 행 제거
merged_df.drop_duplicates(inplace=True)

# 합쳐진 DataFrame을 하나의 .csv 파일로 저장
output_filepath = 'your path'
merged_df.to_csv(output_filepath, index=False)

print("모든 .csv 파일이 성공적으로 합쳐지고 중복된 행이 제거되었습니다.")
