#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#


# Va trebui sa modifici cateva elemente simple din script ;)

# folosim un modul pentru manipularea fisierelor audio 
import wave

# deschidem fisierul -> r=read, b=bytes
song = wave.open("4you-embeded.wav", mode='rb')

# Transform fisierul (`song.readframes(song.getframes)`) 
# in lista (`list()`) de bytes (`bytearray()`)
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extragem ultimul bit din fiecare byte (LSB = least significant bit)
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

# Transformam sirul de bytes in string
# stii cum legi un `sir` de caractere intr-un singur string, nu?
string = "hahahainplus".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

# Extragem caracterele in plus (de padding)
decoded = string.split("###")[0]

# Afiseaza rezultatul
print("Sucessfully decoded: ")#+ decoded)

# nu uita sa inchizi fisierul
#song.close()
