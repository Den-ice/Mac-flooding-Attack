Mac-Flooding attack simulation

#This was done over a virtual switch to test over a few different security types.

#The first is the MAC-flooding attack by having an “attacker” program where the “attacker” is sending ethernet frames in mass quantities, each with a different spoofed MAC address. 

#The second form of attack is a subtler one: the “attacker” program instead sends only one or a small number of falsified MAC addresses. This is harder to detect, and can bypass several security measures that block floods. 

#The third form of attack is called the CAM Overflow attack. CAM means Content Addressable Memory. CAM Table Overflow is a Layer 2 attack on a switch.A switch’s CAM table contains network information; available MAC address on switch ports and connected VLAN parameters). CAM Table Overflows occur when an influx of MAC addresses are flooded into the table and the CAM table threshold is reached. This attack is very similar to the first method of attack.
