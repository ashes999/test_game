from browser import console
import sys
import jabal

console.log("Running Python v{0}!".format(sys.version))

resources = []

jabal.init(800, 600)
jabal.load_audio(["blip.wav"])

e = jabal.Entity().size(48, 48).move(32, 16).move_with_keyboard().colour('red')

def on_click():
	jabal.play_audio("blip")
	e.colour("blue")
	
e.on_click(on_click)