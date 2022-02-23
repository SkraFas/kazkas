from ssl import VERIFY_DEFAULT
from flask import Flask, render_template, request

app = Flask(__name__)
sale = [["xx","e", "xx", "p", "e", "xx", "e", "e", "xx", "xx", "xx", "p", "e", "xx", "xx"],
        ["e", "e", "e", "p", "e", "e", "e", "e", "e", "e", "e", "p", "e", "e", "e"],
        ["xx", "e", "e", "p", "e", "xx", "e", "e", "xx", "xx", "e", "p", "xx", "e", "xx"],
        ["e", "e", "xx", "p", "xx", "e", "xx", "xx", "e", "e", "e", "p", "e", "e", "xx"],
        ["e", "xx", "e", "p", "e", "xx", "e", "e", "e", "xx", "e", "p", "xx", "e", "e"],
        ["xx", "xx", "xx", "p", "e", "e", "xx", "xx", "xx", "e", "e", "p", "e", "xx", "xx"],
        ["e", "e", "e", "p", "e", "xx", "e", "e", "xx", "xx", "xx", "p", "e", "e", "xx"],
        ["vxx", "v", "p", "v", "vxx", "v", "v", "p", "vxx", "vxx"]]

   
@app.route("/", methods=["GET", "POST"])
def index():
    global sale   
    if request.method == "POST":
        veiksmas = request.values.get("action")
        match veiksmas:
            case "sale":
                vieta = request.values.get("kede").split(".")
                if sale[int(vieta[0])][int(vieta[1])] == "e":
                    sale[int(vieta[0])][int(vieta[1])] = "m"
                elif sale[int(vieta[0])][int(vieta[1])] == "m":
                    sale[int(vieta[0])][int(vieta[1])] = "e"
        
                if sale[int(vieta[0])][int(vieta[1])] == "s":
                    sale[int(vieta[0])][int(vieta[1])] = "sm"
                elif sale[int(vieta[0])][int(vieta[1])] == "sm":
                    sale[int(vieta[0])][int(vieta[1])] = "s"
                
                if sale[int(vieta[0])][int(vieta[1])] == "v":
                    sale[int(vieta[0])][int(vieta[1])] = "vm"
                elif sale[int(vieta[0])][int(vieta[1])] == "vm":
                    sale[int(vieta[0])][int(vieta[1])] = "v"
        
                if sale[int(vieta[0])][int(vieta[1])] == "vs":
                    sale[int(vieta[0])][int(vieta[1])] = "vsm"
                elif sale[int(vieta[0])][int(vieta[1])] == "vsm":
                    sale[int(vieta[0])][int(vieta[1])] = "vs"
            case "pirkti":
                for i in range(len(sale)):
                    for j in range(len(sale[i])):
                        if sale[i][j] == "m":
                            sale[i][j] = "x"
                        elif sale[i][j] == "sm":
                            sale[i][j] = "x"
                        elif sale[i][j] == "vm":
                            sale[i][j] = "vx"
                        elif sale[i][j] == "vsm":
                            sale[i][j] = "vx"
                for i in range(len(sale)):
                    for j in range(len(sale[i])):
                        if sale[i][j] == "s":
                            sale[i][j] = "e" 
                        elif sale[i][j] == "vs":
                            sale[i][j] = "v"
            case "reset":
                sale = ResetFunkcija(sale)
            case "grazinti":
                for i in range(len(sale)):
                    for j in range(len(sale[i])):
                        if sale[i][j] == "x":
                            sale[i][j] = "e"
                        elif sale[i][j] == "vx":
                            sale[i][j] = "v"
            case "suggest":
                kiekis = int(request.values.get("count"))
                sale = linija(sale, kiekis)

    return render_template("puslapis.html", eiles = sale)

def ResetFunkcija(vietos):
    vietos=[["xx","e", "xx", "p", "e", "xx", "e", "e", "xx", "xx", "xx", "p", "e", "xx", "xx"],
        ["e", "e", "e", "p", "e", "e", "e", "e", "e", "e", "e", "p", "e", "e", "e"],
        ["xx", "e", "e", "p", "e", "xx", "e", "e", "xx", "xx", "e", "p", "xx", "e", "xx"],
        ["e", "e", "xx", "p", "xx", "e", "xx", "xx", "e", "e", "e", "p", "e", "e", "xx"],
        ["e", "xx", "e", "p", "e", "xx", "e", "e", "e", "xx", "e", "p", "xx", "e", "e"],
        ["xx", "xx", "xx", "p", "e", "e", "xx", "xx", "xx", "e", "e", "p", "e", "xx", "xx"],
        ["e", "e", "e", "p", "e", "xx", "e", "e", "xx", "xx", "xx", "p", "e", "e", "xx"],
        ["vxx", "v", "p", "v", "vxx", "v", "v", "p", "vxx", "vxx"]]
    return vietos

def linija(vietos, kiekis):
    for i in range(len(vietos)):
        laisvosvietos = []
        for j in range(len(vietos[i])):

            if vietos[i][j] == "e" or vietos[i][j] == "s": 
                laisvosvietos.append(str(i)+"."+str(j))

            elif vietos[i][j] == "v" or vietos[i][j] == "vs": 
                if (kiekis % 2) == 0:
                    vip = 0
                    for k in range(len(vietos[i])):
                        if vietos[i][k] == "v":
                            vip += 1
                    if vip * 2 >= kiekis:
                        for k in range(len(vietos[i])):
                                if vietos[i][k] == "v":
                                    vietos[i][k] = "vs"

            if vietos[i][j] == "vxx" or vietos[i][j] == "vx" or vietos[i][j] == "xx" or vietos[i][j] == "x" or vietos[i][j] == "p" or len(vietos[i])- 1 == j:
                if len(laisvosvietos) >= kiekis:
                    for k in range(len(laisvosvietos)):
                        vieta = laisvosvietos[k].split(".")
                        vietos[int(vieta[0])][int(vieta[1])] = "s"
                laisvosvietos = []

    return vietos