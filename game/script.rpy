# 游戏在此开始。

label start:
    jump test
    return

image logo = 'brandlogo.png'

define audio.logo_sound = 'audio/sysse/shigu_sys_0001.ogg'
define audio.main_menu_sound = 'audio/sysse/shigu_eye.ogg'

label splashscreen:
    show logo
    with dissolve
    play audio logo_sound

    pause 2

    hide logo
    with dissolve
    stop audio

label before_main_menu:
    play audio main_menu_sound
