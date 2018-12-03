"""
Credit to /u/om_henners on Reddit for this solution.

"""

import numpy as np
import parse

claim_matcher = '''#{id:d} @ {x:d},{y:d}: {width:d}x{height:d}\n'''
fabric = np.zeros((1000, 1000), dtype=np.int)


for line in open('input.txt'):
    r = parse.parse(claim_matcher, line)
    claim = fabric[r['y']: r['y'] + r['height'], r['x']: r['x'] + r['width']]
    claim[:] = claim + 1


for line in open('input.txt'):
    r = parse.parse(claim_matcher, line)
    claim = fabric[r['y']: r['y'] + r['height'], r['x']: r['x'] + r['width']]

    if claim.max() == 1:
        print(r['id'])
