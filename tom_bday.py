def taumBday(b, w, bc, wc, z):
    cost_black = min(bc, wc + z)
    cost_white = min(wc, bc + z)
    return b * cost_black + w * cost_white