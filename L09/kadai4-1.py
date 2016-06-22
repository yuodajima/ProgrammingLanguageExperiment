# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

ifname  = 'KyokoSampling.wav'
ifname0 = 'KnoiseColored.wav'       # 入力ファイル名
ifname1 = 'HAL0001noiseColored.wav' # 入力ファイル名
ifname2 = 'HAL0002noiseColored.wav' # 入力ファイル名
ofname0 = 'kadai4-1-0.wav'          # 出力ファイル名
ofname1 = 'kadai4-1-1.wav'          # 出力ファイル名
ofname2 = 'kadai4-1-2.wav'          # 出力ファイル名

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

# y0 = read( ifname0 )
# Fs0 = y0[0]          # サンプリングレート
# Nmax0 = 65536*2     # FFT のため 2 のベキにしておく
# yl0 = y0[1][:Nmax]   # 左音声の 0〜Nmax-1 までを信号とする
# fc0 = 6000          # 500Hz で遮断してみる
# yflt0 = LowPass( yl0, fc0, Fs0 )
# write(ofname0, Fs0, np.int16( np.real(yflt0) ).reshape(Nmax0,1) ) 

def cutOff(filename, Nmax, fc, ofname):
    y = read( filename )
    Fs = y[0]           # サンプリングレート
    yl = y[1][:Nmax]    #0〜Nmax-1 までを信号とする
    yflt = LowPass( yl, fc, Fs )
    write(ofname, Fs, np.int16( np.real(yflt) ).reshape(Nmax,1) )
    s = ShowWav(ofname)
    s.plot()
    

cutOff(ifname0, 65536*2, 6000, ofname0)
cutOff(ifname1, 65536*8, 6000, ofname1)
cutOff(ifname2, 65536*4, 6000, ofname2)

#実行結果
#以下のように変換し，結果をファイルに出力した．
#KnoiseColored.wav->kadai4-1-0.wav
#HAL0001noiseColored.wav->kadai4-1-1.wav
#HAL0002noiseColored.wav->kadai4-1-2.wav
#以下，順に聴きとった音声
#こんにちは，私はKyokoです．
#茶色い狐が私のろまな犬を飛び越えた．
#おはようチャンドラ博士．私はHALです．今日の最初の授業をはじめてください．
#いずれの音声ファイルも6000Hzを基準にカットした．
