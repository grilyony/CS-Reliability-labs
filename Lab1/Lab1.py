with open("data.txt", "r") as nums:
    input_data = nums.read()

input_data = input_data.replace("\n", " ")
input_data = list(map(lambda x: int(x), input_data.split(", ")))
gamma = float(input("Gamma: "))
n = int(input("Interval num: "))
T1 = int(input("Time to measure probability: "))
T2 = int(input("Time to measure intensity: "))
T_avg = sum(input_data) / len(input_data)
interval = max(input_data) / n
densities = []
for i in range(n):
    num = 0
    for elem in input_data:
        num += 1 if interval * i < elem < interval * (i + 1) else 0
    densities.append(num / (len(input_data) * interval))
probabilities = [1 - sum(densities[:i]) * interval for i in range(n + 1)]
ti = list(map(lambda x: x < gamma, probabilities)).index(True)
ti_1 = ti - 1
d = (probabilities[ti_1] - gamma) / (probabilities[ti_1] - probabilities[ti])
T_gamma = ti_1 + interval * d


def work_probability(time):
    index = list(map(lambda x: x > time, [interval * i for i in range(n + 1)])).index(True) - 1
    return 1 - sum(densities[:index]) * interval - (time - interval * index) * densities[index], index


P_w, _ = work_probability(T1)
intensity, idx = work_probability(T2)
intensity = densities[idx] / intensity
print()
print(f"Average work time (Tср): {T_avg}")
print(f"γ-percentage work time (Tγ), γ = {gamma}: {T_gamma}")
print(f"Normal work probability at time {T1}: {P_w}")
print(f"Fail intensity at time {T2}: {intensity}")