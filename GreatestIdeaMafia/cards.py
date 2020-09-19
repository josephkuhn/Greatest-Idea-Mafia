class Card:
    def __init__(self):
        self
    abilityDesc = {
        "Vanilla": "",
        "Goon": "",
        "Roleblocker": "Roleblocker: During the Night, you may PM me the name of another player. This player will be unable to use his/her ability (if he/she has one).\n",
        "Godfather": "Godfather: You will investigate as \"Not Guilty\" if investigated by a Cop.\n",
        "Tracker": "Tracker: During the Night, you may PM me the name of another player. You will be informed of the name of anyone that player targeted during that Night.\n",
        "Doctor": "Doctor: During the Night, you may PM me the name of another player. This player will be protected from all nightkills for that Night.\n",
        "Lover": "Lover: If there are other Lovers in the game, you will form a Lover bond with them. All Lovers will die at the same time.\n",
        "Seer": "Seer: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is aligned with the Werewolves. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not aligned with the Werewolves. You will receive \"No result\" if your investigation failed.\n",
        "Day Vigilante": "Day Vigilante: During the Day, you may post \"Kill: NAME\". This player will immediately die.\n",
        "Governor": "Governor: During the Day, you may post \"Govern NAME\" in bold. That player will be unable to be eliminated that day.\n",
        "Strongman": "Strongman: You have the ability to bypass any protective/roleblock abilities when you perform the factional kill.\n",
        "Reflexive Doctor": "Reflexive Doctor: If you are targeted at night, any and every player who targets you will be protected from all nightkills that night.\n",
        "Hirsute": "Hirsute: You will investigate as \"GUILTY\" to Seers.\n",
        "Cupid": "Cupid: During Night 1, you may PM me the name of another player. Every player that targets this player (except you) will become Lovers with them.\n",
        "Alpha": "Alpha: You will investigate as \"Not Guilty\" if investigated by a Seer.\n",
        "Hider": "Hider: During the Night, you may PM me the name of another player. You will \"hide\" behind that player, making you immune to any actions that target you. However, if you hide behind a non-Town-aligned player, you will die.\n",
        "Fruit Vendor": "Fruit Vendor: During the Night, you may PM me the name of another player. They will be told that they received fruit.\n",
        "Bulletproof": "Bulletproof: You cannot be nightkilled.\n",
        "Cop": "Cop: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is aligned with the Mafia. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not aligned with the Mafia. You will receive \"No result\" if your investigation failed.\n",
        "Mason": "Mason: If there are other Masons in the game, you will form a Mason group with them. There will be a Mason PM that can be used pre-game and during the Night.\n",
        "Watcher": "Watcher: During the Night, you may PM me the name of another player. You will be informed of the name of anyone who targeted that person during that Night.\n",
        "FBI Agent": "FBI Agent: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is a Serial Killer. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not a Serial Killer. You will receive \"No result\" if your investigation failed.\n",
        "Ninja": "Ninja: You will not appear on any Watcher or Tracker reports.\n",
        "Paranoid Gun Owner": "Paranoid Gun Owner: Every player that targets you will die.\n",
        "Miller": "Miller: You will investigate as \"GUILTY\" to Cops.\n",
        "Supersaint": "Supersaint: If you are eliminated, whomever placed the hammer vote will also die.\n",
        "Gravedigger": "Gravedigger: You will show up as targeting all nightkilled players to Trackers and Watchers during the Night of said players' deaths.\n",
        "Parrot": "Parrot: During the Night, you may PM me the name of another player. If that player has an active ability, you will use that ability on that player.\n",
        "Prince": "Prince: If you are eliminated, you will not die.\n",
        "Prober": "Prober: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be WEREWOLF\" if that player is aligned with the Werewolves. You will receive \"You believe NAME to be NOT WEREWOLF\" if that player is not aligned with the Werewolves. You will receive \"No result\" if your investigation failed. Your target will also be roleblocked.\n",
        "Vanillaiser": "Vanillaiser: During the Night, you may PM me the name of another player. This player will lose any abilities they have (not counting factional abilities). This will take effect at the start of the next Day.\n",
        "Silencer": "Silencer: During the Night, you may PM me the name of another player. This player will not be able to vote during the next Day phase.\n",
        "Psychotrooper": "Psychotrooper: All investigators with \"GUILTY/NOT GUILTY\" results are Insane while you are still alive.\n",
        "Mass Redirector": "Mass Redirector: During the Night, you may PM me the name of another player. All Night actions will be redirected to this player.\n",
        "Bloodsucker": "Bloodsucker: During the Night, you may PM me the name of another player. That player will turn into a Treestump (they will be unable to vote or perform actions for the rest of the game). No Alien may perform the factional nightkill on the same night that you do this.\n",
        "Sympathiser": "Sympathiser: If there are no other Aliens in the game, you will become a Vanilla Townie instead.\n",
        "Cop/Lover": "During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is aligned with the Mafia. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not aligned with the Mafia. You will receive \"No result\" if your investigation failed.\nLover: If there are other Lovers in the game, you will form a Lover bond with them. All Lovers will die at the same time.\n",
        "Jailkeeper": "Jailkeeper: During the Night, you may PM me the name of another player. This player will be unable to use his/her ability (if he/she has one). This player will also be immune to nightkills for that Night.\n",
        "Bodyguard": "Bodyguard: During the Night, you may PM me the name of another player. If this player is nightkilled, you will die instead.\n",
        "Vigilante": "Vigilante: During the Night, you may PM me the name of another player. This player will die.\n",
        "Compulsive Childkiller": "Compulsive Childkiller: If any Innocent Child is revealed, you will immediately Dayvig that player.\n",
        "Mason/Doctor": "Mason: If there are other Masons in the game, you will form a Mason group with them. There will be a Mason PM that can be used pre-game and during the Night.\nDoctor: During the Night, you may PM me the name of another player. This player will be protected from all nightkills for that Night.\n",
        "Mason/Lover": "Mason: If there are other Masons in the game, you will form a Mason group with them. There will be a Mason PM that can be used pre-game and during the Night.\nLover: If there are other Lovers in the game, you will form a Lover bond with them. All Lovers will die at the same time.\n",
        "Jack-of-all-Trades": "Jack-of-all-Trades: You may use each of the following abilities once per game. You may not use more than one ability per Night.\nRoleblocker: During the Night, you may PM me the name of another player. This player will be unable to use his/her ability (if he/she has one).\nCop: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is aligned with the Mafia. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not aligned with the Mafia. You will receive \"No result\" if your investigation failed.\nDoctor: During the Night, you may PM me the name of another player. This player will be protected from all nightkills for that Night.\n",
        "Vengeful": "Vengeful: If you are eliminated, you may choose to kill one player immediately by posting in-thread \"Kill: PLAYERNAME\". If you do not want to kill anyone, please post \"Kill: No one\".\n",
        "Retired Werewolf Hunter": "Retired Werewolf Hunter: You are immune to nightkills performed by Werewolves.\n",
        "Marine": "Retired Marine: You are immune to nightkills performed by any Serial Killers.\n",
        "Evangelistic": "Evangelistic: You will investigate as \"GUILTY\" to Cult investigators.\n",
        "Tentacled": "Tentacled: You will investigate as \"GUILTY\" to Alien investigators.\n",
        "Watchlisted": "Watchlisted: You will investigate as \"GUILTY\" to Serial Killer investigators.\n",
        "Wrong Place at the Wrong Time": "Wrong Place at the Wrong Time: You will investigate as \"GUILTY\" to all investigators.\n",
        "Black Goo": "Black Goo: Anyone who targets you will become part of the Cult faction.\n",
        "Ascetic": "Ascetic: You are immune to all Night actions except kills.\n",
        "Private Investigator": "Private Investigator: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be Cult\" if that player is aligned with the Cult faction. You will receive \"You believe NAME to not be Cult\" if that player is not aligned with the Cult. You will receive \"No result\" if your investigation failed.\n",
        "Nymphomaniac": "Nymphomaniac: During Night 1, you must PM me the name of another player. You will form a Lover bond with them (aka if you or your partner is killed, the other Lover will also die).\n",
        "Innocent Child": "Innocent Child: You can post \"I am an Innocent Child\" in bold in the thread at any time. I will then confirm that you are Town.\n",
        "Enabler": "Enabler: If you die, the player you \"enable\" (randomly selected by the mod) will be unable to use his/her abilities (not counting factional abilities).\n",
        "Tree Stump": "Tree Stump: At any time during the Day, you can post \"Treestump\" in bold. This will cause you to die and your role to be revealed but, unlike other dead players, you may continue to post. You may not vote.\n",
        "Conspiracy Theorist": "Conspiracy Theorist:\nDuring the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is aligned with the Aliens. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not aligned with the Aliens. You will receive \"No result\" if your investigation failed.\nTentacled: You will investigate as \"GUILTY\" to Alien investigators.\n",
        "Kingmaker": "Kingmaker: During the Night, you may PM me the name of another player. This player will be the \"King\" during the next Day phase, becoming the only player with a vote for that Day. They may \"execute\" someone to decide the day's lynch.\n",
        "Bloodhound": "Bloodhound: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be TOWN\" if that player is aligned with the Town. You will receive \"You believe NAME to be NOT TOWN\" if that player is not aligned with the Town. You will receive \"No result\" if your investigation failed.\n",
        "Vanilla Cop": "During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be VANILLA\" if that player is either a Vanilla Townie, Mafia Goon or basic Werewolf. You will receive \"You believe NAME to be NOT VANILLA\" otherwise. You will receive \"No result\" if your investigation failed.\n",
        "Hero": "Hero: If a King tries to execute you, they will die instead.\n",
        "Tourist": "Tourist: During the Night, you must PM me the name of another player. If you do not submit a target, it will be randomized. This has no effect.\n",
        "Nurse": "Nurse: If a Town Doctor dies, you will inherit their power.\n",
        "Commuter": "Commuter: At Night, you may \"commute\". All abilities that target you that Night will fail.\n",
        "Cop-of-all-Trades": "Cop-of-all-Trades: You may use each of the following abilities once per game. You may not use more than one ability per Night.\nCop: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is aligned with the Mafia. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not aligned with the Mafia. You will receive \"No result\" if your investigation failed.\nSeer: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is aligned with the Werewolves. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not aligned with the Werewolves. You will receive \"No result\" if your investigation failed.\nFBI Agent: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is a Serial Killer. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not a Serial Killer. You will receive \"No result\" if your investigation failed.\nConspiracy Theorist:\nDuring the Night, you may PM me the name of another player. You will receive \"You believe NAME to be GUILTY\" if that player is aligned with the Aliens. You will receive \"You believe NAME to be NOT GUILTY\" if that player is not aligned with the Aliens. You will receive \"No result\" if your investigation failed.\nPrivate Investigator: During the Night, you may PM me the name of another player. You will receive \"You believe NAME to be Cult\" if that player is aligned with the Cult faction. You will receive \"You believe NAME to not be Cult\" if that player is not aligned with the Cult. You will receive \"No result\" if your investigation failed.\n",
        "Gladiator": "Gladiator: During the Night, you may PM me the name of two other players. If both of them are alive at daybreak, they are the only two lynch candidates for that day.\n",
        "Persona Non Grata": "Persona Non Grata: If you are lynched, any and all Condemners immediately win.\n",
        "Psychiatrist": "Psychiatrist: During the Night, you may PM me the name of another player. If that player is a Serial Killer, they will turn into a Vanilla Townie.\n",
        "Reloader": "Reloader: During the Night, you may PM me the name of another player. If that player has previously used a 1-shot ability, they regain the use of that ability.\n"
    }
    modifier = {
        "": "",
        "1-Shot": "1-Shot: You may only use this ability once during the game.\n",
        "Compulsive": "Compulsive: You are required to use your ability each Night. If you do not submit a target, it will be randomised.\n",
        "Bulletproof": "Bulletproof: You cannot be nightkilled.\n",
        "Weak": "Weak: If you target a non-Town player, you will die.\n"
    }

