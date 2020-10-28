# The decompilers to use
# This is in order from first attempt to last attempt
# After some testing from ssinakhot, it was determined this order is the best
# Only these 3 decompilers are currently supported
decompilers = ['unpyc3', 'decompyle3', 'uncompyle6']

gameplay_folder_data = os.path.join(game_folder, 'Data', 'Simulation', 'Gameplay')
gameplay_folder_game = os.path.join(game_folder, 'Game', 'Bin', 'Python')

decompile_folders = [gameplay_folder_data, gameplay_folder_game]
