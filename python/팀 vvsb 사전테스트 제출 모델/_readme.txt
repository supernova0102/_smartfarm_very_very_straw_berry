keras 기반 모델을 inference.py와 함께 제출 합니다.
인풋 데이터는 n, 1, 6 차원의 numpy로 들어갑니다.
환경 데이터 종류가 전처리를 거치고도 6개를 초과하면 작동하지 않을수 있습니다
이 경우 인덱싱 코드 부분을 수정하여야 합니다

아웃풋 데이터는 n, 9 차원의 데이터 프레임 기반 csv파일 입니다
datetime과 레이블을 제외한 생육정보만 출력됩니다
첫 열 부터 초장, 엽장, 엽폭, 엽병장, 엽수, 관부직경, 화방꽃수, 착화수에 해당되는 수치만을 출력합니다.

아웃풋의 각 행은 7일간격의 생육정보 측정을 가정하고 출력됩니다.