class Town(Card):
    def __init__(self, ability, modifier=""):
        self.alignment = "Town"
        self.ability = ability
        self.wincon = "You win when there are no longer any threats to the Town and at least one Town-aligned player is still alive, or nothing can prevent the same."
        self.factional = "During the Day, you may vote for whomever you want eliminated."
        self.abilityDesc = Card.abilityDesc[ability]
        self.modifier = modifier
        self.modifierDesc = Card.modifier[modifier]
        if (self.modifier != ""):
            self.name = modifier + " " + self.alignment + " " + ability
        elif (self.ability == "Vanilla"):
            self.name = "Vanilla Townie"
        elif (self.ability == "Bulletproof"):
            self.name = "Bulletproof Townie"
        elif (self.ability == "Vengeful"):
            self.name = "Vengeful Townie"
        elif (self.ability == "Hirsute"):
            self.name = "Hirsute Townie"
        elif (self.ability == "Evangelistic"):
            self.name = "Evangelistic Townie"
        elif (self.ability == "Tentacled"):
            self.name = "Tentacled Townie"
        elif (self.ability == "Watchlisted"):
            self.name = "Watchlisted Townie"
        elif (self.ability == "Wrong Place at the Wrong Time"):
            self.name = "Wrong Place at the Wrong Time Townie"
        elif (self.ability == "Ascetic"):
            self.name = "Ascetic Townie"
        else:
            self.name = self.alignment + " " + ability

