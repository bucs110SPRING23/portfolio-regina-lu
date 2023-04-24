class Player:
  def __init__(self, pnum=1):
    """
    Initialize the player object
    args: pnum [int] the player's id number
    """
    self.player_num = pnum
    self.lives = 3 # players always start with 3 lives
    self.is_large = False # player always starts small

class mysterybox:
  def __init__(self):
    ""
    self.height = (x, y)
    self.ismystery = True

class text:
  def __init__(self):
    ""
    self.font = 
    self.color = 
    self.location = (x, y)

class pipes:
  def __init__(self):
    ""
    self.location = (x, y)
    