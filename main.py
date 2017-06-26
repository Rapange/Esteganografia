import audioconverter
import audioreader
import audiowriter

#Ejemplo de como utilizar
audioconverter.mp3towav('EncodeAudio/Pk3.mp3','EncodeAudio/output2.wav')

audioreader.audiotoimage('EncodeAudio/output2.wav')

audiowriter.imagetoaudio('image.png','DecodeAudio/final.wav')

audioconverter.wavtomp3('DecodeAudio/final.wav','DecodeAudio/final.mp3')


