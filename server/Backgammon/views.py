from django.shortcuts import render
from Backgammon.src.constants import CLUSTERS, TILES_BY_CLUSTER, SLOTS_BY_TILE

# Create your views here.

def board(request):
  context_dict = {}
  context_dict["clusters"]               = CLUSTERS
  context_dict["clusters_range"]         = range(1, CLUSTERS + 1)
  context_dict["tiles_by_cluster"]       = TILES_BY_CLUSTER
  context_dict["tiles_by_cluster_range"] = range(1, TILES_BY_CLUSTER + 1)
  context_dict["slots_by_tile"]          = SLOTS_BY_TILE
  context_dict["slots_by_tile_range"]    = range(1, SLOTS_BY_TILE + 1)
  return render(request, "Backgammon/board.html", context=context_dict)