t1 = Town("Vanilla")
t2 = Town("Vanilla")
t3 = Town("Vanilla")
t4 = Town("Vanilla")
t5 = Town("Vanilla")
t6 = Town("Vanilla")
t7 = Town("Vanilla")
t8 = Town("Vanilla")
t9 = Town("Vanilla")
t10 = Town("Vanilla")
t11 = Town("Vanilla")
t12 = Town("Vanilla")
t13 = Town("Watcher")
t14 = Town("Tracker")
t15 = Town("Tracker")
t16 = Town("Cop")
t17 = Town("Cop")
t18 = Town("Cop/Lover")
t19 = Town("Seer")
t20 = Town("Seer")
t21 = Town("FBI Agent")
t22 = Town("Doctor")
t23 = Town("Doctor")
t24 = Town("Roleblocker")
t25 = Town("Jailkeeper")
t26 = Town("Bodyguard")
t27 = Town("Vigilante")
t28 = Town("Vigilante", "1-Shot")
t29 = Town("Day Vigilante", "1-Shot")
t30 = Town("Day Vigilante", "1-Shot")
t31 = Town("Compulsive Childkiller")
t32 = Town("Bulletproof")
t33 = Town("Supersaint")
t34 = Town("Paranoid Gun Owner", "1-Shot")
t35 = Town("Mason")
t36 = Town("Mason")
t37 = Town("Mason")
t38 = Town("Mason")
t39 = Town("Mason/Doctor")
t40 = Town("Mason/Lover")
t41 = Town("Lover")
t42 = Town("Lover")
t43 = Town("Lover")
t44 = Town("Jack-of-all-Trades")
t45 = Town("Vengeful")
t46 = Town("Retired Werewolf Hunter")
t47 = Town("Marine")
t48 = Town("Miller")
t49 = Town("Hirsute")
t50 = Town("Evangelistic")
t51 = Town("Tentacled")
t52 = Town("Watchlisted")
t53 = Town("Wrong Place at the Wrong Time")
t54 = Town("Black Goo")
t55 = Town("Ascetic")
t56 = Town("Private Investigator")
t57 = Town("Gravedigger")
t58 = Town("Nymphomaniac")
t59 = Town("Governor", "1-Shot")
t60 = Town("Prince", "1-Shot")
t61 = Town("Godfather")
t62 = Town("Innocent Child")
t63 = Town("Hider")
t64 = Town("Enabler")
t65 = Town("Tree Stump")
t66 = Town("Conspiracy Theorist")
t67 = Town("Conspiracy Theorist")
t68 = Town("Conspiracy Theorist")
t69 = Town("Kingmaker", "1-Shot")
t70 = Town("Jailkeeper", "Weak")
t71 = Town("Bloodhound")
t72 = Town("Vanilla Cop")
t73 = Town("Hero")
t74 = Town("Tourist")
t75 = Town("Nurse")
t76 = Town("Commuter", "1-Shot")
t77 = Town("Cop-of-all-Trades")
t78 = Town("Gladiator", "1-Shot")
t79 = Town("Persona Non Grata")
t80 = Town("Psychiatrist")
t81 = Town("Reloader")
t82 = Town("Fruit Vendor")
t83 = Town("Parrot")

