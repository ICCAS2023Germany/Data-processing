import os
import pandas as pd

csv_directory = 'your path'

#모든 파일을 읽어 오면서 수행
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

for csv_file in csv_files:
    csv_file_path = os.path.join(csv_directory, csv_file)
    data = pd.read_csv(csv_file_path, encoding='utf-8')

    data['글자 수'] = data.iloc[:, 0].str.len()

    data.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
    print(f"파일 '{csv_file_path}'이(가) 성공적으로 처리되었습니다.")
