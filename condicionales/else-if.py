ingreso_mensual = 80000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bein, estas bien")
    else:
        print("ey pa, se esta gastando las lukas, hay que ver si te alcanza")    
    
elif ingreso_mensual > 1000:
    print("estas bien en latam")
    
elif ingreso_mensual > 850:
    print("estas bien en Colombia")
    
elif ingreso_mensual > 11:
    print("estas bien en Venezuela")
    
else:
    print("pobre hpta")