townCards = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39,
             t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76,
             t77, t78, t79, t80, t81, t82, t83]

class Mafia(Card):
    def __init__(self, ability, modifier=""):
        self.alignment = "Mafia"
        self.ability = ability
        self.wincon = "You win when all players without a Mafia wincon are wiped out and at least one Mafia-aligned player is still alive (or nothing can prevent the same)."
        self.factional = "During the Day, you may vote for whomever you want eliminated.\nFactional Kill: The Mafia may kill one player per Night.\nFactional Communication: If there are other Mafia-aligned players, there will be a Mafia PM that can be used pre-game and during the Night."
        self.abilityDesc = Card.abilityDesc[ability]
        self.modifier = modifier
        self.modifierDesc = Card.modifier[modifier]
        if (self.modifier != ""):
            self.name = modifier + " " + self.alignment + " " + ability
        elif (self.ability == "Alpha"):
            self.name = "Alpha Goon"
        else:
            self.name = self.alignment + " " + ability


m1 = Mafia("Goon")
m2 = Mafia("Goon")
m3 = Mafia("Goon")
m4 = Mafia("Goon")
m5 = Mafia("Goon")
m6 = Mafia("Godfather")
m7 = Mafia("Tracker")
m8 = Mafia("Doctor")
m9 = Mafia("Roleblocker")
m10 = Mafia("Lover")
m11 = Mafia("Seer")
m12 = Mafia("Day Vigilante", "1-Shot")
m13 = Mafia("Governor", "1-Shot")
m14 = Mafia("Strongman")
m15 = Mafia("Reflexive Doctor")
m16 = Mafia("Hirsute")
m17 = Mafia("Cupid")
m18 = Mafia("Alpha")
m19 = Mafia("Hider", "Compulsive")
m20 = Mafia("Fruit Vendor")

