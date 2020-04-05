class Back(object):
    def __init__(self):
        pass

    @staticmethod
    def get_instructions():
        instructions = '1. Choosing a Mode: \n     - User Mode: if you want to play the game. \n     - Computer Mode:' \
                       ' if you want to watch our AI play. \n \n 2. Choosing a Difficulty Level: \n You can choose ' \
                       'any level among Easy, Medium and Difficult. \n \n 3. Click on "PLAY" to start playing. You ' \
                       'can use the arrows in your keyboard or the ones in the screen. \n \n 4. Click on "EXIT" if ' \
                       'you want to close the game.'
        return instructions

    @staticmethod
    def get_track(index):
        # Default Mode: Medium
        length = 1.7
        speed = 50
        if index == 0:
            # Easy Mode
            length = 2.5
            speed = 75
        if index == 2:
            # Difficulty Mode
            length = 0.9
            speed = 25
        params = [speed, length]
        return params
