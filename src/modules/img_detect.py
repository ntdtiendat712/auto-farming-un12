from collections import namedtuple

class ImgDetect:
  def processing():
    has_champion=False
    has_sanctum=False
    has_target=False
    has_mini_map=False
    enhance_skill_available=False
    explore_map_successfully=False
    
    ImgInfo = namedtuple("ImgInfo", ["has_champion", "has_sanctum","has_target","has_mini_map","enhance_skill_available","explore_map_successfully"])

    return ImgInfo(has_champion= has_champion,has_sanctum = has_sanctum,has_target=has_target,has_mini_map=has_mini_map,enhance_skill_available=enhance_skill_available,explore_map_successfully=explore_map_successfully)

