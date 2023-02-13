atletas = []
record = 15.50
num_atletas = int(input("Cuantos atletas pasaron a la final "))

for atleta in range(num_atletas):

    nombre = input("Digite el nombre del atleta ")
    marca_atleta = float(input("Digite la marca del salto en (m) ")) 

    atletas.append(
        {
            "name": nombre,
            "marca": marca_atleta
        }
    )
    if(marca_atleta > record):
        print(f"NUEVOOO RECORDDDD!!! {nombre.upper()} acabas de romper el record de {record}m con {marca_atleta}m ")
        record = marca_atleta

name_camepon = ""
marca_campeon = 0

for atleta in atletas:
    if(atleta["marca"] > marca_campeon):
        marca_campeon = atleta["marca"]
        name_camepon = atleta["name"]

if(record == marca_campeon):
    print(f"EL GANADOR DE LA MEDALLA DE ORO Y CON UN NUEVO RECORD DE {marca_campeon}m ES {name_camepon.upper()}")
    print(f"{name_camepon} Felicitaciones!! se le depositaran 500 millones por romper el record olimpico")
else:
    print(f"EL GANADOR DE LA MEDALLA DE ORO CON UNA MARCA DE {marca_campeon}m ES {name_camepon.upper()}")
