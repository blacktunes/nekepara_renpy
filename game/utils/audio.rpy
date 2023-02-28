# 主菜单背景音乐
define audio.main_menu_bgm = 'audio/sys/vol4op_inst.ogg'

# 按钮音效
define audio.se_cancel = 'audio/sysse/sysse_cancel.ogg'
define audio.se_ok = 'audio/sysse/sysse_ok.ogg'
define audio.se_select = 'audio/sysse/sysse_select.ogg'

style normal_button:
    mouse 'over'
    hover_sound audio.se_select
    activate_sound audio.se_ok
    padding (0, 0)

style cancel_button:
    mouse 'over'
    hover_sound audio.se_select
    activate_sound audio.se_cancel
    padding (0, 0)
