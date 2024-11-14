from . import ImgDetect, Actions

game_state = {
  "base":"base",
  "dungeon":"dungeon",
}

class GameEngine:
  def __init__(self, state="base", met_champion=False,sct=None):
    self.state = state
    self.met_champion = met_champion
    self.sct = sct

  def return_to_base(self):
    self.state = "base"
    return
  def move_to_battlefield(self):
    self.state = "dungeon"
    return
  def go_to_escort_point(self):
    return
  def action(self):
    has_champion,has_sanctum,has_target,has_mini_map,enhance_skill_available, explore_map_successfully = ImgDetect.processing(self.sct)
    if enhance_skill_available:
      Actions.use_enhance_skill()
    if has_sanctum:
      Actions.get_sanctum_buff()
    if self.met_champion:
      if not has_champion:
        self.return_to_base()
      else:
        Actions.move_to_champion()
      return
    
    if explore_map_successfully:
      self.return_to_base()
      return


    Actions.explore_map()

    return
    