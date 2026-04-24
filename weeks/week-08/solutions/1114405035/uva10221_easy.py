import sys, math

for line in sys.stdin:
    if not line.split(): continue
    s, a, unit = line.split()
    s, a = float(s), float(a)
    
    if unit == "min":
        a /= 60.0
        
    a %= 360
    if a > 180: a = 360 - a
        
    r = 6440 + s
    arc = r * math.pi * a / 180.0
    chord = 2 * r * math.sin(math.pi * a / 360.0)
    
    print(f"{arc:.6f} {chord:.6f}")