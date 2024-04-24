import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('onlinefoods.csv')

# Просмотр первых нескольких строк
print(data.head())

# Основные статистические характеристики
print(data.describe())

# Проверка наличия пропущенных значений
print(data.isnull().sum())

plt.figure(figsize=(10, 6))
data['Age'].value_counts().plot(kind='bar')
plt.title('Распределение клиентов по возрасту')
plt.xlabel('Возраст клиента')
plt.ylabel('Количество')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(data['Age'], data['Occupation'], alpha=0.5)
plt.title('Диаграмма разброса по возрасту и профессиям')
plt.xlabel('Age')
plt.ylabel('Occupation')
plt.show()

plt.figure(figsize=(10, 6))
data.boxplot(column='Age', by='Monthly Income', rot=45)
plt.title('Ящик с усами для возраста в зависимости от ежемесячного дохода')
plt.xlabel('Monthly Income')
plt.ylabel('Age')
plt.show()

category_counts = data['Age'].value_counts()

# Построение круговой диаграммы
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Products by age')
plt.show()