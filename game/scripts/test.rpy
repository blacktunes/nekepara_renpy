define x = Character('???')
define i = Character('')


image balck = '#000'
image white = '#fff'

label test:
    scene black
    with fade

    scene bg
    with Dissolve(2.0)

    play sound sysse_cancel

    menu:
        '你周围有其他人':
            '不，你周围没有人'
        '你周围没有人':
            pass

    scene black
    with fade

    scene bg
    with Dissolve(2.0)

    play sound 鸟
    stop sound fadeout 5.0

    pause 4

    scene white
    with Dissolve(2.0)

    voice chok_4_90001
    x '「……啾……啾叭……嘿咻……」'

    voice vani_4_90001
    x '「咧咯咧咯……」'

    '——嗯？怎么有一阵阵快感……？'

    '我不是在做梦吧？'

    voice chok_4_90002
    x '「嗯啾……啾叭……嗯咧咯……」'

    voice chok_4_90002
    x '「咧咯咧咯……」'

    '下半身好像有种湿湿暖暖的感觉……？'

    voice 我打你啊
    '想啥呢，醒醒吧'

    scene black
    with Fade(1.0)

    return
