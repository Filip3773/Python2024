def cm_u_m(cm):
    m = cm / 100
    return m


rasto_m_ucm= 324

metri = cm_u_m(rasto_m_ucm)
print(f"{rasto_m_ucm} cm ima {metri} metara.")