import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("temperaturer.csv", sep=";", encoding='utf8')
print("Loaded CSV! Header: " + str(df.columns.tolist()))
for patient in df.columns.tolist()[1:]:
    print('Fandt patient: ' + patient + '.')

def udskriv_graf():
    ax = plt.gca() #opsætning af plot
    df.plot(kind='line', x='Nr', y='Niels Jensen',color='red', ax=ax)
    #df.plot(kind='line', x='Nr', y='Jens Olsen', ax=ax)
    #plt.xticks(rotation=90)
    plt.show()
    menu()

def gem():
    df.to_csv("temperaturer.csv", sep=";", encoding='utf8')

def daglige_indtastninger():
    global df

    patient = input("Indtast patientnavn: ")
    temperatur = float(input("Indtast temperatur: "))
    sidste_temp = df[patient].dropna().iloc[-1]

    if temperatur - sidste_temp > 1:
        print("ALARM! Temperaturen er steget mere end 1 grad!")

    ny_række = {}

    # næste nummer
    nyt_nr = df['Nr'].max() + 1
    ny_række['Nr'] = nyt_nr

    # tomme værdier til alle patienter
    for kolonne in df.columns[1:]:
        ny_række[kolonne] = None

    # indsæt temperatur hos valgt patient
    ny_række[patient] = temperatur

    # tilføj rækken
    df.loc[len(df)] = ny_række

    # gem fil
    df.to_csv("temperaturer.csv", sep=";", encoding='utf8', index=False)

    print("Temperatur gemt!\n")
    menu()

def afslut():
    print("Tak for nu!")


def menu():
    print("Indtast dit valg (g = udskriv graf q = afslut d = daglige indtastninger)")
    valg = input("Indtast dit valg:")
    if (valg == 'g'):
        udskriv_graf()
    if (valg == 'q'):
        afslut()
    if (valg == 'd'):
        daglige_indtastninger()

menu()

