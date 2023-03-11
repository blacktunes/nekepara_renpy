# 存档界面

init python:
    def save_image(file_name):
        return 'gui/save/' + file_name + '.png'

    select_id = 0
    @renpy.pure
    class SaveHover(Action, DictEquality):
        def __init__(self, slot, flag):
            self.slot = slot
            self.flag = flag

        def __call__(self):
            global select_id
            if self.flag:
                select_id = self.slot
            else:
                select_id = 0
            renpy.restart_interaction()

    def is_slot_hover(slot):
        global select_id
        return select_id == slot

screen save(is_main_menu = False):

    tag menu

    use save_window(is_main_menu)



screen load(is_main_menu = False):

    tag menu

    use save_window(is_main_menu)


screen save_window(is_main_menu = False):

    tag menu

    add save_image('save_bg')
    if renpy.current_screen().screen_name[0] == 'load':
        add save_image('load') pos (90, 70)
    else:
        add save_image('save') pos (90, 70)

    hbox:
        align (1.0, 1.0)
        imagebutton:
            style 'cancel_button'
            pos  (-10, 10)
            idle save_image('back')
            hover save_image('back_hover')
            action Return()

    key 'mouseup_3' activate_sound audio.se_cancel action Return()

    hbox:
        align(0.5, 0)
        ypos 80
        spacing 15

        for page in range(1, 3):
            imagebutton:
                style 'normal_button'
                idle save_image(f'page_{page}')
                hover save_image(f'page_{page}_hover')
                insensitive save_image(f'page_{page}_active')
                sensitive not int(persistent._file_page) == page
                action FilePage(page)

    vbox:
        pos (1520, 215)
        spacing 25

        if not is_main_menu:
            imagebutton:
                style 'normal_button'
                idle save_image('menu_save')
                hover save_image('menu_save_hover')
                insensitive save_image('menu_save_active')
                action [ShowMenu('save'), SensitiveIf(renpy.current_screen().screen_name[0] == 'load')]

            imagebutton:
                style 'normal_button'
                idle save_image('menu_load')
                hover save_image('menu_load_hover')
                insensitive save_image('menu_load_active')
                action [ShowMenu('load'), SensitiveIf(not renpy.current_screen().screen_name[0] == 'load')]

        imagebutton:
            style 'normal_button'
            idle save_image('menu_title')
            hover save_image('menu_title_hover')
            action MainMenu()

        imagebutton:
            style 'normal_button'
            idle save_image('menu_exit')
            hover save_image('menu_exit_hover')
            action Quit()

    fixed:
        pos (-200, 70)

        grid 2 4:
            style_prefix 'slot'

            align (0.5,0.5)

            spacing 30

            for i in range(2 * 4):

                $ slot = i + 1

                button:
                    xysize (648, 174)
                    action FileAction(slot)
                    hovered SaveHover(slot, True)
                    unhovered SaveHover(slot, False)

                    add save_image('slot')

                    add FileScreenshot(slot) pos(9,9)

                    hbox:
                        pos (292,131)
                        spacing 2

                        imagebutton:
                            idle save_image('slot_delete')
                            hover save_image('slot_delete_hover')
                            insensitive save_image('slot_delete_disable')
                            action FileDelete(slot)

                        imagebutton:
                            selected is_slot_hover(slot)
                            if renpy.current_screen().screen_name[0] == 'load':
                                idle save_image('slot_load')
                                hover save_image('slot_load_hover')
                                selected_idle save_image('slot_load_hover')
                            else:
                                idle save_image('slot_save')
                                hover save_image('slot_save_hover')
                                selected_idle save_image('slot_save_hover')
                            action FileAction(slot)

                    text FileTime(slot, format=_('{#file_time}%Y/%m/%d %H:%M')):
                        pos (305, 50)
                        size 26
                        color '#990000'
                        bold True

                    key 'save_delete' action FileDelete(slot)

style slot_button is normal_button
style slot_image_button is normal_button