import time
from random import randint
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
i = 0
while i < 5:
	x = randint(-126, 126)
	y = randint(-62, 62)
	z = randint(-126, 126)
	block = mc.getBlock(x, y, z)
	if block == 0:
		mc.player.setPos(x, y, z)
		time.sleep(5)
		i += 1
