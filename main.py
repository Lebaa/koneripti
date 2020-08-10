import csv

from datetime import datetime

sauron_lista = []
sccm_lista = []
molemmissa_lista = []
luokkalista = []
yleiskoneet = ("africa", "latin", "europe", "lakes", "mountains", "sovjet", "rho", "finland", "maa-aula", "ohte")

def c(t):
    ttime = datetime.strptime(t, "%m/%d/%Y")
    return (datetime.now() - ttime).days


with open("/home/lehmik/Downloads/results.csv", "r") as sauron_dump, open("/home/lehmik/Downloads/konelista.csv", "r") as sccm_dump:
    for row in csv.reader(sccm_dump):
        if row[0].startswith(yleiskoneet):
            luokkalista.append(row)
        else:
            k1 = ""
            k2 = ""
        try:
            k1 = row[1].split("\\")[1]
            if "asentaja" in k1:
                k1 = ""
        except IndexError:
            k1 = ""

        try:
            k2 = row[2].split("\\")[1]
            if "asentaja" in k2:
                k2 = ""
        except IndexError:
            k2 = ""

        sccm_lista.append([row[0].lower(), k1, k2])

    for row in csv.reader(sauron_dump):
        sauron_lista.append([
          row[0].split(".")[0].lower(),
          row[6],
          row[7],
          row[8],
          row[9],
          row[12],
          row[19],
        ])


for line in sccm_lista:
    for sauron_rivi in sauron_lista:
        if line[0] in sauron_rivi:
            molemmissa_lista.append([sauron_rivi[0],sauron_rivi[1],sauron_rivi[2],sauron_rivi[3],sauron_rivi[4],sauron_rivi[5],sauron_rivi[6],line[1],line[2]])

with open("/home/lehmik/Downloads/poistoehdokkaat.csv","w") as poisto, open("/home/lehmik/Downloads/staff-koneet.csv", "r") as ad:
    poistowriter = csv.writer(poisto)
    poistowriter.writerow([
    "Hostname",
    "Sauronissa käyttäjä",
    "Osasto",
    "Sijainti",
    "Info",
    "Malli",
    "DHCP date",
    "LastLogonDate"
    ])
    poistowriter.writerow("\n")
    for kone in csv.reader(ad):
        for row in molemmissa_lista:
            if kone[0] == row[0]:
                if row[7] == "" and row[8] == "" and c(row[6].split(" ")[0]) >180:
                    poistowriter.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],kone[1]])



