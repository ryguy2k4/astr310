from math import sin, cos, acos, pi

def ymd2jd(y, m, d):
    return (1461 * (y + 4800 + (m - 14)//12))//4 + \
           (367 * (m - 2 - 12 * ((m - 14)//12)))//12 - \
           (3 * ((y + 4900 + (m - 14)//12)//100))//4 + d - 32075

def gst2ut(GST, JD):
    T  = (JD - 2451545.0) / 36525.0
    T0 = (6.697374558 + 2400.051336*T + 0.000025862*T**2) % 24.
    return 0.9972695663 * (GST - T0)

def dh2hms(dh):
    h = int(dh)
    m = int((dh - h)*60.)
    s = int((dh - h - m/60.)*3600.)
    return (h, m, s)

def riseandset(ra, dec, lam, phi, y, m, d):
    alpha = ra[0] + ra[1]/60 + ra[2]/3600
    delta = dec[0] + dec[1]/60 + dec[2]/3600

    d2r  = pi/180.
    cosH = -sin(lam*d2r)*sin(delta*d2r) / (cos(lam*d2r)*cos(delta*d2r))
    H    = (acos(cosH) / d2r / 15.04107) % 24.
    LSTr = (alpha - H) % 24.
    LSTs = (alpha + H) % 24.

    GSTr = (LSTr - phi/15.) % 24.
    GSTs = (LSTs - phi/15.) % 24.

    JD = ymd2jd(y, m, d)

    UTr = gst2ut(GSTr, JD) % 24.
    UTs = gst2ut(GSTs, JD) % 24.

    LTr = dh2hms(UTr - 6.)
    LTs = dh2hms(UTs - 6.)

    return LTr, LTs
