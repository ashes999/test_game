from browser import window
from browser import console
from javascript import JSConstructor

global melonjs
melonjs = window.me

# Facade, delegates to JS
class ScreenObject:

	def __init__(self):
		self.jsScreen = JSConstructor(melonjs.ScreenObject)()

	def reset(self):
		self.jsScreen.reset()

	def destroy(self):
		self.jsScreen.destroy()


class PlayScreen(ScreenObject):

	def __init__(self):
		super(PlayScreen, self).__init__()

	def onResetEvent(self):
		console.log("Resetting with {0}, g={1}".format(args, melonjs.game))
		melonjs.game.reset()

		# add the background & foreground
		# add the foreground
		background_sprite10 = window.melonjs.Sprite(0, 0,   { "image": melonjs.loader.getImage("background")})
		background_sprite10 = window.copyBrythonMethodsToObjectRoot(background_sprite10)

		# add all objects
		melonjs.game.world.addChild(background_sprite10, 0)

		console.log("Houston, we have liftoff~!")

	# action to perform when leaving this screen (state change)
	def onDestroyEvent(self):
	    pass
	    # remove the HUD from the game world
	    #melonjs.game.world.removeChild(this.HUD)

	    # stop some music
	    # melonjs.audio.stopTrack()
