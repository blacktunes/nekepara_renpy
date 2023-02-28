screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix 'confirm'

    add 'gui/overlay/confirm.png'

    fixed:

        add 'gui/confirm/dialog.png' align (0.5, 0.5)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 45

            label _(message):
                style 'confirm_prompt'
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                imagebutton:
                    style 'normal_button'
                    idle 'gui/confirm/dialog_yes.png'
                    hover 'gui/confirm/dialog_yes_hover.png'
                    action yes_action

                imagebutton:
                    style 'cancel_button'
                    idle 'gui/confirm/dialog_no.png'
                    hover 'gui/confirm/dialog_no_hover.png'
                    action no_action

    key 'mouseup_3' activate_sound audio.se_cancel action no_action
