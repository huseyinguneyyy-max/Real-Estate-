def run(g=10, refmult=1.0, label=""):
    cum=0; peak=0; be=None; inv=0; pay=None; m12=m24=None
    for m in range(1,49):
        offices = 0 if m<7 else min(15+g*(m-7), 300)
        rev = offices*50 + (0 if m<5 else min(300+250*(m-5),6000)) + (0 if m<5 else min((2+(m-5))*250,10000))
        rev += 0 if m<9 else (500 if m<13 else 1000)
        rev += (0 if m<9 else (1000 if m<13 else 2000 if m<19 else 3000))*refmult
        cost = 5500 if m<=3 else (6500 if m<=12 else 8500 if m<=24 else 10000)
        if m==1: cost+=6000
        net=rev-cost; cum+=net; peak=min(peak,cum)
        if be is None and net>0: be=m
        if net>0 and pay is None: inv+=net*0.5
        if pay is None and inv>=60000: pay=m
        if m==12: m12=rev
        if m==24: m24=rev
    print(label,"peak",peak,"breakeven",be,"payback",pay,"rev12",m12,"rev24",m24)
run(label="base")
run(g=5,refmult=0.5,label="cons")
