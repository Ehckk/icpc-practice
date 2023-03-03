import sys

def arrange_towers(towers):
	tower = towers[6]
	blocks = towers[:6]
	for block1 in blocks:
		arranged = []
		height = 0
		if block1 >= tower: continue
		height += block1
		arranged.append(block1)
		for block2 in blocks:
			if block1 == block2: continue
			if height + block2 >= tower: continue
			height += block2
			arranged.append(block2)
			for block3 in blocks:
				if block3 == block1 or block3 == block2: continue
				if height + block3 == tower:
					arranged.append(block3)
					arranged.sort(reverse=True)
					blocks.sort(reverse=True)
					for block in blocks:
						if block not in arranged:
							arranged.append(block)
					return arranged
			arranged.pop()
			height -= block2

for i in sys.stdin:
    line = i.split()
    tower_blocks = []
    for block in line:
        tower_blocks.append(int(block))
    print(' '.join([str(num) for num in arrange_towers(tower_blocks)]))
