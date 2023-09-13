
# 임베디드 프로젝트 관련 내용


## 1.온도 센서의 종류
비접촉 온도센서 -  적외선 온도계
접촉 온도센서 - 써모커플 (열전대 | Thermocouples), 저항을 감지하는 RTD와 써미스터, 온도에 따라 상태가 변하는 온도라벨, 액체 온도계, 바이메탈 온도센서


비접촉 온도센서는 흔히 생각할 수 있는 적외선 카메라의 느낌.
그렇기 때문에 비닐하우스에 사용하는 센서는 모두 접촉 온도 센서이다.
접촉 온도 센서는 측정 센서의 끝부분에 온도만 알 수 있다.

<span style="color:blue">결과 -> 비닐하우스의 온도 센서는 접촉 온도 센서이며, 온도 측정범위는 매우 좁다.</span>


## 2.구성 방안(2차원)
가정 1 : 가로 N(m) X 세로 M(m)인 구조(각 격자는 1cm마다 있으며 총 NM개)

가정 2 : 측정 센서는 S개 (1 <= S <= NM)

![image](https://github.com/HanbatEmbeddedProject/Backend/assets/45327794/f92c1239-19b5-419a-9404-b0bfc5c88a96)

온도 측정 방안 : 평균값으로 측정

접근 방법
| S=1 | 2<=S<NM | S=NM |
|---|---------|----|
|모든 공간은 S의 온도|S개의 가중평균으로 측정|계산 없음|

## 3.예제 결과

    N, M = 5, 5 
    sensors = [(1, 1, 25), (3, 4, 30)]
![Figure_1](https://github.com/HanbatEmbeddedProject/Backend/assets/45327794/3f808ccf-e8c2-4a89-8953-545af08adcc5)


    N, M = 15, 15
    sensors = [(3, 2, 30), (5, 14, 22), (5, 2, 20), (14, 13, 20), (14, 2, 25)]
![Figure_2](https://github.com/HanbatEmbeddedProject/Backend/assets/45327794/51031da2-19c1-4697-9cb5-21c664f826e7)
