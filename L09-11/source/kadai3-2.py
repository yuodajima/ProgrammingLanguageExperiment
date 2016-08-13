# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf

from scipy.io.wavfile import write
import matplotlib.pylab as plt
from scipy.io.wavfile import read

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

class GenFreq( object ):
    def __init__( self, Fs=44100., dur=1., Amp=4000. ):
        self.Fs = Fs
        self.dur = dur
        self.Amp = Amp
        self.delta = 1./Fs
        self.Nmax = Fs * dur  # サンプル点の数
        self.t = np.arange(self.Nmax) * self.delta
        self.sound = np.zeros(len(self.genSound(262)))
        self.codes = {'C':262,
                      'E':330,
                      'G':392}
    
        
    def getSound( self ):
        return self.sound
        

    def getLen( self ):
        return len(self.getSound())
        # データ配列長を返す

    def addTone( self, code='C' ):
        newSound = self.genSound(self.codes[code])
        self.sound +=  newSound

    def genSound(self, freq):
        return self.Amp * np.sin( 2. * np.pi * freq * self.t )
        


Fs = 44100.                  # サンプル周波数
s = GenFreq( Fs, dur=1.)
s.addTone( 'C' )
s.addTone( 'E' )
s.addTone( 'G' )
N = s.getLen()


write( 'kadai3-2.wav', Fs, s.getSound().reshape( (N, 1) ) )
s = ShowWav('kadai3-2.wav')
s.plot()





