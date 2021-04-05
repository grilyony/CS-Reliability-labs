from math import log, factorial
from lab2.lab2 import calc_P_Sys


N = input("Input number of elements: ")
while not N.isnumeric():
    N = input("Incorrect value, try again:")
N = int(N)

while True:
    ps = input("Input probabilities: ").strip()
    try:
        ps = list(map(lambda x: float(x), ps.split(" ")))
        if len(ps) == N:
            break
        else:
            print("Incorrect number of probabilities!")
    except ValueError:
        print("Incorrect input")

T_in = input("Input time: ")
while not T_in.isnumeric():
    T_in = input("Incorrect value, try again:")
T_in = int(T_in)

K1 = input("Input K1: ")
while not K1.isnumeric():
    K1 = input("Incorrect value, try again:")
K1 = int(K1)

K2 = input("Input K2: ")
while not K2.isnumeric():
    K2 = input("Incorrect value, try again:")
K2 = int(K2)

P_sys = calc_P_Sys(N, "data.txt", ps)
Q_sys = 1 - P_sys
t_avg = -T_in / log(P_sys)

print(f"Базова імовірність безвідмовної роботи = {P_sys}\n"
      f"Базова імовірність відмови = {Q_sys}\n"
      f"Базовий середній наробіток на відмову = {t_avg}\n")


def load_general(t, k1, Q_sys, P_sys, t_avg):
    q1 = pow(Q_sys, (k1 + 1))
    p1 = 1 - q1
    t_avg1 = -t / log(p1)
    gq1 = q1 / Q_sys
    gp1 = p1 / P_sys
    gt1 = t_avg1 / t_avg
    print(f"Імовірність безвідмовної роботи системи з навантаженим загальним резервуванням = {p1}\n"
          f"Імовірність відмови системи з навантаженим загальним резервуванням = {q1}\n"
          f"Середній час роботи системи з навантаженим загальним резервуванням = {t_avg1}")
    print(f"Виграш системи з навантаженим загальним резервуванням по імовірності безвідмовної роботи = {gp1}\n"
          f"Виграш системи з навантаженим загальним резервуванням по імовірності відмови = {gq1}\n"
          f"Виграш системи з навантаженим загальним резервуванням по середньому часу роботи = {gt1}\n")


def unloaded_general(t, k1, Q_sys, P_sys, t_avg):
    q1 = pow(Q_sys, (k1 + 1)) / factorial(k1 + 1)
    p1 = 1 - q1
    t_avg1 = -t / log(p1)
    gq1 = q1 / Q_sys
    gp1 = p1 / P_sys
    gt1 = t_avg1 / t_avg
    print(f"Імовірність безвідмовної роботи системи з ненавантаженим загальним резервуванням = {p1}\n"
          f"Імовірність відмови системи з ненавантаженим загальним резервуванням = {q1}\n"
          f"Середній час роботи системи з ненавантаженим загальним резервуванням = {t_avg1}")
    print(f"Виграш системи з ненавантаженим загальним резервуванням по імовірності безвідмовної роботи = {gp1}\n"
          f"Виграш системи з ненавантаженим загальним резервуванням по імовірності відмови = {gq1}\n"
          f"Виграш системи з ненавантаженим загальним резервуванням по середньому часу роботи = {gt1}\n")


def loaded_distribute(t, k2, Q_sys, P_sys, ps, t_avg, N):
    new_ps = list(map(lambda x: 1 - (1 - x) ** (k2 + 1), ps))
    p2 = calc_P_Sys(N, 'data.txt', new_ps)
    q2 = 1 - p2
    t_avg2 = -t / log(p2)
    gq2 = q2 / Q_sys
    gp2 = p2 / P_sys
    gt2 = t_avg2 / t_avg
    print(f"Імовірність безвідмовної роботи системи з навантаженим розподіленим резервуванням = {p2}\n"
          f"Імовірність відмови системи з навантаженим розподіленим резервуванням = {q2}\n"
          f"Середній час роботи системи з навантаженим розподіленим резервуванням = {t_avg2}")
    print(f"Виграш системи з навантаженим розподіленим резервуванням по імовірності безвідмовної роботи = {gp2}\n"
          f"Виграш системи з навантаженим розподіленим резервуванням по імовірності відмови = {gq2}\n"
          f"Виграш системи з навантаженим розподіленим резервуванням по середньому часу роботи = {gt2}\n")


def unloaded_distribute(t, k2, Q_sys, P_sys, ps, t_avg, N):
    new_ps = list(map(lambda x: 1 - (1 - x) ** (k2 + 1) / factorial(k2 + 1), ps))
    p2 = calc_P_Sys(N, 'data.txt', new_ps)
    q2 = 1 - p2
    t_avg2 = -t / log(p2)
    gq2 = q2 / Q_sys
    gp2 = p2 / P_sys
    gt2 = t_avg2 / t_avg
    print(f"Імовірність безвідмовної роботи системи з ненавантаженим розподіленим резервуванням = {p2}\n"
          f"Імовірність відмови системи з ненавантаженим розподіленим резервуванням = {q2}\n"
          f"Середній час роботи системи з ненавантаженим розподіленим резервуванням = {t_avg2}")
    print(f"Виграш системи з ненавантаженим розподіленим резервуванням по імовірності безвідмовної роботи = {gp2}\n"
          f"Виграш системи з ненавантаженим розподіленим резервуванням по імовірності відмови = {gq2}\n"
          f"Виграш системи з ненавантаженим розподіленим резервуванням по середньому часу роботи = {gt2}\n")


load_general(T_in, K1, Q_sys, P_sys, t_avg)
unloaded_general(T_in, K1, Q_sys, P_sys, t_avg)
loaded_distribute(T_in, K2, Q_sys, P_sys, ps, t_avg, N)
unloaded_distribute(T_in, K2, Q_sys, P_sys, ps, t_avg, N)