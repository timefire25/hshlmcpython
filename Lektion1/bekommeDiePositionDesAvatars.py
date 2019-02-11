from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positionDesSpielers = mc.player.getPos()
#Alternativ: positionDesSpielers = mc.player.getTilePos()
x=positionDesSpielers.x
y=positionDesSpielers.y
z=positionDesSpielers.z

mc.postToChat(str(x) + " " + str(y) + " " + str(z))


