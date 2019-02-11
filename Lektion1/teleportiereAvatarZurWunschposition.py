from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = int(input("Geben Sie eine X-Koordinate an: "))
y = int(input("Geben Sie eine Y-Koordinate an: "))
z = int(input("Geben Sie eine Z-Koordinate an: "))
Block =  mc.getBlock(x, y, z)
if Block == 0:
	mc.player.setPos(x, y, z)
else:
	Hoehe = mc.getHeight(x, z)
	mc.player.setPos(x, Hoehe, z)
