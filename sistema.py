import csv
import matplotlib.pyplot as plt
import seaborn as sns

hospitais = []

with open("A2_PSE_EficienciaHospitalar.csv", "r", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        hospitais.append({
            "hospital": linha["hospital"],  
            "leitos": int(linha["leitos"]),
            "atendimentos": int(linha["atendimentos"]),
            "obitos": int(linha["obitos"])
        })

for h in hospitais:
    h["taxa_mortalidade"] = h["obitos"] / h["atendimentos"]
    h["ocupacao"] = h["atendimentos"] / h["leitos"]

print("Dados lidos e processados:\n")
for h in hospitais:
    print(h)


plt.figure(figsize=(6, 4))

x = [h["leitos"] for h in hospitais]
y = [h["taxa_mortalidade"] for h in hospitais]
labels = [h["hospital"] for h in hospitais]

sns.scatterplot(x=x, y=y, s=120)

for i in range(len(labels)):
    plt.text(x[i] + 1, y[i], labels[i])

plt.title("Relação entre Leitos e Taxa de Mortalidade")
plt.xlabel("Leitos")
plt.ylabel("Taxa de Mortalidade")
plt.grid(True)
plt.show()

plt.figure(figsize=(4, 2))

ocupacao_dict = {h["hospital"]: h["ocupacao"] for h in hospitais}
heatmap_data = [[ocupacao_dict[h["hospital"]] for h in hospitais]]

sns.heatmap(
    heatmap_data,
    annot=[[ocupacao_dict[h["hospital"]] for h in hospitais]],
    fmt=".2f",
    cmap="coolwarm",
    xticklabels=[h["hospital"] for h in hospitais],
    yticklabels=["Ocupação"]
)

plt.title("Mapa de Calor - Ocupação Hospitalar")
plt.show()
