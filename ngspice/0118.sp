* ex1
.global 0
V1 0 1 SIN(0 5m 100)
R1 1 2 1000
R2 2 3 0.00315
C2 2 3 10p
R3 3 4 10
R4 4 0 1.7
.TRAN 0.1m 50m
.control
run
*plotting input and output voltages
plot V(1) V(3)
.end