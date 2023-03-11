init python:
    def history_image(filename):
        return 'gui/history/' + filename + '.png'

    @renpy.pure
    class HistoryVoice(Action, DictEquality):
        def __init__(self, filename):
            self.filename = filename

        def __call__(self):
            if not self.get_sensitive():
                return

            renpy.play(self.filename, 'voice')


screen history():

    tag menu

    ## 避免预缓存此界面，因为它可能非常大。
    predict False

    style_prefix 'history'

    add history_image('backlog')

    hbox:
        align(1.0, 1.0)
        xoffset -15
        spacing -10

        imagebutton:
            style 'cancel_button'
            idle history_image('title')
            hover history_image('title_hover')
            action MainMenu()

        imagebutton:
            style 'normal_button'
            idle history_image('back')
            hover history_image('back_hover')
            action Return()

    key 'mouseup_3' activate_sound audio.se_cancel action Return()

    frame:
        vpgrid:
            cols 1
            yinitial 1.0

            scrollbars 'vertical'
            mousewheel True
            draggable True
            pagekeys True

            side_yoffset 40
            side_ysize 1000

            xsize 1300
            xoffset 290

            for h in _history_list:


                vbox:
                    xfill True
                    ysize 250

                    if h.voice.filename:
                        imagebutton:
                            pos (20, 15)
                            hover_sound audio.se_select
                            idle history_image('voice')
                            hover history_image('voice_hover')
                            action HistoryVoice(h.voice.filename)
                    else:
                        null:
                            height 51
                            pos (20, 15)

                    imagebutton:
                        pos (20, 30)
                        hover_sound audio.se_select
                        idle history_image('jump')
                        hover history_image('jump_hover')
                        action RollbackToIdentifier(h.rollback_identifier)

                    if h.who:
                        label h.who:
                            style 'history_name'
                            substitute False

                            if 'color' in h.who_args:
                                text_color h.who_args['color']
                    else:
                        label '':
                            style 'history_name'
                            substitute False

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

                    image history_image('separate') align (0.5, 1.0)


## 此代码决定了允许在历史记录界面上显示哪些标签。
define gui.history_allow_tags = { 'alt', 'noalt', 'rt', 'rb', 'art' }

style history_frame is empty

style history_name_text is say_label
style history_text is say_dialogue

style history_name:
    xpos 110
    ypos -105

style history_text:
    xpos 100
    ypos -90
    xsize 950
    min_width 950
    text_align 0.0
    layout ('subtitle' if 0.0 else 'tex')
