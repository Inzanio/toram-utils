
from toram_utils.stat_calculations import Build

class SkillTypes :
	ACTIVE = "Active"
	PASSIVE = "Passive"
	ATTACKING = "Attacking"


class Skill : 
	def __init__(self, name : str, type : list, level:int, build : Build ):
		self.name = name
		self.type = type
		self.level = level
		self.mp_cost = 0
		self.build_meet_weapon_condition= True
		self.tree_level = 1
		self.ailment = None
		#self.effects = effects
		self.build = build
		self.hasSpecialEffect = False
		self.description = ""
		self.passive_description = ""
		self.active_description = ""
		self.dps_description = ""
		self.active = False
  
		self.hasSpecialAttribute = False
		
		
	@property
	def dps_stats(self):
		return {}
	@property
	def passive_stats(self):
		return {}
	@property
	def active_stats(self):
		return {}
	
	@property
	def constant(self):
		return 0
	@property
	def multi(self):
		return 0
	
	@property
	def damage(self):
		return None


