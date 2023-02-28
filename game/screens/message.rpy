init python:
    def message_image(file_name):
        return 'gui/message/' + file_name + '.png'

    quick_menu_id = 0
    @renpy.pure
    class QuickMenuHover(Action, DictEquality):
        def __init__(self, menu_id, flag):
            self.menu_id = menu_id
            self.flag = flag

        def __call__(self):
            global quick_menu_id
            if self.flag:
                quick_menu_id = self.menu_id
            else:
                quick_menu_id = 0
            renpy.restart_interaction()

    def is_menu_hover(menu_id):
        global quick_menu_id
        return quick_menu_id == menu_id

# 对话框
screen say(who, what):
    style_prefix 'say'

    window:
        id 'window'

        if who is not None:

            window:
                id 'namebox'
                style 'namebox'
                text who id 'who'

        text what id 'what'

    image message_image('breakglyph'):
        at transform:
            alpha 0
            linear 0.7 alpha 0.9
            linear 0.7 alpha 0
            repeat
        pos (1530,970)

    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为没有空间。
    if not renpy.variant('small'):
        add SideImage() xalign 0.0 yalign 1.0

    if voice_can_replay():
        imagebutton:
            pos (295,780)
            idle message_image('voice')
            hover message_image('voice_hover')
            action VoiceReplay()

    imagebutton:
        pos (1550,800)
        idle message_image('window_hide')
        hover message_image('window_hide_hover')
        action renpy.curried_call_in_new_context('_hide_windows')

    grid 4 2:
        pos (1650,860)
        spacing -7

        imagebutton:
            hovered QuickMenuHover(1, True)
            unhovered QuickMenuHover(1, False)
            idle message_image('quick_save')
            hover message_image('quick_save_hover')
            action QuickSave()

        imagebutton:
            hovered QuickMenuHover(2, True)
            unhovered QuickMenuHover(2, False)
            idle message_image('save')
            hover message_image('save_hover')
            action ShowMenu('save')

        imagebutton:
            hovered QuickMenuHover(3, True)
            unhovered QuickMenuHover(3, False)
            idle message_image('auto')
            hover message_image('auto_hover')
            selected_idle message_image('auto_active')
            action Preference('auto-forward', 'toggle')

        imagebutton:
            hovered QuickMenuHover(4, True)
            unhovered QuickMenuHover(4, False)
            idle message_image('backlog')
            hover message_image('backlog_hover')
            action ShowMenu('history')

        imagebutton:
            hovered QuickMenuHover(5, True)
            unhovered QuickMenuHover(5, False)
            idle message_image('quick_load')
            hover message_image('quick_load_hover')
            action QuickLoad()

        imagebutton:
            hovered QuickMenuHover(6, True)
            unhovered QuickMenuHover(6, False)
            idle message_image('load')
            hover message_image('load_hover')
            action ShowMenu('load')

        imagebutton:
            hovered QuickMenuHover(7, True)
            unhovered QuickMenuHover(7, False)
            idle message_image('skip')
            hover message_image('skip_hover')
            selected_idle message_image('skip_active')
            action Skip() alternate Skip(fast=True, confirm=True)

        imagebutton:
            hovered QuickMenuHover(8, True)
            unhovered QuickMenuHover(8, False)
            idle message_image('config')
            hover message_image('config_hover')
            action ShowMenu('preferences', True)

    if quick_menu_id != 0:
        frame:
            style 'empty'
            at transform:
                alpha 0
                pos (1650,1015)
                linear 0.1:
                    alpha 1
                    pos (1650,1005)

            pos (1650,1005)
            xysize (220, 26)
            add message_image('help')

            if quick_menu_id == 1:
                add message_image('help_quick_save') ypos 6 xalign 0.5
            elif quick_menu_id == 2:
                add message_image('help_save') ypos 6 xalign 0.5
            elif quick_menu_id == 3:
                add message_image('help_auto') ypos 6 xalign 0.5
            elif quick_menu_id == 4:
                add message_image('help_backlog') ypos 6 xalign 0.5
            elif quick_menu_id == 5:
                add message_image('help_quick_load') ypos 6 xalign 0.5
            elif quick_menu_id == 6:
                add message_image('help_load') ypos 6 xalign 0.5
            elif quick_menu_id == 7:
                add message_image('help_skip') ypos 6 xalign 0.5
            elif quick_menu_id == 8:
                add message_image('help_config') ypos 6 xalign 0.5

    key 'mousedown_4' action ShowMenu('history')


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 290

    background Image(message_image('window'), xalign=0.5, yalign=1.0)

style namebox:
    xpos 400

style say_label:
    align (1.0,0.5)
    size 48
    color '#fdca0f'
    outlines [ (absolute(5), '#442211', absolute(0), absolute(0)) ]

style say_dialogue:
    size 42
    outlines [ (absolute(2), '#442211', absolute(0), absolute(0)) ]

    xpos 400
    ypos 75
    xsize 1200

    adjust_spacing False

style say_image_button:
    mouse 'over'
    activate_sound audio.se_ok

screen choice(items):
    style_prefix 'choice'

    fixed:
        style 'empty'

        at transform:
            alpha 0.0
            linear 0.2 alpha 1.0

        vbox:
            for i in items:
                textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 390
    yanchor 0.5

    spacing 80

style choice_button is normal_button:
    xysize (1380,120)
    background message_image('select')
    hover_background message_image('select_hover')

style choice_button_text:
    min_width 1380
    text_align 0.5
    color '#fff'
    outlines [ (absolute(2), '#00000099', absolute(0), absolute(0)) ]
