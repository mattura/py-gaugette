# Sample code for both the RotaryEncoder class and the Switch class.
# The common pin for the encoder should be wired to ground.
# The sw_pin should be shorted to ground by the switch.

import gaugette.rotary_encoder
import gaugette.switch

A_PIN  = 7
B_PIN  = 9
SW_PIN = 8

encoder = gaugette.rotary_encoder.RotaryEncoder(A_PIN, B_PIN)
switch = gaugette.switch.Switch(SW_PIN)
last_state = None

while 1:
    delta = encoder.delta()
    if delta!=0:
        print "rotate %d" % delta

    sw_state = switch.state()
    if sw_state != last_state:
        print "switch %d" % sw_state
        last_state = sw_state
        