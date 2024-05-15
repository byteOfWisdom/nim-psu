Nutzung:

in state.h ist der default state und andere konstanten definiert
upload via arduino ide (oder arduino-cli)

steuerung ueber serial_comm.py:
"alte" art funktioniert immer noch (tuple aus [channel, zustand])
alternativ: 
    enable [channel oder mehrere channel (space sepereated)]
    disable [channel oder mehrere channel (space sepereated)]

auslesen des aktuellen zustands:
    read