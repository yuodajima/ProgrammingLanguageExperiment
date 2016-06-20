# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf

from scipy.io.wavfile import write
import matplotlib.pylab as plt

# 設定
Fs = 22050.  # サンプリング周波数 22 KHz
fname = 'kadai2-1.wav'
dur = 3.    
Amp = 4000.  # 振幅 (とりあえず)

delta = 1./Fs  # サンプリング間隔
Nmax = Fs * dur  # サンプル点の数

t = np.arange(Nmax) * delta
Fcs = [262, 294, 330, 349, 392, 440, 494, 523]

def GenFreq(Fc, Fs, dur):
    return Amp * np.sin( 2. * np.pi * Fc * t )


y1 = GenFreq(262, Fs, dur)
y2 = GenFreq(294, Fs, dur)
y3 = GenFreq(330, Fs, dur)
y4 = GenFreq(349, Fs, dur)
y5 = GenFreq(392, Fs, dur)
y6 = GenFreq(440, Fs, dur)
y7 = GenFreq(494, Fs, dur)                    
y8 = GenFreq(523, Fs, dur)

x = np.hstack((y1, y2, y3, y4, y5, y6, y7, y8))
write( fname, Fs, np.int16( x ).reshape(Nmax * 8, 1) )  
    

# 確認用

Y = spf.fft( x )                
fdelta = 1./(Nmax * 8 * delta)
f = np.arange(Nmax * 8) * fdelta
plt.figure()
plt.subplot( 2, 1, 1 )
plt.plot( t[:100], x[:100] )
plt.grid
plt.subplot( 2, 1, 2 )
plt.semilogy( f, np.abs( Y ) )
plt.grid()

plt.show()




