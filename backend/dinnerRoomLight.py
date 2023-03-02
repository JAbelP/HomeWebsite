
import tinytuya
print("d being set up")
d = tinytuya.BulbDevice('XXXXXXXXXXXXX','XXX.XXX.X.xxx','XXXXXXXXXXXXXXX')
d.set_version(3.3)
b =d.status()
print("Status set now")
print("Look here ",b)
d.set_colour(255,0,0)
