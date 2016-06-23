# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

ifname1 = 'KnoiseColored.wav'   # 入力ファイル名
ifname2 = 'HAL0001noiseColored.wav'   # 入力ファイル名
ifname3 = 'HAL0002noiseColored.wav'   # 入力ファイル名
o1fname1 = 'voice1.wav'
o1fname2 = 'voice2.wav'
o1fname3 = 'voice3.wav'

def LowPass( x, f, Fs=44100. ):
    N = len(x)
    fdelta = float(Fs)/N
    X = spf.fft( x )
    Ncut = int(f/fdelta)  # カットオフ周波数対応添字
    flt = np.zeros(N)
    flt[0:Ncut] = 1
    flt[-Ncut+1:] = 1

    xflt = spf.ifft( X * flt ) # フィルタ処理
    return xflt.real # 実部だけを返す

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
        self.Nmax = int(pow(2, int(np.log2(self.Nmax)) ))
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
            plt.xlim( self.f[0], self.f[-1] )
            plt.semilogy( self.f, np.abs(spf.fftshift(Y)) )
            plt.title( 'Power Ch.%d' % k )
            plt.grid()

        plt.show()


y1 = read( ifname1 )
Fs1 = y1[0]          # サンプリングレート
Nmax = 65536*2       # FFT のため 2 のベキにしておく
yl1 = y1[1][:Nmax] # 左音声の 0〜Nmax-1 までを信号とする
fc1 = 4000           # 500Hz で遮断してみる
yflt1 = LowPass( yl1, fc1, Fs1 )
write(o1fname1, Fs1, 10 * np.int16( np.real(yflt1) ).reshape(Nmax,1) )
s1 = ShowWav( o1fname1 )
s1.plot()

y2 = read( ifname2 )
Fs2 = y2[0]          # サンプリングレート
Nmax = 65536*5       # FFT のため 2 のベキにしておく
yl2 = y2[1][:Nmax] # 左音声の 0〜Nmax-1 までを信号とする
fc2 = 4600           # 500Hz で遮断してみる
yflt2 = LowPass( yl2, fc2, Fs2 )
write(o1fname2, Fs2, 10 * np.int16( np.real(yflt2) ).reshape(Nmax,1) )
s2 = ShowWav( o1fname2 )
s2.plot()

y3 = read( ifname3 )
Fs3 = y3[0]          # サンプリングレート
Nmax = 65536*4       # FFT のため 2 のベキにしておく
yl3 = y3[1][:Nmax] # 左音声の 0〜Nmax-1 までを信号とする
fc3 = 5000           # 500Hz で遮断してみる
yflt3 = LowPass( yl3, fc3, Fs3 )
write(o1fname3, Fs3, 10 * np.int16( np.real(yflt3) ).reshape(Nmax,1) )
s3 = ShowWav( o1fname3 )
s3.plot()

"""実行例
実行結果のグラフをshowwav1.png、showwav2.png、showwav3.pngとして保存し、
実行結果の音をvoice1.wav、voice2.wav、voice3.wavとして保存しました"""
