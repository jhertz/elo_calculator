#@author: jhertz

import challonge



k = 32 #right now we use a constant K-value


player_db = {}


class player:
    name = ""
    rating = 0

    def __init__(self, name, rating=1200):
        self.name = name
        self.rating = rating

    def __str__(self):
        return "name: " + str(self.name) + " rating: " + str(self.rating)


class match:
    winner = ""
    loser = ""

    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser

    def __str__(self):
        return "winner: " + self.winner + " loser: " + self.loser



def get_player(name):
    if player_db.has_key(name):
        return player_db[name]
    else:
        player_db[name] = player(name)
        return player_db[name]


def print_ratings():
    players = player_db.values()
    sorted_players = sorted(players, key=lambda p: p.rating, reverse=True)
    for p in sorted_players:
        print p


def update_rating(winner, loser):
    winner_old_rating = winner.rating
    loser_old_rating = loser.rating
    s = 1 # "score"
    adjustment =  k * (s - calc_expected(winner_old_rating, loser_old_rating))
    winner.rating += adjustment
    loser.rating -= adjustment


def calc_expected(a, b):
    return 1.0 / (1 + 10**((b - a) / 400) )


def init_challonge(username, api_key):
    challonge.set_credentials(username, api_key)

def get_tournament(id):
    return challonge.tournaments.show(id)

def get_participants(id):
    return challonge.participants.index(id)

def get_matches(id):
    return challonge.matches.index(id)

def harvest_matches(id):
    participants = get_participants(id)
    matches = get_matches(id)
    ids_to_names = {}
    for p in participants:
        ids_to_names[p['id']] = p['name']
    toReturn = []
    for m in matches:
        winner = ids_to_names[m['winner-id']]
        loser = ids_to_names[m['loser-id']]
        toReturn.append(match(winner, loser))
    return toReturn

def update_elos_from_matches(matches):
    for match in matches:
       # print "about to process a match::"
        winner = get_player(match.winner)
       # print "winner: " , winner
        loser = get_player(match.loser)
       # print "loser: " , loser
        update_rating(winner, loser)





if __name__ == "__main__":
    api_key = ""
    username = ""
    brackets = []

    with open("brackets.txt") as bracket_file:
        for line in bracket_file:
            brackets.append(line.rstrip())

    if not brackets:
        print "failed to read brackets, exiting"
        exit(-3)

    with open("creds.txt") as creds_file:
        username = creds_file.readline().rstrip()
        api_key = creds_file.readline().rstrip()


    if not api_key:
        print "failed to read api key, exiting"
        exit(-1)

    if not username:
        print "failed to read username, exiting"
        exit(-2)



    init_challonge(username, api_key)
    for bracket_id in brackets:
        #print "about to do bracket:" , bracket_id , "\n"
        matches = harvest_matches(bracket_id)
        update_elos_from_matches(matches)
        #print_ratings()

   # print "done, printing final ratings \n"
    print_ratings()
  #  print "exiting"
#test
