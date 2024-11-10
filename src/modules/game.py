from img_detect import ImgDetect
from actions import Actions

game_state = {
  "base":"base",
  "dungeon":"dungeon",
}

class GameEngine:
  def __init__(self, state="base", met_champion=False):
    self.state = state
    self.met_champion = met_champion
  def return_to_base(self):
    self.state = "base"
    return
  def move_to_battlefield(self):
    self.state = "dungeon"
    return
  def go_to_escort_point(self):
    return
  def action(self):
    has_champion,has_sanctum,has_target,has_mini_map,enhance_skill_available, explore_map_successfully = ImgDetect.processing()
    if ImgDetect.enhance_skill_available():
      Actions.use_enhance_skill()
    if ImgDetect.has_sanctum():
      Actions.get_sanctum_buff()
    if self.met_champion:
      if not ImgDetect.has_champion():
        self.return_to_base()
      else:
        Actions.move_to_champion()
      return
    
    if ImgDetect.explore_map_successfully():
      self.return_to_base()
      return


    Actions.explore_map()

    return
    