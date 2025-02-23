
from .skills import SkillTypes , Skill
from toram_utils.stat_calculations import Build
from math import floor
from toram_utils.equipment import EquipmentType

# ADD all blade skills
# Done
# - passive : Sword mastery,quick slash, sword techniques, 
# - buff : war cry, berzerk , gladiate
# - active : astute, buster blade, aura blade
# 
# TODO : 
# - buff : rampage
# - active : Meteor Breaker, Lunar Slash, Shut out
# - active : spiral air, sonic blade, sword tempest, tiger slash


# ---------------------------------- BLADE SKILLS ---------------------------------#
class BladeSkill:
	tree = "Blade Skills"
	def __init__(self):
		pass

class SwordMastery(Skill,BladeSkill):
	name = "Sword Mastery" 
	type = [SkillTypes.PASSIVE]
	
	def __init__(self, level, build :Build):
		super().__init__(self.name, self.type,level, build)
		self.build_meet_weapon_condition = self.build.main_weapon and self.build.main_weapon.type in ["OHS","THS"]
	@property
	def passive_stats(self):
		if (self.build_meet_weapon_condition):
			return {
				"ATK %":1 if self.level <3 else 2 if self.level <8 else 3 ,
				"Weapon ATK %": 3*self.level
			}
		
		return {}

class QuickSlash(Skill,BladeSkill):
	name = "Quick Slash"
	type = [SkillTypes.PASSIVE]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type, level, build)
		self.build_meet_weapon_condition = self.build.main_weapon and self.build.main_weapon.type in ["OHS","THS"]
  
	@property
	def passive_stats(self):
		if (self.build_meet_weapon_condition):
			return {
				"ASPD":10*self.level,
				"ASPD %": self.level
			}
		return {}
	#def passive(self,build):

class SwordTechniques(Skill,BladeSkill):
	name = "Sword Techniques"
	type = [SkillTypes.PASSIVE]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type , level, build)
		self.build_meet_weapon_condition = self.build.main_weapon and self.build.main_weapon.type in ["OHS","THS"]
		self.hasSpecialEffect = True
		self.passive_description = f"Increases the damage of Blade Skills by {(2 * self.level)}%"
	 
class WarCry(Skill,BladeSkill):
	name = "War Cry"
	type = [SkillTypes.ACTIVE]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type, level, build)
		self.mp_cost = 300
	@property
	def active_stats(self):
		if (self.build.main_weapon and self.build.main_weapon.type == "THS"):
			return {
				"ATK %": 5 + self.level
			}
		return {
			"ATK %": self.level
		}

class Berserk(Skill,BladeSkill):
	name = "Berserk"
	type = [SkillTypes.ACTIVE]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type, level, build)
		self.mp_cost = 500
	@property
	def active_stats(self):
		stats = {
				"ASPD %":  10*self.level,
				"ASPD":  100*self.level,
				"Critical Rate":  floor(2.5*self.level),
				"Stability %": - floor(( 100 - 5*self.level)),
				"DEF %": -(100-self.level),
				"MDEF %": -(100-self.level)
			}
		
		if self.build.main_weapon :
			if (self.build.main_weapon.type in ["OHS","THS"]):
				stats["Stability %"] = - floor(( 100 - 5*self.level)/2)

			if (self.build.main_weapon.type == "OHS" and ( self.build.sub_weapon and self.build.sub_weapon.type != "OHS")):
				stats["DEF %"] = -floor((100-self.level)/2)
				stats["MDEF %"] = -floor((100-self.level)/2)
			if (self.build.main_weapon.type == "THS"):
				stats["Critical Rate"] = 5*self.level
		
		return stats

class Gladiate(Skill,BladeSkill):
	name = "Gladiate"
	type = [SkillTypes.ACTIVE]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type, level, build)
		self.build_meet_weapon_condition = self.build.main_weapon and self.build.main_weapon.type in ["OHS","THS"]
		self.hasSpecialEffect = True
		description = f"You need OHS or THS or Dual Sword to use This bro" 
		if self.build.main_weapon :
			if ( self.build.main_weapon.type == "THS" or (self.build.sub_weapon.type == "OHS" and self.build.main_weapon.type=="OHS") ):
				description = f"Reduce any damage received by {2*self.level}%"
			if self.build.main_weapon.type == "OHS" :
				description = f"Reduce any damage received by {self.level}%"
		self.active_description = description    
	
