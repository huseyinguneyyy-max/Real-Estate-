import sys
def run(scale=1.0, inv_first=0.7, equity=0.5, cap=None, show=False):
    cum=0; peak=0; rows=[]
    for m in range(1,37):
        off = 0 if m<6 else min(10+12*(m-6), 350)
        subs = off*60
        dop = 0 if m<5 else min(300+300*(m-5), 8000)
        proj = 0 if m<4 else min(3+2*(m-4), 60)*250
        ref = 0 if m<8 else (1500 if m<10 else 3000 if m<19 else 6000)
        bank = 0 if m<9 else 1000
        rev = (subs+dop+proj+ref+bank)*scale
        cost = 7000 if m<=3 else (8500 if m<=15 else 11000 if m<=24 else 13000)
        if m==1: cost+=6000
        net = rev-cost
        rows.append([m,off,rev,cost,net])
    # cash before distributions
    c=0; pk=0
    for r in rows:
        if r[4]<0: c+=r[4]; pk=min(pk,c)
        else: break
    capital = cap or 65000
    paid=0; first=None; back=None; cash=capital; out=[]
    for m,off,rev,cost,net in rows:
        cash += net
        dist = 0
        if net>0 and cash>3000:  # keep min buffer
            share = inv_first if paid<capital else equity
            dist = min(net*share, cash-3000)
            paid += dist; cash -= dist
            if back is None and paid>=capital: back=m
        out.append((m,off,rev,cost,net,dist,paid,cash))
    if show:
        for o in out: print("%2d off=%3d rev=%6.0f cost=%6.0f net=%6.0f inv=%6.0f invcum=%7.0f cash=%7.0f"%o)
    m12=[o[5] for o in out if o[0]>=12]
    print(f"scale={scale} capital≈£{capital} payback month={back} inv@m12=£{out[11][5]:.0f} min inv m12-36=£{min(m12):.0f} total paid 36m=£{paid:.0f} rev m12=£{out[11][2]:.0f} m24=£{out[23][2]:.0f}")
run(show=True)
run(scale=0.75)
run(scale=0.6)
