# 标题页面

init python:
    def main_menu_image(file_name):
        return 'gui/main_menu/' + file_name + '.png'

    def main_menu_pos(num):
        return (1600,200 + 150 * num)

screen main_menu_button(idle_image, hover_image, action):
    imagebutton:
        idle main_menu_image(idle_image)
        hover main_menu_image(hover_image)
        hover_sound audio.se_select
        activate_sound audio.se_ok
        action action
        mouse 'over'

screen main_menu():

    tag menu

    on 'show' action Play('music', 'audio/sys/vol4op_inst.ogg')

    frame:
        style 'empty'
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

        add main_menu_image('title_bg_end')
        add main_menu_image('title_logo'):
            pos (1570,50)

        vbox:
            pos (1600,250)
            spacing 0

            use main_menu_button('start', 'start_hover', Start())
            use main_menu_button('load', 'load_hover', ShowMenu('load', True))
            use main_menu_button('config', 'config_hover', ShowMenu('preferences'))
            # use main_menu_button('extra', 'extra_hover', ShowMenu('gallery'))
            imagebutton:
                idle main_menu_image('extra_disbale')
            use main_menu_button('exit', 'exit_hover', Quit(confirm=not main_menu))
