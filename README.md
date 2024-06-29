# I.F Rocket Project Code Repository

광주과학고등학교 로켓 동아리 I.F의 프로젝트 진행에 사용되는 코드들을 모아두는 레포입니다.

## 추력 테스트 장치

* [아두이도 업로드 코드](Load%20cell%20upload%20code/collectData.ino)

collectData.ino는 추력 테스트 장치의 아두이노에 업로드하는 코드입니다. 사용하는 추력 테스트 장치는 로드셀과 아두이노를 연결하여 사용하는 중입니다. 

* [데이터 수집 코드](data.py)

data.py는 아두이노가 Serial 통신을 통해 보내주는 값을 저장하는 코드입니다. **아두이노 ide 시리얼 모니터가 켜져있으면 에러가 발생합니다** 코드가 작성중일 때 Ctrl+C를 눌러 정지시키면 값을 자동으로 data.csv에 저장합니다.

* [데이터 시각화 코드](visualize.py)

visualize.py는 저장된 값을 해석하는 코드입니다. 
Edit the following constants 라고 주석이 되어 있는 부분의 값을 수정하면 됩니다.
코드를 실행하면 output 폴더에 설정한 이름의 폴더가 생성됩니다. 그 폴더 안에 그래프가 저장됩니다. 

| 변수명 | 설명                                  |
| --- |-------------------------------------|
| ```ZERO_DATA``` | 로드셀 위에 아무것도 올려두지 않았을 때의 센서값         |
| ```ROCKET_MASS``` | 로켓의 발사 전 연료를 포함한 질량(Kg)             |
| ```ROCKET_DATA``` | 로드셀 위에 로켓만 올렸을 때 센서값                |
| ```ROCKET_END_DATA``` | 로켓이 완전 연소가 끝난 뒤, 로드셀 위에 올려진 상태의 센서값 |
| ```LOOK_START``` | 로켓이 발사되기 시작하는 지점의 데이터 인덱스           |
| ```LOOK_END``` | 로켓 연소가 끝나는 지점의 데이터 인덱스            |
| ```DATA_TITLE``` | 데이터의 제목(그래프의 제목)                  |
| ```FILE_PATH``` | 데이터가 저장된 파일의 경로                   |