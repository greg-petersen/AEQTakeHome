from Transformers.transformer import Transformer


def make_and_sort_list(faction, transformers):
    """Receives the faction and a list of transformers to filter and sort into a list based on their allegiance."""
    faction_key = faction_type(faction)
    list_of_transformers_of_faction = list(filter(lambda x: x.allegiance == faction_key, transformers))
    list_of_transformers_of_faction.sort(key=lambda transformer: transformer.rank, reverse=True)
    return list_of_transformers_of_faction


def faction_type(faction):
    """Determines single character representation of faction."""
    if faction == 'autobots':
        return 'A'
    elif faction == 'decepticons':
        return 'D'


def do_battle(autobots, decepticons):
    """Determines the winning faction between the autobots and decepticons and outputs the battle stats."""
    autobot_victories = 0
    decepticon_victories = 0
    index = 0
    while index < len(autobots) and index < len(decepticons):
        transformer_a = autobots[index]
        transformer_b = decepticons[index]

        result = transformer_a.fight(transformer_b)
        if result == 'Optoking':
            print('Optiumus Prime/Predaking verse Optimus Prime/Predaking. GAME OVER. Everyone dies.')
            decepticon_victories = 0
            autobot_victories = 0
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
    else:
        print('The Autobots and Decepticons tied overall.')


def make_string_of_winning_team(team_list, team):
    """Returns the string of the winning team members."""
    winning_team_string = 'Winning team(' + team + '): '
    winning_team_string += ' '.join(member.name for member in team_list)
    return winning_team_string


def make_string_of_losing_team_survivors(team_list, team):
    """Returns the string of the survivors in the received team_list."""
    survivors = 'Survivors from the losing team(' + team + '): '

    for idx, member in enumerate(team_list):
        if member.alive:
            survivors += '%s ' % member.name

    return survivors


def main():
    """Main function that is ran when file is called from command line."""
    list_of_input_transformers = [
        Transformer('Soundwave', 'D', 8, 9, 1, 5, 6, 5, 6, 10),
        # Transformer('Starscream', 'D', 7, 9, 10, 7, 9, 9, 8, 8),
        Transformer('Bluestreak', 'A', 6, 6, 7, 9, 5, 2, 9, 7),
        Transformer('Hubcap', 'A', 4, 4, 4, 4, 4, 4, 4, 4)
        # Transformer('Optimus Prime', 'A', 10, 10, 8, 10, 10, 10, 8, 10),
        # Transformer('Ratchet', 'A', 4, 8, 4, 5, 7, 8, 3, 10)
    ]

    autobots = make_and_sort_list('autobots', list_of_input_transformers)
    decepticons = make_and_sort_list('decepticons', list_of_input_transformers)
    do_battle(autobots, decepticons)


if __name__ == '__main__':
    main()
