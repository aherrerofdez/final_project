class Back(object):
    def __init__(self):
        pass

    def get_instructions(self):
        instructions = '1. Choosing a Mode: \n     - User Mode: if you want to play the game. \n     - Computer Mode:' \
                       ' if you want to watch our AI play. \n \n 2. Choosing a Difficulty Level: \n You can choose ' \
                       'any level among Easy, Medium and Difficult. \n \n 3. Click on "PLAY" to start playing. You ' \
                       'can use the arrows in your keyboard or the ones in the screen. \n \n 4. Click on "EXIT" if ' \
                       'you want to close the game.'
        return instructions

    def get_track(self, index):
        # Default Mode: Medium
        length = 2
        speed = 2
        if index == 0:
            # Easy Mode
            length = 1
            speed = 1
        if index == 2:
            # Difficulty Mode
            length = 4
            speed = 4
