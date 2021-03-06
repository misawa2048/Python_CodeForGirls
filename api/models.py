from django.conf import settings
from django.db import models

class Rand_int(models.Model):
    value = models.IntegerField(default=12)

    def __str__(self):
        return self.value

    def rand(self,seed=0):
      self.value = seed
      return self.value


#import librosa
#import librosa.display
#!/usr/bin/python 
# based on : www.daniweb.com/code/snippet263775.html
import math
import wave
import struct
#from pydub import AudioSegment
#import numpy as np

class TextToWav(models.Model):
    sample_rate:float = 16000.0 #models.FloatField(default=16000.0)
    pulse_hz:float = 1200.0 #models.FloatField(default=1200.0)
    volume:float = 0.5 #models.FloatField(default=0.5)
    audio:float = []

    '''
    sample_rate = 16000
    pulse_hz = 1200
    volume = 0.5
    '''

    def __str__(self):
        return self.sample_rate

    def __init__(self,samplerate,volume):
        self.sample_rate = 16000
        self.volume = 0.5
        self.pulse_hz = 1200
        self.audio=[]

    def clear(self):
        self.audio=[]

    def append_silence(self, _audio, duration_milliseconds=1000):
        num_samples = duration_milliseconds * (self.sample_rate / 1000.0)
        for x in range(int(num_samples)): 
            _audio.append(0.0)

        return _audio

    def append_sinPulse(self, _audio, _pulse_bit=0, _pulseNum=1):
        base_hz = (self.pulse_hz*(_pulse_bit+1))
        per_samples = self.sample_rate / base_hz
        for x in range(int(_pulseNum * per_samples)):
            val =  self.volume * math.sin(2 * math.pi * ( x / per_samples ));
            _audio.append(val)
        return _audio

    def append_bytes_to_tone(self, _audio, _data:bytes, _max_bytes=100000):
        if(_max_bytes<=0):
            _max_bytes = len(_data)
        else:
            _max_bytes = min(_max_bytes,len(_data))
            
        for idx in range(_max_bytes):
            _audio = self.append_sinPulse(self,_audio, 0, 1) # start bit 
            for b in range(8):
                onbit = ((_data[idx]>>b)&1) # off=0,on=1
                _audio = self.append_sinPulse(self,_audio, onbit, 1) # data bit 

            _audio = self.append_sinPulse(self,_audio, 1, 2) # stop bit 

        return _audio

    def get_full_path(self):
        return settings.MEDIA_ROOT+'/'

    def save_wav(self, _audio, _filename, _callback=None):
        # Open up a wav file
        wav_file=wave.open(self.get_full_path(self)+_filename+".wav","w")

        # wav params
        nchannels = 1
        sampwidth = 2

        # 44100 is the industry standard sample rate - CD quality.  If you need to
        # save on file size you can adjust it downwards. The stanard for low quality
        # is 8000 or 8kHz.
        nframes = len(_audio)
        comptype = "NONE"
        compname = "not compressed"
        wav_file.setparams((nchannels, sampwidth, self.sample_rate, nframes, comptype, compname))

        # WAV files here are using short, 16 bit, signed integers for the 
        # sample size.  So we multiply the floating point data we have by 32767, the
        # maximum value for a short integer.  NOTE: It is theortically possible to
        # use the floating point -1.0 to 1.0 data directly in a WAV file but not
        # obvious how to do that using the wave module in python.
        for sample in _audio:
            wav_file.writeframesraw(struct.pack('h', int( sample * 32767.0 )))

        wav_file.close()

        return None if _callback==None else _callback()


    '''
    def save_mp3(self, _audio, _filename, _callback=None):
        a = np.array(_audio)
        a.tobytes()
        sound = AudioSegment(
            data=a,
            sample_width = 2, # 2 byte (16 bit) samples
            frame_rate=16000, # 44.1 kHz frame rate
            channels=1 # monoral
        )
        sound.export(self.get_full_path(self)+_filename+".mp3", format="mp3")
        return None if _callback==None else _callback()

    def bin_to_mp3(self, _bindata:bytes,_filename,_callback=None):
        self.audio = self.bin_to_audio(self,_bindata,_filename)
        return self.save_mp3(self,self.audio,_filename,_callback)

    def text_to_mp3(self, _text:str="hello", _filename="outputwav", _callback=None):
        bindata = _text.encode()
        return self.bin_to_mp3(self,bindata, _filename,_callback)
    '''



    def bin_to_audio(self, _bindata:bytes,_filename):
        #http://ngs.no.coocan.jp/doc/wiki.cgi/TechHan?page=2%BE%CF+%A5%AB%A5%BB%A5%C3%A5%C8%8E%A5%A5%A4%A5%F3%A5%BF%A1%BC%A5%D5%A5%A7%A5%A4%A5%B9
        self.audio = []
        self.audio = self.append_sinPulse(self,self.audio,1,12000) #16000
        self.audio = self.append_bytes_to_tone(self,self.audio,b'\xd3\xd3\xd3\xd3\xd3\xd3\xd3\xd3\xd3\xd3') #0xD3 x 10
        self.audio = self.append_bytes_to_tone(self,self.audio, (_filename+".cas").encode('utf-8')) # filename
        self.audio = self.append_silence(self,self.audio,1700) # space
        self.audio = self.append_sinPulse(self,self.audio,1,4000) # short header
        self.audio = self.append_bytes_to_tone(self,self.audio, _bindata,10000) # data body
        self.audio = self.append_sinPulse(self,self.audio, 0, 7) # end of data
        return self.audio

    def bin_to_wav(self, _bindata:bytes,_filename,_callback=None):
        self.audio = self.bin_to_audio(self,_bindata,_filename)
        return self.save_wav(self,self.audio,_filename,_callback)

    def text_to_wav(self, _text:str="hello", _filename="outputwav", _callback=None):
        bindata = _text.encode()
        return self.bin_to_wav(self,bindata, _filename,_callback)

    def debug_disp_bindata(self,_bindata):
        print("--------------------------------------------------------------------")
        print (_bindata)
        print("--------------------------------------------------------------------")

        datCnt=0
        for data in _bindata:
            print(data,)
            datCnt+=1
            if(datCnt>20):
                break

    def debug_disp_bytes(self,_data:bytes, _max_bytes=100000):
        if(_max_bytes<=0):
            _max_bytes = len(_data)
        else:
            _max_bytes = min(_max_bytes,len(_data))
            
        for idx in range(_max_bytes):
            bstr="0"
            for b in range(8):
                onbit = ((_data[idx]>>b)&1)+1 # off=1,on=2
                bstr += str(onbit-1)

            bstr += "11"
            print(bstr)

    def cat_text(self,_text:str):
        return _text+"?"+str(self.volume*10)

    def cat_text2(self,_text:str):
        return self.cat_text(self,_text=_text)
