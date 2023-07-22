import pandas as pd

# 변환할 자음과 해당하는 분류를 딕셔너리로 정의합니다.
consonant_dict = {
    'ㅣ': '고모음',
    'ㅟ': '고모음,',
    'ㅡ': '고모음,',
    'ㅜ': '고모음,',
    'ㅔ': '중모음,',
    'ㅚ': '중모음,',
    'ㅓ': '중모음,',
    'ㅗ': '중모음,',
    'ㅐ': '저모음,',
    'ㅏ': '저모음,',
}

# 없는 값 처리를 위한 기본 분류
default_consonant = 'NULL'

csv_file_path = 'your path'

# 데이터 불러오기
data = pd.read_csv(csv_file_path, encoding='utf-8')

# 변환된 값을 혀의 높이 열에 저장하는 작업 수행
data['혀의 높이'] = data.iloc[:, 0].apply(lambda x: ''.join([consonant_dict.get(jamo, default_consonant) for jamo in str(x)]))

# 수정된 데이터 저장
data.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
print(f"파일 '{csv_file_path}'이(가) 성공적으로 처리되었습니다."
