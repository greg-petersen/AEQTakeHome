"""castle.py has two functions. calculate_number_of_castles and a main function."""
import random


def calculate_number_of_castles(land):
    """Returns number of castles that can be built on input land array."""
    print(land)
    direction = 0  # 0 represents start, 1 means up, -1 means down
    previous_plot = None
    castles = 0

    for index, plot in enumerate(land):
        output_string = 'Index: %s Value: %s' % (index, plot)

        if index > 0:
            if plot > previous_plot and direction != 1:
                direction = 1
                castles += 1
                output_string += ' Castles: %s - Preceding Valley Found' % castles
            elif plot < previous_plot and direction != -1:
                direction = -1
                castles += 1
                output_string += ' Castles: %s - Preceding Peak Found' % castles
            else:
                output_string += ' Castles: %s' % castles
        else:
            output_string += ' Castles: %s' % castles
        previous_plot = plot
        print(output_string)

    return castles


def main():
    """Main function that is ran when file is called from command line."""
    land_array = [random.randrange(1, 10, 1) for _ in range(20)]
    # land_array = [9,8,6,3,6,1,1,9,3,9] Use this if you want to pass a predetermined array.

    number_of_castles = calculate_number_of_castles(land_array)
    print('Number of Castles: %s' % number_of_castles)


if __name__ == '__main__':
    main()
