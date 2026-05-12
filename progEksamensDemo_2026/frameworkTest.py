#Tjek requirements.txt for liste over krævede libraries.
try:
    import pandas as pd
    import matplotlib.pyplot as plt
except:
    print("FEJL: Manglende libraries! - Husk at installere pandas og matplotlib")
    exit()

print("Hvis du kan se en graf i pycharm nu, så virker det. :) - Held og lykke til eksamen!")
print("Hvis ikke, så tag kontakt til Mark og vis ham fejlbeskeden!")

data = pd.read_csv("frameworkTestData.csv")

data['Tid'] = pd.to_datetime(data['time'])
plt.figure(figsize=(10, 6))
plt.plot(data['Tid'], data['value'], label='data over tid')
plt.axhline(data['value'].min(), color='blue', linestyle='--', label='Minimum')
plt.axhline(data['value'].max(), color='red', linestyle='--', label='Maksimum')
plt.axhline(data['value'].mean(), color='green', linestyle='--', label='Gennemsnit')
plt.xlabel('x aksens titel')
plt.ylabel('y aksens titel')
plt.title('Titel på plot')
plt.legend()
plt.show()


