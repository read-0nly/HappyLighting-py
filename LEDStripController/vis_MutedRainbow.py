import numpy as np
import ExternalAudio
import colorsys
import Utils
import dsp
rLerp =  0.8
gLerp =  0.8
bLerp =  0.8
vLerp =  0.1
rold=0;
gold=0;
bold=0;
vold=0;
Utils.MAX_FREQUENCY=16000
Utils.N_PIXELS = 512 
Utils.N_FFT_BINS = 256 
from importlib import reload

reload(ExternalAudio)
dsp.create_mel_bank()
def visualize_spectrum(y):
    """Effect that maps the Mel filterbank frequencies onto the LED strip"""
    global rold,gold,bold,vold
    y = np.copy(ExternalAudio.interpolate(y, Utils.N_PIXELS // 2))
    ExternalAudio.common_mode.update(y)
    diff = y - ExternalAudio._prev_spectrum
    maxIndex=np.argmax(y)
    maxValue = y[maxIndex]
    avg = np.average(y)
    print(str(len(y)))
    #print (str(maxIndex/len(y))+":"+str((avg/maxValue))+":"+str(maxValue))
    vnew = pow(min(1,max(0,maxValue-0.1)),0.3)
    if(vnew<vold):
        vnew=vnew*(vLerp)+(vold*(1-vLerp))
    color = colorsys.hsv_to_rgb((pow(((maxIndex/len(y)))*1.5,0.7)%1),(min(1,pow((max(0,maxIndex-int(Utils.N_FFT_BINS/128))/len(y)),0.2))),vnew)
    ExternalAudio._prev_spectrum = np.copy(y)
    # Color channel mappings
    r = np.array([color[0]])
    if(r<rold):
        r=r*(rLerp)+(rold*(1-rLerp))
    g = np.array([color[1]])
    if(g<gold):
        g=g*(gLerp)+(gold*(1-gLerp))
    b = np.array([color[2]])
    if(b<bold):
        b=b*(bLerp)+(bold*(1-bLerp))
    # Mirror the color channels for symmetric output
    #r = np.concatenate((r[::-1], r))
    #g = np.concatenate((g[::-1], g))
    #b = np.concatenate((b[::-1], b))
    rold=r
    gold=g
    bold=b
    vold=vnew
    output = np.array([r,g,b]) * 255
    return output
