def devideFloor(width, height):
  if width == height:
    return height
  else:
    longer = max(width, height)
    short = min(width, height)

    i = 1
    while longer - short * i > 0:
      i = i+1

    remain = longer - short * (i - 1)
    return devideFloor(remain, short)  


print devideFloor(1680, 640)