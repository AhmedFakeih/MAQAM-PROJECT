# MAQAM PROJECT

MAQAM PROJECT is a an algorithm that takes in any number sequence in .txt form and outputs a musical sheet based on the sequence in .MIDI form. This project was initially meant for the algorithm to include Arabic music mode, also known as MAQAM, thus the name. I, still, have not managed to include those since Arabic mode or scales require microtonal notes. 

Program Configuration:
Up until now, music is produced by tweaking the different setting and changing the number sequences. Please check the following for an in-depth comment on the how the program works.

Parameters:

# ------ PARAMETRS ------

scales: A way of inputting different music scales using the difference between notes in an octave. For example, [2,2,1,2,2,2,1] for Major and [2,1,2,2,1,1,2] for Minor etc.

chord_mode: 'none' for no accompanying chords at all, 'harmonic' for harmonic chords, 'dynamic' for dynamic harmonics chords.

chord_length: How long do chords last, enter many (as in [1,2,3]) if you wish varied chord lengths.

chord_vel: chords velocity/strength range 

file: Which file to open, that is the file the contains the number sequence you wish to use.

ran: is a Boolean variable. Used random numbers an input instead of the number file, it overrides any giving files. Thus, keep false instead you wish to use random numbers as input.
 
Scale: Based on Midi notation, the note where your scale starts - [48] for middle C
maqam: Choose a scale from the scales dictionary. 

s: All notes are assigned digits depending on the variable the expansion factor s, where s=1 meaning digits are mapped to a range of [0-9], where s=5 meaning the range is [0-45], and so on.

n = s*(x): number notes in final Midi file, where x is the number of notes

note_length_value: How long do note last depending on their mapped value. Changing values in the list will make note changing in length accordingly, which usually results in interesting results. 

tempo: tempo In BPM

running_avg: Boolean. True, activates running average function, which flattens out the transitions between note and makes them smoother.

running_i: the number of times the to execute the running average function. 
