import random
import copy
from django.shortcuts import render
from Backgammon.src.constants import CLUSTERS, TILES_BY_CLUSTER, SLOTS_BY_TILE
from Backgammon.src.Board import Board

# WARNING : using session to store board will not be functionnal online
def board(request):
  # Init page
  if (request.POST.get("pseudo") != None):
    request.session['pseudo'] = request.POST.get("pseudo")
    board = Board()
  else:
    board = Board(dic=request.session['board'])

  # Getting player input
  if (request.method == "POST"):
    if (request.POST.get("roll") != None):
      board.roll_dice()
    if (request.POST.get("one_player") != None):
      board.init_1_player()
    #if (request.POST.get("dice_0") != None):
    #  context_dict["dice_list"]           = [0, random.randrange(1,7)]
    #for i in range(CLUSTERS*TILES_BY_CLUSTER):
    #  if (request.POST.get(f"slot_{i}") != None):
    #    context_dict["clicked"]           = i

  # Processing
  request.session['board'] = board.toDict()

  # Filling context
  context_dict = {}
  context_dict["clusters"]                = CLUSTERS
  context_dict["clusters_range"]          = range(1, CLUSTERS + 1)
  context_dict["tiles_by_cluster"]        = TILES_BY_CLUSTER
  context_dict["tiles_by_cluster_range"]  = range(1, TILES_BY_CLUSTER + 1)
  context_dict["slots_by_tile"]           = SLOTS_BY_TILE
  context_dict["slots_by_tile_range"]     = range(1, SLOTS_BY_TILE + 1)
  context_dict["black_pawn_list"]         = board.black_pawn_list
  context_dict["grey_pawn_list"]          = board.grey_pawn_list
  context_dict["not_empty_list"]          = [e[0] for e in board.black_pawn_list]
  context_dict["not_empty_list"].extend([e[0] for e in board.grey_pawn_list])
  context_dict["pseudo"]                  = request.session.get('pseudo')
  context_dict["state"]                   = board.state
  context_dict["dice_list"]               = copy.deepcopy(board.dice_list)

  return render(request, "Backgammon/board.html", context=context_dict)