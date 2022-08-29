import random
import copy

class Board:

  def __init__(self, dic=None):
    if (dic == None):
      self._state           = "INIT"  # Possible values : INIT / BLACK_TURN / GREY_TURN / DONE
      self._black_pawn_list = [(1, 2), (12, 5), (17, 3), (19, 5)] # (position, stack_size) Black must reach the tile 25 by increasing
      self._grey_pawn_list  = [(24, 2), (13, 5), (8, 3), (6, 5)]  # (position, stack_size) Grey must reach the tile 0 by decreasing
      self._dice_list       = [(0, 0), (0, 0)]  # (value, available loads)
      self._dice_clicked    = None
    else:
      # WARNING : Check on dic key must be done here
      self._state           = dic["state"]
      self._black_pawn_list = copy.deepcopy(dic["black_pawn_list"])
      self._grey_pawn_list  = copy.deepcopy(dic["grey_pawn_list"])
      self._dice_list       = copy.deepcopy(dic["dice_list"])
      self._dice_clicked    = dic["dice_clicked"]

  @property
  def state(self):
    return self._state

  @property
  def black_pawn_list(self):
    return copy.deepcopy(self._black_pawn_list)

  @property
  def grey_pawn_list(self):
    return copy.deepcopy(self._grey_pawn_list)

  @property
  def dice_list(self):
    return copy.deepcopy(self._dice_list)

  def toDict(self):
    dic = {}
    dic["state"]            = self._state
    dic["black_pawn_list"]  = copy.deepcopy(self._black_pawn_list)
    dic["grey_pawn_list"]   = copy.deepcopy(self._grey_pawn_list)
    dic["dice_list"]        = copy.deepcopy(self._dice_list)
    dic["dice_clicked"]     = self._dice_clicked
    return dic

  def roll_dice(self, double_en=True):
    while True:
      for diceIdx in range(len(self._dice_list)):
        self._dice_list[diceIdx][0] = random.randrange(1,7)
      if (self._dice_list[0][0] == self._dice_list[1][0]):
        for diceIdx in range(len(self._dice_list)):
          self._dice_list[diceIdx][1] = 2
      else:
        for diceIdx in range(len(self._dice_list)):
          self._dice_list[diceIdx][1] = 1
      if (double_en or (self._dice_list[0][0] != self._dice_list[1][0])):
        break

  def init_1_player(self):
    self._state = "BLACK_TURN"

  def dice_click(self, dice_id):
    # WARNING : Check if dice_id exists, dice_clicked empty, your turn, dice has loads
    self._dice_clicked = dice_id

  def pawn_click(self, tile):
    # WARNING : Check if tile exists, dice_clicked, arrival tile empty
    if (self._state == "BLACK_TURN"):
      pass
    elif (self._state == "GREY_TURN"):
      pass