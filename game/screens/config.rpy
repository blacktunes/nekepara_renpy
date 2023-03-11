default persistent._window_alpha = 1.0

init python:
    def config_image(file_name):
        return 'gui/config/' + file_name + '.png'

    def window_alpha_change(alpha):
        persistent._window_alpha = alpha
        renpy.restart_interaction()

screen text_preview():
    text '猫娘乐园\nNEKO WORKS\n文字显示速度示例':
        style 'say_dialogue'
        pos (710, 400)
        slow_cps True
        line_spacing 15


screen preferences(is_main_menu = False):

    default config_page = 1
    default test = True

    tag menu

    add 'gui/config/config_bg.png'

    hbox:
        align(1.0, 1.0)
        xoffset -15
        spacing -10

        if is_main_menu:
            imagebutton:
                style 'cancel_button'
                idle history_image('title')
                hover history_image('title_hover')
                action MainMenu()

        imagebutton:
            style 'normal_button'
            idle history_image('back')
            hover history_image('back_hover')
            action [Hide('text_preview'), Return()]

    key 'mouseup_3' activate_sound audio.se_cancel action [Hide('text_preview'), Return()]

    hbox:
        align(0.5, 0)
        ypos 80
        spacing 15

        imagebutton:
            style 'normal_button'
            idle config_image('game')
            hover config_image('game_hover')
            insensitive config_image('game_active')
            sensitive config_page != 1
            action [SetScreenVariable('config_page', 1), Show('text_preview')]

        imagebutton:
            style 'normal_button'
            idle config_image('sound')
            hover config_image('sound_hover')
            insensitive config_image('sound_active')
            sensitive config_page != 2
            action [Hide('text_preview'), SetScreenVariable('config_page', 2)]

    if config_page == 1:

        timer 0.01 action Show('text_preview')

        add config_image('config_game'):
            align (0.5, 0.5)
            yoffset 50

        add config_image('preview'):
            pos (680, 350)
            alpha persistent._window_alpha

        bar:
            pos (170, 340)
            value Preference('text speed')
            released [Hide('text_preview'), Show('text_preview')]

        bar:
            pos (170, 460)
            value Preference('auto-forward time')

        bar:
            style 'slider'
            pos (170, 590)
            range 1.0
            changed window_alpha_change
            value persistent._window_alpha

    elif config_page == 2:

        add config_image('config_sound'):
            align (0.5, 0.5)
            yoffset 50

        bar:
            pos (1100, 380)
            value Preference('main volume')

        bar:
            pos (1100, 550)
            value Preference('music volume')

        bar:
            pos (1100, 720)
            value Preference('sound volume')

        bar:
            pos (1100, 890)
            value Preference('voice volume')

    # TODO
    else:
        vbox:
            align (0.5, 0.5)

            hbox:
                box_wrap True

                if renpy.variant('pc') or renpy.variant('web'):

                    vbox:
                        style_prefix 'radio'
                        label _('显示')
                        textbutton _('窗口') action Preference('display', 'window')
                        textbutton _('全屏') action Preference('display', 'fullscreen')

                vbox:
                    style_prefix 'check'
                    label _('快进')
                    textbutton _('未读文本') action Preference('skip', 'toggle')
                    textbutton _('选项后继续') action Preference('after choices', 'toggle')
                    textbutton _('忽略转场') action InvertSelected(Preference('transitions', 'toggle'))


style slider:
    xsize 380
    ysize 40
    base_bar Frame('gui/slider/horizontal_[prefix_]bar.png', None, tile=gui.slider_tile)
    thumb 'gui/slider/horizontal_[prefix_]thumb.png'
    thumb_offset 20
    mouse 'over'
    hover_sound audio.se_select

style vslider:
    xsize 40
    ysize 380
    base_bar Frame('gui/slider/vertical_[prefix_]bar.png', None, tile=gui.slider_tile)
    thumb 'gui/slider/vertical_[prefix_]thumb.png'
    thumb_offset 20
    mouse 'over'
    hover_sound audio.se_select