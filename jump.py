import random
#import maths


def jump():
    print("---------------------")
    print("Combat jump initiated. \n")

    astro_mods = input("Astrogation+EDU skill modifier: ")
    astro_mods = int(astro_mods)

    dice = random.randint(1, 6) + random.randint(1, 6)
    dice_total = dice
    dice_total_2 = dice_total+(astro_mods-2)
    if dice_total_2 < 4:
        print("Astrogation plot failed. Try again next turn.")
        jump()
    else:
        astro_effect = dice_total_2-4

    jump_mods = input("Course has been successfully plotted. Engineer J-Drive+EDU skill modifier: ")
    jump_mods = int(jump_mods)

    dice_2 = random.randint(1, 6) + random.randint(1, 6)
    dice_total = dice_2
    dice_total_3 = dice_total + (jump_mods-2) + astro_effect

    maint = input("Is the ships maintenance up to date? y/n ")
    if maint == "y":
        maint = 0
    else:
        maint = -1

    fuel = input("Are you using refined fuel? y/n ")
    if fuel == "y":
        fuel = 0
    else:
        fuel = -2

    diam = input("are you outside the 100D limit of a planetary body? y/n ")
    if diam == "y":
        diam = 0
        vbj_mod = -4
    else:
        diam = -4
        vbj_mod = +2

    dice_total_3 = dice_total_3 + maint + fuel + diam
    eng_effect = dice_total_3 - 4

    distance_var = random.randint(1, 6) + random.randint(1, 6) + astro_effect
    print("distance var")
    print(distance_var)
    time_var = random.randint(1, 6) + random.randint(1, 6) + eng_effect
    print("time var")
    print(time_var)

    vbj_dice = random.randint(1, 6) + random.randint(1, 6) + vbj_mod
    vbj_drive = random.randint(1, 6) + random.randint(1, 6)
    vbj_table = {
        2: "\tNo additional effects.",
        3: "\tJump drive requires lengthy recalibration, taking" + str(vbj_drive) + "days after emergence.",
        4: "\tJump drive requires lengthy recalibration, taking" + str(vbj_drive) + "days after emergence.",
        5: "\tJump drive requires lengthy recalibration, taking" + str(vbj_drive) + "days after emergence.",
        6: "\tJump drive requires minor repairs after emergence.",
        7: "\tJump drive requires minor repairs after emergence.",
        8: "\tJump drive requires major repairs at a port after emergence.",
        9: "\tJump drive requires major repairs at a port after emergence.",
        10: "\tJumpspace intrusions occur, dealing " + str(vbj_drive-2) + "% Hull damage every day whilst in jumpspace.",
        11: "\tJumpspace intrusions occur, dealing " + str(vbj_drive-2) + "% Hull damage every day whilst in jumpspace. Jumpdrive is destroyed.",
        12: "\tJumpspace intrusions occur, dealing " + str(vbj_drive-2) + "% Hull damage every day whilst in jumpspace. Jumpdrive is destroyed.",
        13: "\tSevere jumpspace intrusions occur, dealing " + str(vbj_drive+5) + "% Hull damage every day whilst in jumpspace. Jumpdrive is destroyed.",
    }



    if distance_var <= 5 or time_var <= 5:
        bad_jump = ("\tSomething went wrong with the transition into jumpspace. Each Traveller must make an END and INT check. One of the checks needs 6+, the other 10+. Traveller chooses which."
                   +"\nEND check determines physical effects like nausea and possible vomiting. INT check determines mental effects like paranoia and instability."
                   +"\nNote the EFFECT of each roll and consult the GM for repercussions. (Traveller Companion pg. 142)")
    else:
        bad_jump = ""

    if distance_var <=5 and time_var <= 5:
        vbj_result = vbj_table.get(vbj_dice)
        bad_jump = ""
        very_bad_jump = ("\tSomething went very wrong with the transition into jumpspace. Each Traveller must make an END and INT check. One of the checks needs 8+, the other 12+. Traveller chooses which."
                   +"\nEND check determines physical effects like nausea and possible vomiting. INT check determines mental effects like paranoia and instability."
                   +"\nNote the EFFECT of each roll and consult the GM for repercussions. (Traveller Companion pg. 143)")


    else:
        very_bad_jump = ""
        vbj_result = ""

    distance_variance = {
        2: 110-(random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)),
        3: 110-(random.randint(1, 6) + random.randint(1, 6)),
        4: 105-(random.randint(1, 6)),
        5: 100+((random.randint(1, 6) + random.randint(1, 6))*10),
        6: 100+((random.randint(1, 6) + random.randint(1, 6))*5),
        7: 100+(random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)+ random.randint(1, 6)),
        8: 100+(random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)),
        9: 100+(random.randint(1, 6) + random.randint(1, 6)),
        10: 100+(random.randint(1, 6)),
        11: 100+(random.randint(1, 3)),
        12: 100
    }
    if distance_var <= 2:
        distance_var = 2
    elif distance_var >= 12:
        distance_var = 12

    distance_var_2 = distance_variance.get(distance_var)

    if distance_var_2 <= 100:
        distance_var_2 = 100
        precipitation = "Your ship tried to exit Jumpspace within 100D of a planetary body. The jump drive has overheated and needs to cool for " + str(random.randint(6, 24)) + " hours before it can be used again."
    else:
        precipitation = ""

    time_variance = {
        2: (random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6)))))*4,
        3: (random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6)+(random.randint(1, 6))))))*2,
        4: (random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6)))))*2,
        5: (random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6))))*2,
        6: (random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6)+(random.randint(1, 6)))))),
        7: (random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6))))),
        8: (random.randint(1, 6) +(random.randint(1, 6) +(random.randint(1, 6)))),
        9: (random.randint(1, 6) +(random.randint(1, 6))),
        10: (random.randint(1, 6)),
        11: (random.randint(1, 3)),
        12: 160
    }
    if time_var < 2:
        time_var = 2
    elif time_var >= 12:
        time_var = 12

    time_var_2 = time_variance.get(time_var)

    if time_var_2 != 160:
        o_e_check = random.randint(1, 6)
        if o_e_check % 2 == 0:
            odd_even = 0+time_var_2
        else:
            odd_even = 0-time_var_2
    else:
        odd_even = 0

    #six_d = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(
     #   1, 6) + random.randint(1, 6)

    misjump_time = 160 + (random.randint(1, 6) * 24) #+ odd_even
    #misjump_days = round((misjump_time / 24), 2)
    jump_time = 160 + odd_even
    #jump_days = round((jump_time / 24), 2)
    seconds_mj = (misjump_time * 60 * 60) + random.randint(1, 3599)
    seconds = (jump_time * 60 * 60) + random.randint(1, 3599)
    if dice_total_3 < 4:
        print("Jump error detected!")
        if dice_total_3 == 3:
            m, s = divmod(seconds_mj, 60)
            h, m = divmod(m, 60)
            d, h = divmod(h, 24)
            print("The jump takes slightly longer than usual (d/h/m/s): " + "%d:%d:%02d:%02d" % (d, h, m, s))
            print("You are " + str(distance_var_2)  + " diameters away from your target.")
            if precipitation:
                print(precipitation)
            if bad_jump:
                print(bad_jump)
            if very_bad_jump:
                print(very_bad_jump)
            if vbj_result:
                print(vbj_result)
        elif dice_total_3 == 2 or 1:
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            d, h = divmod(h, 24)
            print("The jump takes (d/h/m/s): " + "%d:%d:%02d:%02d" % (d, h, m, s))
            print("The plotted course had an error. You arrive in the desired system " + str(random.randint(1, 6) * random.randint(100, 150)) + " diameters away from your target.")
            if bad_jump:
                print(bad_jump)
            if very_bad_jump:
                print(very_bad_jump)
            if vbj_result:
                print(vbj_result)
        elif dice_total_3 <= 0:
            print("It's all gone wrong. Catastrophic misjump. Consult the GM on exactly what has happened.")


    else:
        print("Jump successful.")

        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        print("The jump takes (d/h/m/s): " + "%d:%d:%02d:%02d" % (d, h, m, s))
        print("You are " + str(distance_var_2) + " diameters away from your target.")
        if precipitation:
            print(precipitation)
        if bad_jump:
            print(bad_jump)
        if very_bad_jump:
            print(very_bad_jump)
        if vbj_result:
            print(vbj_result)

    jump()


jump()
