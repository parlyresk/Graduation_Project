import serial
import wave
import struct
import datetime

# 시리얼 포트 설정
port = 'COM6'  # 아두이노와 연결된 시리얼 포트
baudrate = 115200  # 통신 속도
timeout = 10  # 읽기 타임아웃 설정 (초)

# 시리얼 포트 열기
ser = serial.Serial(port, baudrate, timeout=timeout)

# .wav 파일 정보 설정

sample_width = 2  # 샘플의 바이트 수
sample_rate = 16000  # 샘플링 속도 (Hz)
channels = 2  # 채널 수
duration = 10 # 파일 녹음 시간(초)

file_count=1

try:
    while True:
        output_file = '파일 저장 경로 {}.wav'.format(file_count)  # 저장할 .wav 파일 경로

# wave 모듈을 사용하여 .wav 파일 생성
        with wave.open(output_file, 'wb') as wav_file:
            wav_file.setnchannels(channels)
            wav_file.setsampwidth(sample_width)
            wav_file.setframerate(sample_rate)

            start_time= datetime.datetime.now()
            end_time=start_time + datetime.timedelta(seconds=duration)

            while datetime.datetime.now() < end_time:
                data = ser.read()

                if data:
                    wav_file.writeframesraw(data)

        file_count += 1

except KeyboardInterrupt:
    print('end')

finally:
    ser.close()
                
   
