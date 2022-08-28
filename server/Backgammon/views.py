import random
from django.shortcuts import render
from Backgammon.src.constants import CLUSTERS, TILES_BY_CLUSTER, SLOTS_BY_TILE

# Create your views here.

def board(request):
  context_dict = {}
  context_dict["clusters"]                = CLUSTERS
  context_dict["clusters_range"]          = range(1, CLUSTERS + 1)
  context_dict["tiles_by_cluster"]        = TILES_BY_CLUSTER
  context_dict["tiles_by_cluster_range"]  = range(1, TILES_BY_CLUSTER + 1)
  context_dict["slots_by_tile"]           = SLOTS_BY_TILE
  context_dict["slots_by_tile_range"]     = range(1, SLOTS_BY_TILE + 1)
  context_dict["black_pawn_slot_list"]    = [3, 6, 8]
  context_dict["black_pawn_number_list"]  = [1, 2, 4]
  context_dict["grey_pawn_slot_list"]     = [2, 10, 20]
  context_dict["grey_pawn_number_list"]   = [3, 1, 6]
  context_dict["not_empty_slot_list"]     = list(context_dict["black_pawn_slot_list"])
  context_dict["not_empty_slot_list"].extend(context_dict["grey_pawn_slot_list"])
  context_dict["clicked"]                 = "TST"
  if (request.method == "POST"):
    if (request.POST.get("roll") != None):
      context_dict["dice_list"]           = [random.randrange(1,7), random.randrange(1,7)]
    if (request.POST.get("dice_0") != None):
      context_dict["dice_list"]           = [0, random.randrange(1,7)]
    for i in range(CLUSTERS*TILES_BY_CLUSTER):
      if (request.POST.get(f"slot_{i}") != None):
        context_dict["clicked"]           = i
  else:
    context_dict["dice_list"]             = [7, 7]
  return render(request, "Backgammon/board.html", context=context_dict)