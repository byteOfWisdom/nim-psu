Nutzung:

upload des arduino sketches via seriellem port:
wenn D2 D3 genutzt werden sollen muss #define LEGACY entweder in einer source datei oder als compiler option existieren.
ansonsten muessen die jumper auf RX/TX gesetzt werden, dieses wird sowohl fuer programmierung als auch fuer
die spaetere kommunikation mit dem arduino genutzt.

hochladen des sketches mit "make upload". nachdem das compilieren abgeschlossen ist, muss der reset button des
arduinos gedrueckt werden. (ein workaround dafuer ohne hardware revision scheint mir nicht moeglich.)


in state.h ist der default state und andere konstanten definiert
upload via arduino ide (oder arduino-cli)

steuerung ueber serial_comm.py:
"alte" art funktioniert immer noch (tuple aus [channel, zustand])
alternativ: 
    enable [channel oder mehrere channel (space sepereated)]
    disable [channel oder mehrere channel (space sepereated)]

auslesen des aktuellen zustands:
    read