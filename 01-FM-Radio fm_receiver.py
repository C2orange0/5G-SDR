import numpy as np
import sounddevice as sd

# 生成 1 kHz 正弦波，模拟 FM 音频
fs = 48000
t = np.linspace(0, 2, 2 * fs, endpoint=False)
audio = 0.5 * np.sin(2 * np.pi * 1000 * t)
sd.play(audio, fs)
sd.wait()
print("FM 收音机示例运行完成！")  