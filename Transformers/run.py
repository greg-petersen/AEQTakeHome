from Transformers.transformer import Transformer


def make_and_sort_list(faction, transformers):
    faction_key = faction_type(faction)
    list_of_transformers_of_faction = list(filter(lambda x: x.allegiance == faction_key, transformers))
    list_of_transformers_of_faction.sort(key=lambda transformer: transformer.rank, reverse=True)
    return list_of_transformers_of_faction


def faction_type(faction):
    if faction == 'autobots':
        return 'A'
    elif faction == 'decepticons':
        return 'D'


def do_battle(autobots, decepticons):
    autobot_victories = 0
    decepticon_victories = 0
    index = 0
    while index < len(autobots) and index < len(decepticons):
        transformer_a = autobots[index]
        transformer_b = decepticons[index]

        result = transformer_a.fight(transformer_b)
        if result == 'NO ONE':
            # BIG PROBLEMS
            print('Optiumus Prime/Predaking verse Optimus Prime/Predaking. GAME OVER. Everyone dies.')
            # Set all transformers to dead.
            break
        elif result != 'Tie':
            if type(result) == Transformer:
                if result.allegiance == 'D':
                    decepticon_victories += 1
                else:
                    autobot_victories += 1
        index += 1

    if index == 1:
        print('1 battle')
    elif index > 1:
        print('%s battles' % index)

    if autobot_victories > decepticon_victories:
        print(make_string_of_winning_team(autobots, 'Autobots'))
        print(make_string_of_losing_team_survivors(decepticons, 'Decepticons'))
    elif decepticon_victories > autobot_victories:
        print(make_string_of_winning_team(decepticons, 'Decepticons'))
        print(make_string_of_losing_team_survivors(autobots, 'Autobots'))
    elif autobot_victories == decepticon_victories:
        print('The Autobots and Decepticons Tied overall.')


def make_string_of_winning_team(team_list, team):
    winning_team_string = 'Winning team(' + team + '): '
    winning_team_string += ''.join(member.name for member in team_list)
    return winning_team_string


def make_string_of_losing_team_survivors(team_list, team):
    survivors = 'Survivors from the losing team (' + team + '): '

    for member in team_list:
        if member.alive:
            survivors += '%s ' % member.name

    return survivors


def main():
    """Main function that is ran when file is called from command line."""
    list_of_input_transformers = [
        Transformer('Soundwave', 'D', 8, 9, 1, 5, 6, 5, 6, 10),
        Transformer('Bluestreak', 'A', 6, 6, 7, 9, 5, 2, 9, 7),
        Transformer('Hubcap', 'A', 4, 4, 4, 4, 4, 4, 4, 4)
    ]

    autobots = make_and_sort_list('autobots', list_of_input_transformers)
    decepticons = make_and_sort_list('decepticons', list_of_input_transformers)

    do_battle(autobots, decepticons)


if __name__ == '__main__':
    main()
