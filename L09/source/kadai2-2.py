# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read
import matplotlib.pyplot as plt


fname = 'KyokoSampling.wav'

y = read( fname )
Fs = y[0]


#
# y のデータ形式は以下のようなタプル
# ( サンプリング周波数, データ部 )
# データ部の形式は，
# N x 2 の行列データ(2の部分は左音声と右音声)
# N はサンプル数
#

delta = 1./Fs # サンプル間隔([sec])
Nmax = 65536 # FFT のため 2 のベキでサンプルをとる
fdelta = 1./(Nmax*delta) # 周波数刻み
N = 256

t = np.arange(Nmax) * delta
f = np.arange(-Nmax/2, Nmax/2) * fdelta

def SpecGram(x):
    x0 = x[1][0:256]
    x1 = x[1][256:512]
    x2 = x[1][512:768]
    x3 = x[1][768:1024]
    print x3.shape

    yl0 = x0[:Nmax,0].reshape(N,1)
    yl1 = x1[:Nmax,0].reshape(N,1)
    yl2 = x2[:Nmax,0].reshape(N,1)
    yl3 = x3[:Nmax,0].reshape(N,1)
    print yl3.shape
    
    Yl0 = spf.fft( yl0 )
    Yl1 = spf.fft( yl1 )
    Yl2 = spf.fft( yl2 )
    Yl3 = spf.fft( yl3 )
    print Yl3.shape

    img = np.hstack((Yl0, Yl1, Yl2, Yl3))

    z = x[1][:256*1000]
    zl = z[:Nmax, 0]
    Z = spf.fft(zl)
    
    return Z

img = SpecGram(y);
print img.shape



plt.figure()

plt.subplot( 2, 1, 1 )
plt.plot( t, img )
plt.xlim( 0, t[-1] )
plt.title( 'Amplitude' )
plt.grid()

plt.subplot( 2, 1, 2 )
plt.semilogy( f, np.abs(spf.fftshift(img)) )
plt.xlim( f[0], f[-1] )
plt.title( 'Power(Semi log)' )
plt.grid()

plt.show()
