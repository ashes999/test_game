from awesome.awesome_math import AwesomeMath

Jabal.init(800, 600)
Jabal.load_audio(["blip.wav"])

s = AwesomeMath.get_awesomeness()
e = Entity().size(s, s).colour('red').move(32, 16).move_with_keyboard()
e.on_click(lambda: Jabal.play_audio("blip"))