class Astute(Skill,BladeSkill):
	
	name = "Astute"
	type = [SkillTypes.ACTIVE,SkillTypes.ATTACKING]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type, level, build)
		self.build_meet_weapon_condition = self.build.main_weapon and self.build.main_weapon.type in ["OHS","THS"]
		self.mp_cost = 100
		self.max_range = self.build.main_weapon.max_range
	@property
	def active_stats(self):
		if (self.build_meet_weapon_condition):
			return {
				"Critical Rate":50 if self.build.main_weapon.type == "THS" else 25
			}
		else :
			return {}
	
	@property
	def constant(self):
		if (self.build_meet_weapon_condition):
			return 150 + 5*self.level
		else:
			return 0
	@property
	def multi(self):
		if (self.build_meet_weapon_condition):
			return 1.5 + 0.1*self.level + 0.5 if self.build.main_weapon.type == "THS" else 0
		else :
			return 0
	
class BusterBlade(Skill,BladeSkill):
	name = "Buster Blade"
	type = [SkillTypes.ACTIVE,SkillTypes.ATTACKING]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type, level, build)
		self.build_meet_weapon_condition = self.build.main_weapon and self.build.main_weapon.type in ["OHS","THS"]
		self.max_range = 7
	@property
	def active_stats(self):
		stats = {
			"Weapon ATK %": self.level
		}
		if self.build.main_weapon:
			if self.build.main_weapon.type == EquipmentType.OHS and self.build.sub_weapon.type == EquipmentType.SHIELD :
				stats["Weapon ATK %"] = self.level + self.build.sub_weapon.refine

		return stats
	@property
	def constant(self):
		return 30*self.level
	@property
	def multi(self):
		multi = 0.75 * self.level
		if self.build.main_weapon : 
			if self.build.main_weapon.type == EquipmentType.OHS :
				multi+=  self.build.baseDEX/200
				auraBlade = next((skill for skill in self.build.passive_skills if skill.name == AuraBlade.name), None)
				if (auraBlade):
					multi += (0.2 * auraBlade.level) + self.build.baseDEX/200
			elif self.build.main_weapon.type == EquipmentType.THS :
				multi+=  self.build.baseSTR/200 
		return multi

class AuraBlade(Skill,BladeSkill):
	name = "Aura Blade"
	type = [SkillTypes.PASSIVE,SkillTypes.ACTIVE,SkillTypes.ATTACKING]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type, level, build)
		self.mp_cost = 200
		self.build_meet_weapon_condition = self.build.main_weapon and self.build.main_weapon.type in ["OHS","THS"]
		self.hasSpecialEffect = True
		description = "Need OHS or THS bro"
		if (self.build.main_weapon):
			if self.build.main_weapon.type == EquipmentType.THS :
				description = "Increase next skill damage by 1.3x"
			elif self.build.main_weapon.type == EquipmentType.OHS :
				if (self.build.sub_weapon and self.build.sub_weapon.type == "OHS"):
					description = "Increase next skill damage by 1.1x"
				else :
					description = "Increase all skill damage by 1.2x"
		self.active_description = description
  
		if (self.build.main_weapon.type == EquipmentType.OHS ):
			if (self.build.sub_weapon and self.build.sub_weapon.type == "OHS"):
				self.passive_description = f""
			else :
				self.passive_description = f"Increase the power of :blue[{BusterBlade.name}]"
		self.hasSpecialAttribute = True
		self.specialAttribute = {
			"Critical Rate":9999999
		}
		self.dps_description = "The skill :blue[will always deal a Critical Hit]"
	@property
	def active_stats(self):
		# if not self.build_meet_weapon_condition :
		# 	return {}
		stats = {
			"Additional Melee %": 10*self.level
		}
		return stats
	@property
	def constant(self):
		return 30*self.level
	@property
	def multi(self):
		return 5 + self.level

class MeteorBreaker(Skill,BladeSkill):
	name = "Meteor Breaker"
	type = [SkillTypes.ATTACKING]
	
	def __init__(self, level, build : Build):
		super().__init__(self.name,self.type, level, build)
		self.build_meet_weapon_condition = self.build.main_weapon and self.build.main_weapon.type in ["OHS","THS"]
		self.max_range = self.build.main_weapon.max_range
	@property
	def constant(self):
		return 400+20*self.level
	@property
	def multi(self):
		multi = 0.75 * self.level
		if self.build.main_weapon : 
			if self.build.main_weapon.type == EquipmentType.OHS :
				multi+=  self.build.baseDEX/200
				auraBlade = next((skill for skill in self.build.passive_skills if skill.name == AuraBlade.name), None)
				if (auraBlade):
					multi += (0.2 * auraBlade.level) + self.build.baseDEX/200
			elif self.build.main_weapon.type == EquipmentType.THS :
				multi+=  self.build.baseSTR/200 
		return multi

BLADE_SKILLS = [SwordMastery,QuickSlash,SwordTechniques,WarCry,Berserk,Gladiate,Astute,BusterBlade,AuraBlade] #+ DPS_SKILL_BLADE_SKILLS      

