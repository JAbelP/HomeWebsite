
import tinytuya
print("d being set up")
d = tinytuya.BulbDevice('eb96216e45ecbd9093p4qn','192.168.1.229','9fa92d5b218dcebb')
d.set_version(3.3)
b =d.status()
print("Status set now")
print("Look here ",b)
d.set_colour(255,0,0)