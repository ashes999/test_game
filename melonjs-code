from browser import console
import sys
import jabal
from playscreen import PlayScreen

console.log("Running Python v{0}!".format(sys.version))

resources = [
    # background
    { "name": "background", "type": "image", "src": "data/img/background/bg_dirt128.png" },
    # upper part of foreground
    { "name": "grass_upper", "type": "image", "src": "data/img/foreground/grass_upper128.png" },
    # lower part of foreground
    { "name": "grass_lower", "type": "image", "src": "data/img/foreground/grass_lower128.png" },
    # more sprites
    { "name": "mole", "type": "image", "src": "data/img/sprites/mole.png" },

    # bitmap font
    { "name": "PressStart2P", "type":"image", "src": "data/fnt/PressStart2P.png" },
    { "name": "PressStart2P", "type":"binary", "src": "data/fnt/PressStart2P.fnt"},

    # main music track
    { "name": "whack", "type": "audio", "src": "data/bgm/" },
    # Laugh audio FX
    # { "name": "laugh", "type": "audio", "src": "data/sfx/" },
    # ow audio FX
    { "name": "ow", "type": "audio", "src": "data/sfx/" }
]

jabal.init(800, 600, resources, PlayScreen())
#jabal.load_audio(["blip.lol"])

#e = jabal.Entity().size(48, 48).move(32, 16).move_with_keyboard().colour('red')
  
#e.on_click(lambda: jabal.play_audio("blip"))
