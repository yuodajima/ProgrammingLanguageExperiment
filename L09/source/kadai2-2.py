# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read
import matplotlib.pyplot as plt


fname = 'KyokoSampling.wav'
y = read( fname )
N = 256

#
# y のデータ形式は以下のようなタプル
# ( サンプリング周波数, データ部 )
# データ部の形式は，
# N x 2 の行列データ(2の部分は左音声と右音声)
# N はサンプル数
#

# delta = 1./Fs # サンプル間隔([sec])
# Nmax = 65536 # FFT のため 2 のベキでサンプルをとる
# fdelta = 1./(Nmax*delta) # 周波数刻み

# t = np.arange(Nmax) * delta
# f = np.arange(-Nmax/2, Nmax/2) * fdelta

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
    
    
    # x0 = x[1][0:256]
    # x1 = x[1][256:512]
    # x2 = x[1][512:768]
    # x3 = x[1][768:1024]
    # print x3.shape

    # yl0 = x0[:Nmax,0].reshape(N,1)
    # yl1 = x1[:Nmax,0].reshape(N,1)
    # yl2 = x2[:Nmax,0].reshape(N,1)
    # yl3 = x3[:Nmax,0].reshape(N,1)
    # print yl3.shape
    
    # Yl0 = spf.fft( yl0 )
    # Yl1 = spf.fft( yl1 )
    # Yl2 = spf.fft( yl2 )
    # Yl3 = spf.fft( yl3 )
    # print Yl3.shape

   #  img = np.hstack((Yl0, Yl1, Yl2, Yl3))

#     z = x[1][:256*1000]
#     zl = z[:Nmax, 0]
#     Z = spf.fft(zl)
    
#     return Z

# img = SpecGram(y);
# print img.shape



# plt.figure()

# plt.subplot( 2, 1, 1 )
# plt.plot( t, img )
# plt.imshow()
# plt.xlim( 0, t[-1] )
# plt.title( 'Amplitude' )
# plt.grid()

# plt.subplot( 2, 1, 2 )
# plt.semilogy( f, np.abs(spf.fftshift(img)) )
# plt.xlim( f[0], f[-1] )
# plt.title( 'Power(Semi log)' )
# plt.grid()

# plt.show()
