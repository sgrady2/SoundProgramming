import beatloop

loop = beatloop.Loop(300, 4, 4, 3)
#300 BPM, 4 beats with 4 steps each, 3 audio channels

loop.load_sound("kick.ogg", 0) #load kick sound into channel #0
loop.load_sound("hat.ogg", 1) #hat into ch. #1
loop.load_sound("snare.ogg", 2)#snare into ch. #2

loop.set_sound(0, 0, 0) #set kick in beat 0, step 0
loop.set_sound(1, 1, 0) #snare in beat 1, step 0

loop.set_repeat(2, 2) #hats each 2 steps

loop.print_pattern() #display a scheme of the pattern

loop.play_once() #finally, play the loop once

