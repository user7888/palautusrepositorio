import requests
from player import Player
print("asdasd")

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(player_dict)
            players.append(player)

    print("Oliot:")

    for player in players:
        print(player)

# team, assists, goals
if __name__ == '__main__':
    main()
