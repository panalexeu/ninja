def map_init(file_name):
    with open(f'game_files/maps/{file_name}.txt') as file:
        return [line.rstrip() for line in file]
