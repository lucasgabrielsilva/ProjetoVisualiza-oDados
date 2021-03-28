import pandas as pd
import numpy as np

mlsBase = pd.read_csv('./bases/mlsAllPlayers.csv')
fifaBase = pd.read_csv('./bases/fifaAllPlayers.csv')

added = 0

newBase = np.array([
    "Nome",
    "Pais",
    "Clube",
    "Posição",
    "Altura",
    "Peso",
    "Pé Preferencial",
    "Nº de Jogos",
    "Nº de Jogos Iniciados",
    "Nº Minutos Jogados",
    "Nº de Gols",
    "Nº de Gols da Vitoria",
    "Nº de Gols Mandante",
    "Nº de Gols Visitante",
    "Nº de Assistências",
    "Nº de Assistências Mandante",
    "Nº de Assistências Visitante",
    "Nº de Chutes",
    "Nº de Chutes no Gol",
    "Chutes por Gol",
    "Nº de Faltas Sofridas",
    "Nº de Faltas Cometidas",
    "Nº de Cartões Amarelos",
    "Nº de Cartões Vermelhos",
    "Temporada"])

positionsBr = {
    "GK":"Goleiro",
    "RB":"Lateral",
    "LB":"Lateral",
    "CB":"Zagueiro",
    "LCB":"Zagueiro",
    "RCB":"Zagueiro",
    "CDM":"Volante",
    "RDM":"Volante",
    "LDM":"Volante",
    "CM": "Meia",
    "RCM": "Meia",
    "LCM": "Meia",
    "RM": "Meia",
    "LM": "Meia",
    "CAM":"Meia",
    "RAM": "Meia",
    "LAM": "Meia",
    "LF": "Atacante",
    "RF": "Atacante",
    "RW": "Ponta",
    "LW": "Ponta",
    "ST": "Atacante",
    "LS": "Atacante",
    "RS": "Atacante",
    "RWB": "Ponta",
    "LWB": "Ponta",
    "CF": "Atacante",
    "D": "Defensor",
    "M": "Meia",
    "F": "Atacante",
    "NAN": "ERRO",
}

clubNames = {
    "TB": "Tampa Bay Mutiny", 
    "NE": "New England Revolution",
    "MIA": "Inter Miami CF", 
    "CLB": "Columbus Crew", 
    "DAL": "FC Dallas", 
    "KC": "Kansas City Wizards", 
    "CHI": "Chicago Fire FC", 
    "RSL": "Real Salt Lake City",
    "SJ": "San José",
    "LA": "Los Angeles Galaxy",
    "MET": "New York Red Bulls",
    "DC": "DC United",
    "CHV": "Club Deportivo Chivas USA",
    "TOR": "Toronto FC",
    "COL": "Colorado Rapids",
    "HOU": "Houston Dynamo FC",
    "NY": "New York Red Bulls",
    "NSH": "Nashville SC",
    "POR": "Portland Timebers",
    "SKC": "Sporting Kansas City",
    "LAFC": "Los Angeles FC",
    "VAN": "Vancouver Whitecaps FC", 
    "SEA": "Seatle Sounders",
    "MIN": "Minnesota United",
    "PHI": "Philadelphia Union", 
    "MTL": "Club de Foot Montréal",
    "PAN": "Club Deportivo Chivas USA",
    "ORL": "Orlando City SC",
    "CIN": "Cincinnati FC",
    "ATL": "Atlanta United",
    "USA": "Philadelphia Union",
    "NYC": "New York City FC", 
    "CIV": "Club de Foot Montréal",
    "NYR": "New York Red Bulls",
    "CAN": "Philadelphia Union",
    "RBNY": "New York Red Bulls",
    "LFC": "Los Angeles FC",
    "GHA": "DC United",
    "MTQ": "Seatle Sounders",
    "JAM": "Seatle Sounders",
    "ECU": "Club Deportivo Chivas USA",
    "SLV": "Club Deportivo Chivas USA",
    "HAI": "Real Salt Lake City",
    "ROC": "Houston Dynamo FC",
    "HON": "New England Revolution",
    "CHI": "Chicago Fire FC",
    "NAN": "ERRO"
}


for i, rowMls in mlsBase.iterrows():
    playerMls = rowMls['Player'].upper().replace(" ", "")
    if(rowMls['GP'] > 0):
        for j, rowFifa in fifaBase.iterrows():
            playerFifa = rowFifa['Name'].upper().replace(" ", "")
            if(playerMls == playerFifa):
                pos = rowMls['POS'][0] if (rowFifa['Club_Position'] == "Sub" or rowFifa['Club_Position'] == "Res") else str(rowFifa['Club_Position']).upper().replace(" ", "")
                tmp = np.array([
                    rowFifa['Name'],
                    rowFifa['Nationality'],
                    clubNames[str(rowMls['Club']).upper().replace(" ", "")],
                    positionsBr[pos],
                    rowFifa['Height'],
                    rowFifa['Weight'],
                    rowFifa['Preffered_Foot'],
                    rowMls['GP'],
                    rowMls['GS'],
                    rowMls['MINS'],
                    rowMls['G'],
                    rowMls['GWG'],
                    rowMls['HmG'],
                    rowMls['RdG'],
                    rowMls['A'],
                    rowMls['HmA'],
                    rowMls['RdA'],
                    rowMls['SHTS'],
                    rowMls['SOG'],
                    rowMls['SC%'],
                    rowMls['FS'],
                    rowMls['FC'],
                    rowMls['YC'],
                    rowMls['RC'],
                    rowMls['Year']])
                newBase = np.vstack((newBase, tmp))
                added += 1
                break
    print('Index:', i, '- Added:', added)

np.savetxt("./bases/processedBase.csv", newBase, fmt="%s", delimiter=",")
print("Done")