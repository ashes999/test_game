from browser import console
import sys
import jabal

console.log("Running Python v{0}!".format(sys.version))

# Generates a JS error, see: https://github.com/brython-dev/brython/issues/458
from awesome import awesome_math
from awesome.bestest import magic

# fearsome.py
import fearsome
console.log(fearsome.say_hi())

jabal.init(800, 600)
jabal.load_audio(["blip.lol"])

s = awesome_math.get_awesomeness()
m = magic.magic_number() + 1

print("S is {0}".format(s))
print("Magic is {0}".format(m))

e = jabal.Entity().size(48, 48).move(32, 16).move_with_keyboard().colour('red')

def play_blip(t):
    jabal.play_audio("blip")  
    e.colour('blue')
    
e.on_click(play_blip)

# import awesome.randme doesn't work
# import randme does
import randme
console.log(randme.randit())

