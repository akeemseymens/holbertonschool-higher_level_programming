#!/usr/bin/python3
for alphbt_lwr in range(ord('a'), ord('z')+1):
    if alphbt_lwr == 'e' or alphbt_lwr == 'q':
       continue
    print("{:c}".format(alphbt_lwr), end="")
