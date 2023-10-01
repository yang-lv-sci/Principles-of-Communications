# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:13:32 2023

@author: lvyan
"""

import numpy as np
import matplotlib.pyplot as plt

# 设置参数
fs = 1000000  # 采样率，单位：Hz
t = 10  # 时长，单位：秒
n_0 = 5  # 功率谱密度的两倍，用户可以根据需要设置

# 生成高斯白噪声
num_samples = fs * t
noise = np.random.normal(0, np.sqrt(n_0 / 2), num_samples)

# 创建1x2的子图网格
plt.figure(figsize=(14, 6))

# 绘制时间图像
plt.subplot(1, 2, 1)  # 1x2的子图网格中的第一个
plt.plot(np.arange(num_samples) / fs, noise)
plt.title('Gaussian White Noise - Time Domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# 计算并绘制功率谱密度
plt.subplot(1, 2, 2)  # 1x2的子图网格中的第二个
f, Pxx = plt.psd(noise, NFFT=2048, Fs=fs, scale_by_freq=True, color='r')
plt.title('Power Spectral Density - Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power/Frequency (dB/Hz)')

# 显示图像
plt.tight_layout()
plt.show()

