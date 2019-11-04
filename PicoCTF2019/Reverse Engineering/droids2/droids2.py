"""
    This code does exactly what Dalvik assembly does.
    Output: dismass.ogg.weatherwax.aching.nitt.garlick
"""

v0 = [None]*6
v1 = 0x0
v2 = "weatherwax"
v0[v1] = v2
v1 = 0x1
v2 = "ogg"
v0[v1] = v2
v1 = 0x2
v2 = "garlick"
v0[v1] = v2
v1 = 0x3
v2 = "nitt"
v0[v1] = v2
v1 = 0x4
v2 = "aching"
v0[v1] = v2
v1 = 0x5
v2 = "dismass"
v0[v1] = v2

v1 = 0x3
v2 = v1-v1
v3 = v1//v1
v3 += v2
v4 = v3+v3
v4 -= v2
v5 = v1+v4
v6 = v5+v2
v6 -= v3

v7 = v0[v5]
v8 = ""
v7 = v8+v7
v8 += "."
v7 = v7+v8
v9 = v0[v3]
v7 = v7+v9
v7 = v7+v8
v9 = v0[v2]
v7 = v7+v9
v7 = v7+v8
v9 = v0[v6]
v7 = v7+v9
v7 = v7+v8
v9 = v0[v1]
v7 = v7+v9
v7 = v7+v8
v8 = v0[v4]
v7 = v7 + v8

print(v7)
