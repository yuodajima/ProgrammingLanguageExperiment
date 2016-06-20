# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import scipy.fftpack as spf

from scipy.io.wavfile import write
import matplotlib.pylab as plt

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
        

# ド・ミ・ソの和音(CEG) を作ってみる

Fs = 44100.                  # サンプル周波数
s = GenFreq( Fs, dur=1.)
s.addTone( 'C' )
s.addTone( 'E' )
s.addTone( 'G' )
N = s.getLen()

# scipy.wav.iofile の write をインポートしておくこと
write( 'kadai3-2.wav', Fs, s.getSound().reshape( (N, 1) ) )




