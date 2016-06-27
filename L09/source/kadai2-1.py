# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read
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

def GenFreq(Fc, Fs, dur):
    return Amp * np.sin( 2. * np.pi * Fc * t )

class ShowWav(object):
    def __init__( self, fname ):
        self.fname = fname
        y = read( fname )
        Fs = y[0]
        self.ydat = y[1]
        self.Nmax = self.ydat.shape[0]
        if( self.ydat.ndim > 1 ):
            self.channel = self.ydat.shape[1]
        else:
            self.channel = 1
            self.ydat = self.ydat.reshape( (self.Nmax, 1) )
        self.Nmax = int(pow(2, int(np.log2(self.Nmax)) )) # FFT の為，2のベキに調整
        self.delta = 1./Fs
        self.fdelta = 1./(self.Nmax*self.delta)
        self.t = np.arange( self.Nmax ) * self.delta
        self.f = np.arange(-self.Nmax/2, self.Nmax/2) * self.fdelta


    def plot( self ):
        for k in range( self.channel ):
            plt.subplot( 2, self.channel, 2*k+1 )
            plt.plot( self.t, self.ydat[:self.Nmax, k] )
            plt.xlim( 0, self.t[-1] )
            plt.title( 'Amplitude Ch.%d' % k )
            plt.grid()

            Y = spf.fft( self.ydat[:self.Nmax, k] )
            plt.subplot( 2, self.channel, 2*k+2 )
            plt.xlim( -1000, 1000 )
            plt.semilogy( self.f, np.abs(spf.fftshift(Y)) )
            plt.title( 'Power Ch.%d' % k )
            plt.grid()

        plt.show()

y1 = GenFreq(262, Fs, dur)
y2 = GenFreq(294, Fs, dur)
y3 = GenFreq(330, Fs, dur)
y4 = GenFreq(349, Fs, dur)
y5 = GenFreq(392, Fs, dur)
y6 = GenFreq(440, Fs, dur)
y7 = GenFreq(494, Fs, dur)                    
y8 = GenFreq(523, Fs, dur)

x = np.hstack((y1, y2, y3, y4, y5, y6, y7, y8))
write( fname, Fs, np.int16( x ).reshape(int(Nmax) * 8, 1) )
s = ShowWav(fname)
s.plot()






