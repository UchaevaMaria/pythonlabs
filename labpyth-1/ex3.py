import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Товар": ["Ноутбук", "Телефон", "Планшет", "Телефон", "Ноутбук", "Планшет", "Ноутбук", "Телефон"],
    "Цена": [50000, 30000, np.nan, 32000, 51000, 28000, np.nan, 29500],
    "Количество": [10, 5, 0, 1200, 8, 3, 2, 100] # созданм DataFrame с пропусками и выбросами
}
df = pd.DataFrame(data)

# 2. Заполнение пропусков в "Цена" медианой
median_price = df["Цена"].median()
df["Цена"].fillna(median_price, inplace=True) #заполнение пропусков в медианой

df = df[(df["Количество"] >= 1) & (df["Количество"] <= 1000)]#удаление выбросов по "Количество" (<1 или >1000)

df["Общая_стоимость"] = df["Цена"] * df["Количество"]#новый столбец "Общая_стоимость"
revenue = df.groupby("Товар")["Общая_стоимость"].sum()
#построение графика
plt.figure(figsize=(8, 5))
revenue.plot(kind="bar")
plt.title("Выручка по товарам")
plt.xlabel("Товар")
plt.ylabel("Суммарная выручка")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Обработанный DataFrame:")
print(df)

print("\nСуммарная выручка по каждому товару:") #вывод итоговой выручки
print(revenue)