# Icons for large number display (for large clock over 2 lines)

ful	= [ 0b00111, 0b01111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111 ] # Block with upper left rounded
fll	= [ 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b01111, 0b00111 ] # Block with lower left rounded
fur	= [ 0b11100, 0b11110, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111 ] # Block with upper right rounded
flr	= [ 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11111, 0b11110, 0b11100 ] # Block with lower right rounded
fub	= [ 0b11111, 0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000 ] # Upper bar
flb	= [ 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111 ] # Lower bar
fuln= [ 0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111 ] # Upper lower thin
fulk =[ 0b11111, 0b11111, 0b00000, 0b00000, 0b00000, 0b00000, 0b11111, 0b11111 ] # Upper lower thick


fontpkg = [ ful, fll, fur, flr, fub, flb, fuln , fulk ]

ul = 0
ll = 1
ur = 2
lr = 3
ub = 4
lb = 5
uln = 6
ulk = 7

emp = 32 # Empty block

# Numeric patterns 3x2

one     = [ [emp,  ll, emp], [ lb,  ul,  lb] ]
two     = [ [ulk, ulk,  ur], [ ll, uln, uln] ]
three   = [ [ulk, ulk,  ur], [uln, uln,  lr] ]
four    = [ [ ll,  lb,  ur], [emp, emp,  lr] ]
five    = [ [ ul, ulk, ulk], [uln, uln,  lr] ]
six     = [ [ ul, ulk, ulk], [ ll, uln,  lr] ]
seven   = [ [ ub,  ub,  ur], [emp,  ul, emp] ]
eight   = [ [ ul, ulk,  ur], [ ll, uln,  lr] ]
nine    = [ [ ll, ulk,  ur], [emp, emp,  lr] ]
zero    = [ [ ul,  ub,  ur], [ ll,  lb,  lr] ]

A       = [ [ ul,  ub,  ur], [ ll,  ub,  lr] ] #
B       = [ [ ul, ulk,  ur], [ ll, ult,  lr] ] #
C       = [ [ ul,  ub,  ub], [ ll,  lb,  lb] ] #
D       = [ [ ll,  ub,  ur], [ ul,  lb,  lr] ] #
E       = [ [ ul, ulk, ulk], [ ll, ult, ult] ] #
F       = [ [ ul, ulk, ulk], [ ll, emp, emp] ] #
G       = [ [ ul, ulk, ulk], [ ll, ult,  lr] ] #
H       = [ [ ul,  lb,  ur], [ ll,  ub,  lr] ] #
I       = [ [ ub,  ll,  ub], [ lb,  ul,  lb] ] #
J       = [ [emp,  ub,  ur], [ lb,  lb,  lr] ] #
K       = [ [ ul,  lb,  lr], [ ll, ult,  ur] ] #
L       = [ [ ul, emp, emp], [ ll,  lb,  lb] ] #
M       = [ [ lr,  lb,  ll], [ ll, emp,  lr] ] #
N       = [ [ ur,  lb,  ul], [ ll, emp,  lr] ] #
O       = [ [ ul,  ub,  ur], [ ll,  lb,  lr] ] #
P       = [ [ ul, ulk,  ur], [ ll, emp, emp] ] #
Q       = [ [ ul,  ub,  ur], [ ll,  ub,  ur] ] #
R       = [ [ ul, ulk,  ur], [ ll, emp,  ul] ] #
S       = [ [ ul, ulk,  ub], [ult, ult,  lr] ] #
T       = [ [ ub,  ul,  ub], [emp,  ll, emp] ] #
U       = [ [ ul, emp,  ur], [ ll,  lb,  lr] ] #
V       = [ [ lr, emp,  ll], [emp,  ul, emp] ] #
W       = [ [ ul, emp,  ur], [ ur,  ub,  lr] ] #
X       = [ [ lr,  lb,  ll], [ ur,  ub,  ul] ] #
Y       = [ [ lr,  lb,  ll], [emp,  ub, emp] ] #
Z       = [ [ ub, ulk,  ll], [ ur,  ub,  lb] ] #

numbers = [ zero, one, two, three, four, five, six, seven, eight, nine ]
alphas = [ A, B, C, D, E, F, G, H, I, J, K, L, M, N, O P, Q, R, S, T, U, V, W, X, Y, Z ]
