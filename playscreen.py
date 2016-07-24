from browser import window
from browser import console
global melonjs
melonjs = window.me
from javascript import JSObject
from javascript import JSConstructor

class ScreenObject:
    
    #funky = JSConstructor(melonjs.ScreenObject)
    #console.log("HI {0}".format(funky))
    def __init__(self):
      funky = JSConstructor(melonjs.ScreenObject)
      #self = funky()
      #self.bind('reset', self.reset)
      
    def reset(self):
      pass
      
    def destroy(self):
      pass

class PlayScreen(melonjs.ScreenObject):
  
    # action to perform on state change
    def onResetEvent(self, *args):        
        melonjs.game.reset()

        # add the background & foreground
        # add the foreground
        background_sprite10 = melonjs.Sprite(0, 0,   { "image": melonjs.loader.getImage("background")})
        
        # add all objects
        melonjs.game.world.addChild(background_sprite10, 0)

    # action to perform when leaving this screen (state change)     
    def onDestroyEvent(self, *args): 
        pass
        # remove the HUD from the game world
        #melonjs.game.world.removeChild(this.HUD)

        # stop some music
        # melonjs.audio.stopTrack()

    
