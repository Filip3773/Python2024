s_g=int(input("Unesi sadasnju godinu:"))
m_g=int(input("Koliko godina ima  Milos danas?"))
def godina_rodjenja():
    return s_g-m_g

a = str(godina_rodjenja())
print("Milos je rodjen "+ a +" godine.")