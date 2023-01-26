from pathlib import Path

class GameStats:
    '''Track statistics for Alien Invasion.'''

    def __init__(self, ai_game):
        '''Initializing statistics.'''
        self.settings = ai_game.settings
        self.path = Path('.highscore')

        self.reset_stats()
        self.read_score()
        
        # Start the game in an Inactive state
        self.game_active = False

    def reset_stats(self):
        '''Initialize statistics that can change during the game.'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_score(self):
        '''Save high score to a text file.'''
        with open(self.path, 'wt') as out_file:
            out_file.write(str(self.high_score))

    def read_score(self):
        '''Open saved high scores'''
        try:
            with open(self.path, 'rt') as in_file:
                saved_score = in_file.readline()
                self.high_score = int(saved_score)
        except IOError:
            print('No score file found')
            self.high_score = 0
