
def get_hit_chance (monster_dodge,player_accuracy,skill_mpcost):
    hit_chance = 100 - (monster_dodge - player_accuracy)/3 + skill_mpcost/10
    message = ""
    if (hit_chance<0):
        message = "You will always :red[miss] / :red[graze] sad 😭"
        return 0,message
    if(hit_chance>100):
        message = "Wow op 💪 accuracy, :green[it exceeds 100], but you know it cap at 100 so..."
        return 100,message
    return hit_chance,message

def get_doable_boss_dodge(player_accuracy,skill_mpcost=0, hit_chance_wanted = 0.75, monster_dodge_debuff = 0.0):
    doable_boss_dodge = -3 * ( hit_chance_wanted * 100 - skill_mpcost/10 -100 ) + player_accuracy
    
    return doable_boss_dodge / (1 - monster_dodge_debuff)

# def get_required_acc(monster_dodge,skill_mpcost=0, hit_chance_wanted = 0.75, monster_dodge_debuff = 0.0):
#     doable_boss_dodge = -3 * ( hit_chance_wanted * 100 - skill_mpcost/10 -100 ) + player_accuracy
    
#     return doable_boss_dodge / (1 - monster_dodge_debuff)

