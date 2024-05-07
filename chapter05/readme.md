< 정리 >

- RNN은 순환하는 경로가 있고, 이를 통해 내부에 '은닉 상태'를 기억할 수 있다. 

- RNN의 순한 경로를 펼침으로써 다수의 RNN 계층이 연결된 신경망으로 해석할 수 있으며, 보통의 오차역전파법으로 학습할 수 있다 (=BPTT)

- 긴 시계열 데이터를 학습할 때는 데이터를 적당한 길이씩 모으고(이를 '블록'이라고 한다), 블록 단위로 BPTT 에 의한 학습을 수행한다. (=Truncated BPTT)

- Truncated BPTT에서는 역전파의 연결만 끊는다. 

- Truncated BPTT 에서는 순전파의 연결을 유지하기 위해 데이터를 '순차적'으로 입력해야한다.

- 언어 모델은 단어 시퀀스를 확률로 해석한다. 

- RNN 계층을 이용한 조건부 언어 모델은 (이론적으로는) 그때까지 등장한 모든 단어의 정보를 기억할 수 있다. 