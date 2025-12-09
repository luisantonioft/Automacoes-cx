import pandas as pd

df = pd.read_csv("../dados/atendimentos.csv")

# CSAT médio
csat_medio = df["satisfacao"].mean()

# Tempo médio de atendimento
tma = df["tempo_atendimento_min"].mean()

# FCR (% resolvido)
fcr = (df["resolvido"] == "sim").mean() * 100

print("📊 MÉTRICAS DE CX")
print(f"CSAT médio: {csat_medio:.2f}")
print(f"TMA médio (min): {tma:.1f}")
print(f"FCR (% resolvido): {fcr:.1f}%")
