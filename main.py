from browser import console
import sys
import jabal

console.log("Running Python v{0}".format(sys.version))

from awesome import awesome_math

# fearsome.py
import fearsome
console.log(fearsome.say_hi())

jabal.init(800, 600)
jabal.load_audio(["blip.wav"])

s = awesome_math.get_awesomeness()
print("S is {0}".format(s))

e = jabal.Entity().size(s, s).move(32, 16).move_with_keyboard().image('assets/images/avatar.png')
e.on_click(lambda: jabal.play_audio("blip"))

# import awesome.randme doesn't work
# import randme does
import randme
console.log(randme.randit())
