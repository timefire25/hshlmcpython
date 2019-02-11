from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=0
y=60
z=0
mc.setBlock(x, y-1 , z, 57)
mc.player.setPos(x, y, z)
