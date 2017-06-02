from Transformers.transformer import Transformer


def make_and_sort_list(faction, transformers):
    faction_key = faction_type(faction)
    list_of_transformers_of_faction = list(filter(lambda x: x.allegiance == faction_key, transformers))
    list_of_transformers_of_faction.sort(key=lambda transformer: transformer.rank)
    return list_of_transformers_of_faction


def faction_type(faction):
    if faction == 'autobots':
        return 'A'
    elif faction == 'decepticons':
        return 'D'


def do_battle(team_one, team_two):
    # Sorted Lists.
    print('Did battle.')


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

    # print('List of Autobots')
    # for transformer in autobots:
    #     print(vars(transformer))
    #
    # print('List of Decepticons')
    # for transformer in decepticons:
    #     print(vars(transformer))
    #
    # test = list_of_input_transformers[0].fight(list_of_input_transformers[1])
    # print('Winner: %s' % test.name)


if __name__ == '__main__':
    main()
