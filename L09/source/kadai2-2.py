# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

fname = 'KyokoSampling.wav'
y = read( fname )
N = 256

def SpecGram(x):

    Fs = x[0]
    x_left = x[1][0:, 0]
    x_left_length = len(x_left)
    x_quotient = x_left_length / N
    x_surplus =  x_left_length % N
    x_final = x_left[:(x_left_length) - x_surplus]
    x_final_length = len(x_final)

    x_ = np.transpose(x_final.reshape(x_quotient, N))
    X_ = np.zeros((N, x_quotient), dtype = np.complex)

    for i in range(x_quotient):
        X_[:, i] = spf.fft(x_[:, i])

    X_log10 = np.log10(abs(X_))
    time = np.arange(x_final_length)
    x_axis = (np.arange(5) + 1) * 1. * Fs / N
    y_axis = np.arange(5) * N * 1. / Fs * 5000    

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.imshow(X_log10, aspect = 'auto')
    plt.xticks([x_axis[0], x_axis[1], x_axis[2], x_axis[3], x_axis[4]],
                ['1', '2', '3', '4', '5'])
    plt.yticks([y_axis[0], y_axis[1], y_axis[2], y_axis[3], y_axis[4],],
               ['0', '5000', '10000', '15000', '20000'])
    plt.xlim(0, x_quotient)
    plt.ylim(N / 2, 0 )
    plt.grid

    plt.subplot(2, 1, 2)
    plt.plot(time * 1. / Fs, x_final)
    plt.xlim(0, 1. * x_final_length / Fs)
    plt.ylim(-5000, 5000)
    plt.grid()

    plt.show()

SpecGram(y)    
    
    
 