mafiaCards = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20]

class Werewolf(Card):
    def __init__(self, ability, modifier = ""):
        self.alignment = "Werewolf"
        self.ability = ability
        self.wincon = "You win when all players without a Werewolf wincon are wiped out and at least one Werewolf-aligned player is still alive (or nothing can prevent the same)."
        self.factional = "During the Day, you may vote for whomever you want eliminated.\nFactional Kill: The Werewolves may kill one player per Night.\nFactional Communication: If there are other Werewolf-aligned players, there will be a Werewolf PM that can be used pre-game and during the Night."
        self.abilityDesc = Card.abilityDesc[ability]
        self.modifier = modifier
        self.modifierDesc = Card.modifier[modifier]
        if (self.modifier != ""):
            self.name = modifier + " " + self.alignment + " " + ability
        elif (self.ability == "Vanilla"):
            self.name = "Vanilla Werewolf"
        elif (self.ability == "Alpha"):
            self.name = "Alpha Werewolf"
        else:
            self.name = self.alignment + " " + ability


w1 = Werewolf("Vanilla")
w2 = Werewolf("Vanilla")
w3 = Werewolf("Vanilla")
w4 = Werewolf("Vanilla")
w5 = Werewolf("Alpha")
w6 = Werewolf("Roleblocker")
w7 = Werewolf("Bulletproof", "1-Shot")
w8 = Werewolf("Cop")
w9 = Werewolf("Mason")
w10 = Werewolf("Watcher")
w11 = Werewolf("FBI Agent")
w12 = Werewolf("Ninja")
w13 = Werewolf("Paranoid Gun Owner", "1-Shot")
w14 = Werewolf("Miller")
w15 = Werewolf("Supersaint")
w16 = Werewolf("Godfather")
w17 = Werewolf("Gravedigger")
w18 = Werewolf("Parrot")

werewolfCards = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18]


class Alien(Card):
    def __init__(self, ability, modifier = ""):
        self.alignment = "Alien"
        self.ability = ability
        self.wincon = "You win when all players without an Alien wincon are wiped out and at least one Alien-aligned player is still alive (or nothing can prevent the same)."
        self.factional = "During the Day, you may vote for whomever you want eliminated.\nFactional Kill: The Aliens may kill one player once during the game.\nFactional Communication: If there are other Alien-aligned players, there will be an Alien PM that can be used pre-game and during the Night.",
        self.abilityDesc = Card.abilityDesc[ability]
        self.modifier = modifier
        self.modifierDesc = Card.modifier[modifier]
        if (self.modifier != ""):
            self.name = modifier + " " + self.alignment + " " + ability
        else:
            self.name = self.alignment + " " + ability


a1 = Alien("Prince", "1-Shot")
a2 = Alien("Prober")
a3 = Alien("Vanillaiser")
a4 = Alien("Silencer")
a5 = Alien("Lover", "Bulletproof")
a6 = Alien("Psychotrooper")
a7 = Alien("Mass Redirector", "1-Shot")
a8 = Alien("Bloodsucker")
a9 = Alien("Sympathiser")

alienCards = [a1, a2, a3, a4, a5, a6, a7, a8, a9]