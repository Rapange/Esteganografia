import audioconverter
import audioreader
import audiowriter
import ImagenAImagen as png2png
from textoenaudio import lsb as txt2wav

#Ejemplo de como utilizar

#audioconverter.mp3towav('EncodeAudio/pk3.mp3','EncodeAudio/Cpk3.wav')

#txt2wav.hide('EncodeAudio/Cpk3.wav','textoenaudio/resumencap20.txt','EncodeAudio/txtpk3.wav',2)

#audioreader.audiotoimage('EncodeAudio/txtpk3.wav')

#png2png.cifrarImagen("image.png", "suspicious2.png", "stegoimagebattle.png", 8)

png2png.descifrarImagen(252,252, "stegoimagebattle.png", "newimagebattle.png",8)

audiowriter.imagetoaudio('newimagebattle.png','DecodeAudio/newbattle.wav')

txt2wav.recover('DecodeAudio/newbattle.wav','resumencap20.txt',2,1.03)

audioconverter.wavtomp3('DecodeAudio/newbattle.wav','DecodeAudio/newbattle.mp3')


