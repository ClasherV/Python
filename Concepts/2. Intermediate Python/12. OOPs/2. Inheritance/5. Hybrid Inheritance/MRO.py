"""
C-3 Linearization

Linearization(D)=D+merge(L(B),L(C),BC)
L(B)=B+merge(L(A),A)
L(A)=A+merge(L(O),O)=A+merge(O,O)=A+O=AO
L(B)=B+merge(AO,A)=BA+merge(O)=BAO
L(C)=C+merge(L(A),A)=C+merge(AO,A)=CA+merge(O)=CAO
L(D)=D+merge(BAO,CAO,BC)=DB+merge(AO,CAO,C)=DBC+merge(AO,AO)=DBCA+merge(O,O)=DBCAO

Head which is not present in any tail is considered good head
"""