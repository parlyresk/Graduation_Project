# 2023-1 Graduation_Project
# TinyML을 통한 소리 인식 및 위치 탐지

## 개요

지진 등의 사고 현장 같은 불안정한 장소에서 사고 피해자들을 찾기 위한 AI 모델링을 구현한다. 드론에 장착하기 위해 가볍고 저전력으로 사용가능한 TinyML 모델을 학습시켜 드론에 장착하여 사고 피해자들의 소리를 감지하고 위치를 탐지하는 시스템을 구현한다. Sound Classification과 Sound Localization을 혼합하여 Edge Impulse 플랫폼을 사용하여 모델을 학습을 시도한다. 사용할 데이터는 기존에 존재하는 데이터셋 및 직접 녹음한 데이터를 통해 학습을 진행한다. 학습한 모델을 nano 33 ble에 배포하고 드론에 장착시켜 소리를 인식하고 위치를 탐지시킨다.



</br>

## 결과

![화면 캡처 2023-05-24 224700](https://github.com/parlyresk/Graduation_Project/assets/72953981/63287e19-c790-4200-9b1f-597aaeb82dc2)
![KakaoTalk_20230524_224743876](https://github.com/parlyresk/Graduation_Project/assets/72953981/c49aabd0-de03-4283-bc34-098b5c1ceb18)

Classification한 소리 중 0.8 이상이 되면 붉은 색 led가 점등한다

</br>

</br>
## 결론

필요한 음성 정보를 외부 프로젝트 및 직접 녹음을 통해 얻은 뒤

데이터 전처리를 통해 Sound Classifiaction을 구현했다

multi channl을 통한 음성 정보를 넣어 Sound Localization을 학습하여

두 개의 모델을 동시에 적용시키는 것이 추후 과제가 될 것이다

## 참조
https://studio.edgeimpulse.com/public/111611/latest


[https://studio.edgeimpulse.com/studio/200131](https://studio.edgeimpulse.com/public/224653/latest)
