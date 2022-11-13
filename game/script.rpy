# Characters
define mc = Character("{b}You{/b}", color="#ffffff")
define kyk = Character("{b}K Yeo Ko{/b}", color="#9d73ff")
define yw = Character("{b}Young Woman{/b}", color="#9d73ff")
define tg = Character("{b}Town Guard{/b}", color="#b37932")
define tm = Character("{b}Tavern Master{/b}", color="#39864c")
define fm = Character("{b}Fishmonger{/b}", color="#3286db")
define yb = Character("{b}Young Boy{/b}", color="#89cff0")

define config.menu_include_disabled = True
define fadehold = Fade(0.5, 1.0, 0.5)

label start:

    # Stats
    $ trust = 0
    $ knowledge = 0

    # Choices
    $ tenB = 0
    $ twelveA = 0
    $ twelveC = 0
    $ tavernscene = 0

    # Inventory
    $ silverCoins = 0
    $ map = 0
    $ ring = 0

    label chapter1:

        play music "<from 0.0 to 10.0>audio/cello.mp3" fadeout 1.0

        scene chapter1 with Dissolve(2.5)
        pause 5.0
        scene black with Dissolve(2.5)

    label one:

        play music "audio/heavyheart.mp3" fadeout 1.0

        scene wizardhut with dissolve
        "{i}You gradually awake from your slumber.{/i}"
        mc "Ugh... W-Where am I?"

    menu:

        "Retrace your memory.":
            jump two

        "Go to bed.":
            "{i}You close your eyes and begin to fall asleep.{/i}"
            scene black with dissolve
            "{i}You sleep for a few hours.{/i}"
            jump one

        "Get up and explore outside the hut.":
            jump three

    label two:

        mc "Ugh... I can't seem to remember anything."
        mc "I should try looking around this hut for some information."
        "{i}You look around the hut only to find a couple of books on the dusty shelves.{/i}"
        "{i}You learn that you are in a region called Kisandre Land and it's currently the year 1350 where most of the population has died.{/i}"
        "{i}The source of all those deaths was a plague which spread easily, even with the presence of holy magic.{/i}"
        mc "It seems that this plague is still ongoing."
        mc "I should avoid people if I could - not that it's any different from where I'm from..."
        "{i}While searching around, you see a poster of a wanted man on the wall of the hut.{/i}"
        "{b}{i}BOUNTY - WANTED DEAD OR ALIVE{/i}{/b}"
        "{b}{i}FOR ILLEGAL USAGE OF MAGIC AND INTERFERENCE OF THE SPACE TIME CONTINUUM{/i}{/b}"
        mc "Time? Wait, magic?"
        mc "Is this man the reason why I got transported here?!"
        mc "I need to find him, as soon as possible!"
        "{i}You decide that you could find this person for help in returning you back to your own timeline.{/i}"

    label three:

        "{i}You proceed to leave the wooden hut, picking up a few {color=#00ff00}silver coins{/color} you spot on the table.{/i}"
        "You found some {color=#00ff00}silver coins{/color}!"
        $ silverCoins = 1

        scene forestone with dissolve
        "{i}Walking aimlessly on the road, and you soon spot a figure from afar.{/i}"
        "{i}A young woman, carrying a basket full of what seems like potion bottles.{/i}"

    label four:

    menu:

        "Approach the woman.":
            jump five

        "Leave the woman alone.":
            "{i}You ignore the woman, continuing your walk through the forest.{/i}"
            jump seven

        "Wait and think.":
            "{i}You stand there, second guessing your decisions...{/i}"
            jump four

    label five:

        "{i}You approach her on a whim, hoping she could fill you in what is going on.{/i}"
        mc "Hello! Can I-"
        yw "Eeek! Who are you and what do you want?!"
        "{i}She flinches and backs away from you.{/i}"
        mc "Sorry for scaring you, but I have no idea how I got here and I'd appreciate it if you can help me out here."
        mc "I'm not a bandit, please trust me..."
        "{i}She takes a deep breath, and calms down.{/i}"
        yw "Sorry, it's just that... It's very dangerous around here."
        mc "I'm sorry, it's my fault for approaching you so suddenly."
        yw "Hold on, why did you come from the direction of the wizard's house?"
        mc "{i}Oh, so that was the wizard's house.{/i}"
        mc "{i}That explains the books and weird supplies that I found.{/i}"

    menu:

        "Tell her that you were kidnapped.":
            mc "To tell the truth, I was kidnapped and brought here against my will."
            mc "It was sudden and I have no idea where I am or what is going on."
            $ trust += 1
            jump six

        "Tell her that you are a friend of the wizard.":
            mc "I am a friend of the wizard and I would appreciate it if you bring me to him as we have matters to discuss."
            $ trust -= 1
            jump six

        "Ask her what she is doing here.":
            mc "That's not the point. What about you? What are you doing here?"
            jump six

    label six:

        yw "I-I'm sorry I have to go!"
        "{i}She ran away.{/i}"
        mc "Why did she run away? Did I say something wrong?"
        mc "I hope nothing bad comes from that interaction..."
        mc "Anyways, I should probably continue walking."

    label seven:

        scene foresttwo with dissolve
        mc "Where am I going? It looks like it's going to get dark soon and there's no telling what could happen until then."
        "{i}You spot a glow of light in front of you and you see some moving figures on the road not too far ahead.{/i}"
        mc "Hmmm, what should I do?"

    menu:

        "Sneak away from the light and tread down the path quietly.":
            jump eight

        "Walk towards the light and try your luck.":
            jump ten

    label eight:

        scene foresttwo with vpunch
        "{i}You trip over in the dark and hit your head.{/i}"

        scene black with dissolve
        "{i}You faint for a few minutes.{/i}"

        scene foresttwo with dissolve
        "{i}You feel an unending throbbing ache in your head slowly eroding your mind the further you go.{/i}"
        mc "Argh! What, what's happening?"
        mc "Ugh, why does it hurt so much..."
        mc "I shouldn't have gone there... I'm an idiot!"
        "{i}You continue down the path, all while withstanding the immense pain{/i}"
        "{i}You steel your resolve to follow up on your decisions to the end.{/i}"
        "{i}It wasn't long before hunger starts to settle in, and you need food immediately.{/i}"

    menu:

        "Starve through and continue your journey.":
            jump nine

        "Move off-course in search of potential food.":
            jump ten

    label nine:

        "{i}You reminisce your life to distract your mind, wandering ever so slowly yet steadily on your path.{/i}"
        mc "Mom, dad, where are you..."
        "{i}Occupied with the thought of the past, you eventually stumble upon a town...{/i}"

    label ten:

        "{i}Thinking that your journey is at its end, you smile seeing a town brimming with life.{/i}"

        scene townentrance with dissolve
        "{i}You get close to the town entrance and see the figure of a town guard.{/i}"
        "{i}You approach him.{/i}"
        "{i}The guard spares no time and reacts swiftly, pointing a spear at your neck.{/i}"

        play music "audio/crisis.mp3" fadeout 1.0

        tg "Who are you and what are you doing in Jerus?!"
        tg "Who is your lord?!"
        mc "!!!"
        tg "I'll count to five before I slice your head off!"
        tg "ANSWER ME NOW!"
        "{i}Tired from the journey, your mind could barely stay calm.{/i}"
        "{i}In the nick of the moment, you choose to...{/i}"

    menu:

        "Bribe the guard.":
            "{i}You reach into your pocket, hoping to find something valuable. You offer a few {color=#00ff00}silver coins{/color} you've picked up from the wooden hut earlier.{/i}"
            "{i}The guard pushes your arm under before sneakily accepting the coins, hunched over - to avoid being seen by anyone.{/i}"
            "{i}He smiles gleefully and lets you past; you wonder how much those coins are really worth.{i}"
            $ trust -= 1
            jump eleven

        "Run away and look for another entrance.":
            "{i}You dodge under the spear held against your neck and dash away before slipping through a tiny crack in the wall to enter the town.{/i}"
            $ tenB = 1
            jump eleven

        "Tell him you're looking for a wizard.":
            "I won't question why, but don't blame me if you get into trouble."
            "{i}The guard puts down his spear and lets you by.{/i}"
            $ trust += 1
            jump eleven

    label eleven:

        play music "audio/folkround.mp3" fadeout 1.0

        scene towncentre with dissolve
        "{i}You enter the town and start looking for clues.{/i}"
        "{i}You start by asking around for anybody who might know the wizard.{/i}"
        mc "Hello, do you know anything about the wizard that lives outside the town?"
        "{i}The townsfolk ignore you.{/i}"
        "{i}You think that they might know something about the wizard by the look on their faces.{/i}"
        "{i}You decide to continue your search in...{/i}"

    menu:

        "A nearby tavern.":
            jump tavernscene

        "The town market.":
            jump marketscene

    label tavernscene:

        scene towntavern with dissolve
        play music "audio/tavernloop.mp3" fadeout 1.0
        "{i}You invite yourself into the local tavern. It reeks of drunkards.{i}"
        "{i}Pulling up your shirt, you hurry to the counter to meet the master here.{i}"
        mc "Hey, have you seen a woman with a basket full of potions and a white shawl?"
        tm "No requests here. You come here to have a drink or you find yourself out of this place."
        mc "Please, I have to meet her somehow!"
        "{i}The tavern master slams his hand on the counter-{i}"
        tm "Now I don't know what you're thinking here, I don't do naught for free, now do you want me to repeat that?!"
        "{i}The patrons in the tavern all set their sights on you.{i}"
        "{i}You choose to...{/i}"

    menu:

        "Buy a drink.":
            mc "What if I help myself to a drink?"
            tm "Name your price."
            "{i}You reach into your pocket for a few {color=#00ff00}silver coins{/color} and place it on the counter.{i}"
            $ silverCoins = 0
            mc "Is this enough?"
            tm "More than enough..."
            "{i}He smirks before moving towards you.{i}"
            tm "Words do get around, now I do not know what matters you have with her but I do hear her family is often found in the town's market not far from here."
            mc "What do they look like?"
            tm "A {color=ffff00}young boy{/color} clad in grey robes; that's all I'm telling you."
            mc "I appreciate it."
            "{i}As another patron called for him, he leans over to continue his business as per usual.{i}"
            "{i}The master smiles at you before waving you off cheerfully.{i}"
            "{i}You proceed to leave the tavern.{i}"
            $ tavernscene = 1
            jump marketscene

        "Leave the tavern.":
            "{i}You proceed to leave the tavern.{i}"
            jump marketscene

    label marketscene:

        scene townmarket with dissolve

        play music "audio/folkround.mp3" fadeout 1.0

        fm "Wild cod, freshly caught! Only 3 copper per head!"
        "{b}{color=#bb4113}Grocer{/color}{/b}" "Apples are ripe and ready, red as far as could be!"
        "{i}A scenery of a busy market, \"This city is undeniably prosperous\", you think to yourself.{i}"
        mc "Sir, do you know of a woman with a basket full of potions and a white shawl?"
        fm "Gah! I'm sick of you people who come, come all o'er my stall here; blocking my business - thinking I owe you any favour!"
        fm "Move along if you're not going to buy anything!"
        "{i}Seeing the enraged fishmonger, you choose to...{i}"

    menu:

        "Walk away from the stall.":
            mc "Alright, I won't bother you again."
            "{i}You walk away.{/i}"
            jump twelve

        "Beg him":
            mc "Please, I'm sure you know something!"
            "{i}The fishmonger shouts at you again. Passersby look at you oddly.{/i}"
            "{i}You walk away.{/i}"
            jump twelve

        "Punch him.":
            "{i}You punch the fishmonger square in the face.{/i}"

            play music "audio/crisis.mp3" fadeout 1.0

            fm "Agh! So that's how you want to do it!"

            scene townmarket with vpunch
            "{i}The fishmonger rushes at you and punches you back, knocking you to the ground.{/i}"

            scene black with dissolve
            "{i}Your vision blurs, you could only see figures of townsfolk walking through the street, none stop to tend for you.{/i}"
            "{i}You eventually lose consciousness.{/i}"
            "{i}The end.{i}"
            return

    label twelve:

        "{i}Walking around the market, you spot a few people that are not occupied with anything currently.{/i}"

    if tavernscene == 1:
        menu twelvemenuA:

            "Ask an old woman." if twelveA == 0:
                $ twelveA = 1
                mc "Good day madam. I'm looking for a woman with a basket full of potions."
                mc "Do you happen to know her?"
                "{b}{color=#a8003b}Old Woman{/color}{/b}" "I'm sorry dear, I do not know who that is."
                jump twelvemenuA

            "{color=#ffff00}Ask a young boy{/color}":
                mc "Hello there, I'm looking for a woman with a basket full of potions."
                mc "Do you happen to know her?"
                yb "Hmm... She might be my aunt. Was she wearing a white lace shawl?"
                mc "A white lace shawl... Oh, yes, she was! Could you bring me to her?"
                yb "Sure!"
                jump thirteen

            "Ask a young man." if twelveC == 0:
                $ twelveC = 1
                mc "Good day sir. I'm looking for a woman with a basket full of potions."
                mc "Do you happen to know her?"
                "{b}{color=#4856c7}Young Man{/color}{/b}" "..."
                mc "I guess not."
                jump twelvemenuA

    else:
        menu twelvemenuB:

            "Ask an old woman." if twelveA == 0:
                $ twelveA = 1
                mc "Good day madam. I'm looking for a woman with a basket full of potions."
                mc "Do you happen to know her?"
                "{b}{color=#a8003b}Old Woman{/color}{/b}" "I'm sorry dear, I do not know who that is."
                jump twelvemenuB

            "Ask a young boy.":
                mc "Hello there, I'm looking for a woman with a basket full of potions."
                mc "Do you happen to know her?"
                yb "Hmm... She might be my aunt. Was she wearing a white lace shawl?"
                mc "A white lace shawl... Oh, yes, she was! Could you bring me to her?"
                yb "Sure!"
                jump thirteen

            "Ask a young man." if twelveC == 0:
                $ twelveC = 1
                mc "Good day sir. I'm looking for a woman with a basket full of potions."
                mc "Do you happen to know her?"
                "{b}{color=#4856c7}Young Man{/color}{/b}" "..."
                mc "I guess not."
                jump twelvemenuB

    label thirteen:

        if tenB == 0:
            jump fourteen

        "{i}The young boy leads you to his aunt's house.{/i}"

        scene towncentre with dissolve
        tg "Hey you! How did you get into the town?!"

        scene towncentre with vpunch
        "{i}You get arrested by the guard. You get thrown into jail.{/i}"

        scene black with dissolve
        "{i}The end.{/i}"
        return

    label fourteen:

        "{i}The young boy leads you to his aunt's house.{/i}"

        scene towncentre with dissolve
        "{i}*knock* *knock* *knock*{/i}"
        "{i}A young woman opens the door.{/i}"
        yw "Y-You..."

    menu:

        "Ask her why she ran away.":
            mc "Why did you run away from me just now?"
            "{i}The young woman panicks as she calls for the town guard and gets you arrested.{/i}"

            scene black with dissolve
            "{i}The end.{/i}"
            return

        "Beg her for help." if trust >= 0:
            $ knowledge += 1
            mc "Please help me, I really need your help..."
            "{i}The young woman seems hesitant to help you out.{/i}"
            yw "Fine, come in."
            kyk "By the way, my name is K Yeo Ko."
            jump fifteen

        "Calmly talk to her." if trust == 2:
            $ knowledge += 2
            mc "Hello again, I could really use your help. Will you help me?"
            "{i}The young woman decides to trust you and is willing to help you out.{/i}"
            yw "Sure, come on in."
            kyk "By the way, the name's K Yeo Ko."
            jump sixteen

    label fifteen:

        scene kykhouse with dissolve
        kyk "This is my home. Let's start."
        kyk "So, I have not seen the wizard for a few months now."
        kyk "But, he gave me a {color=#00ff00}map{/color} with an X marked on it. I am unable to decipher what it means though-"
        mc "- That must be where he is!"
        mc "Thank you, I really appreciate your help!"
        kyk "Wait, let me-"
        "You found a {color=#00ff00}map{/color}!"
        $ map = 1
        "{i}You leave quickly, satisfied with the information you received.{/i}"
        jump chapter2

    label sixteen:

        scene kykhouse with dissolve
        kyk "Welcome to my home! Have a seat!"
        "{i}You chat a little with [kyk] and learn more about her.{/i}"
        kyk "I'm not really sure if I should tell you this, but I think it's important for you to know."
        kyk "The wizard is actually my brother and I have not seen him for a few months now."
        kyk "He'll usually write to me but I have not seen Pidg for quite some time now and I'm really worried."
        mc "Pidg? Who's that?"
        kyk "Oh, Pidg is our messenger bird and we send letters with it."
        kyk "My brother is a very respectable wizard. I don't think he's made any enemies too... What should I do?"
        mc "Don't worry, I will find him. Do you have any idea where he might be?"
        kyk "Look, he gave me this {color=#00ff00}map{/color} with an X marked on it. He told me that he would be there."
        mc "Thank you so much! {i}*hug*{/i}"
        "You found a {color=#00ff00}map{/color}!"
        $ map = 1
        kyk "Here, take this {color=#00ff00}ring{/color} as well. Bring it to him and he'll know that you've met me. I think it will surely help you out!"
        mc "{i}*touched*{/i} Now I will definitely need to find him, wouldn't I?"
        "You found a {color=#00ff00}ring{/color}!"
        $ ring = 1
        "{i}You leave quickly, satisfied with the information you received.{/i}"
        jump chapter2

    label chapter2:

        play music "<from 0.0 to 10.0>audio/cello.mp3" fadeout 1.0

        scene chapter2 with Dissolve(2.5)
        pause 5.0
        scene black with Dissolve(2.5)

return
