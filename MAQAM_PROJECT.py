import random
import midiutil
import math
import numpy


# ------ PARAMETRS ------

scales = { 'hijaz': [1,3,1,2,1,3,1], # Maqam Assingment
           'major': [2,2,1,2,2,2,1],
           'minor': [2,1,2,2,1,2,2],
           'nawa': [2,1,3,1,1,3,1]}

mode = 'pi_mode'# Calculations based on chosen mode
chord_mode = 'dynamic' # 'harmonic' for harmony mode, 'dynamic' for dynamic harmonics null for no chords
harmonic_speed = 2 # How long do chords last
n = 50 # Music Sheet Size
file = 'phi.txt' # Which file to open
 
scale = [48] # Scale key - [48] for middle C
maqam = 'hijaz'# Choose scale
notes = 10 # Number of notes to map
note_length = [] # An empty vector that will hold not duration values

key = scales[maqam] 
s = 1 # scale expanding factor
running_avg = 0 #running average mode

# ------ CALCULATIONS ------

# Scale mapping
i = 0
j = 1

while len(scale) < notes:
    if i == len(key):
        i = 0

    scale.insert(j,scale[j-1] + key[i])
    j=j+1
    i=i+1


if mode == 'pi_mode':
    # Reading 100,000 digits of pi file
    x = open(file,'r')
    pi = x.read()
    pi = pi.replace(" ", "")
    pi = pi[:n]
    org = pi # Orignal number sequance

    # Scale expaning

    pi = list(map(int, pi))

    for i in range(n-1):
        pi[i] + pi[i+1]
    
    if running_avg == 1:
        # Running Average
        bi = [int(pi[0])]
        for i in range(1,len(pi)-1):
                bi.insert(i,round((int(pi[i])+int(bi[i-1]))/2))

        # Fixing a last element to avoide crashes
        bi.insert(n-1,int((int(pi[n-1])+int(pi[n-2]))/2))
        pi = bi

elif mode == 'scale_testing':
    # Scale testing
    x = open('scale_testing.md','r')
    pi = x.read()
    pi = pi[320:320+n]
    x = pi



# Base sheet generation
# base for basic music sheet in primitve letters
base = []
k = 0

for i in range(n):
    base.insert(k,pi[i])
    k = k + 1

# substitution of digits with MIDI notes
for i in range(int(n)):
    temp = int(base[i])
    base[i] = scale[temp]

for i in range(int(n)):
    base[i] = int(base[i])

if mode == 'pi_mode':
    for i in range(n-1):
        if 0 <= pi[i+1] <= 1:
            note_length.insert(i,1/2)
        elif 2 <= pi[i+1] <= 3:
            note_length.insert(i,1)
        elif 4 <= pi[i+1] <= 5:
            note_length.insert(i,1/2)
        elif 6 <= pi[i+1] <= 8:
            note_length.insert(i,1)
        elif 8 <= pi[i+1] <= 9:
            note_length.insert(i,1/4)

note_length.insert(n,1)

# Create final MUSIC SHEET

final = [base,note_length,pi]

# ------ MIDI CREATE ------

chord = []
bar = []
track    = 0
channel  = 0
time     = 0    # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = midiutil.MIDIFile(2)  # Two tracks

MyMIDI.addTempo(track, time, tempo)

# ------ MAIN NOTES ------

for i, pitch in enumerate(base):
    if mode == 'pi_mode':
        MyMIDI.addNote(0, channel, final[0][i]+12, time ,final[1][i] , 100)
        chord.insert(i,final[0][i])
        bar.insert(i,math.floor(time))
                
        time = time + final[1][i]
        
    elif mode == 'scale_testing':
        MyMIDI.addNote(0, channel, pitch, i ,1 , 100)
            

track1_time = time

# ------ CHORDS ------

time = 0

if mode == 'pi_mode':
    for i, pitch in enumerate(base):
        
        try:
            index = bar.index(time)
        except ValueError:
            
            try:
                index = bar.index(time-1)
            except ValueError:
                
                try:
                    index = bar.index(time-2)
                except ValueError:
                    index = bar.index(time-3)
                    
        if chord_mode == 'harmonics':
        
            MyMIDI.addNote(1, channel, chord[index]+24, time ,harmonic_speed , 80)
            MyMIDI.addNote(1, channel, chord[index]-12, time ,harmonic_speed , 80)
            MyMIDI.addNote(1, channel, chord[index]   , time ,harmonic_speed , 80)

        
        elif chord_mode == 'dynamic':
            
            MyMIDI.addNote(1, channel, chord[index]+24, time                     ,harmonic_speed*1/4 , 80)
            MyMIDI.addNote(1, channel, chord[index]-12, time + harmonic_speed*1/4,harmonic_speed*1/4 , 80)
            MyMIDI.addNote(1, channel, chord[index]+12, time + harmonic_speed*2/4,harmonic_speed*1/4 , 80)
            MyMIDI.addNote(1, channel, chord[index]   , time + harmonic_speed*3/4,harmonic_speed*1/4 , 80)

        time = time + harmonic_speed
        
        if time >= track1_time-1:
                break
        
    

with open("MAQAM_PORJECT["
          + file[:3] + ','
          + str(n) + ','
          + maqam + ','
          + chord_mode + ']'
          + ".mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
