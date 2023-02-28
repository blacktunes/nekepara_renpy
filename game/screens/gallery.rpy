init python:
    g_cg = Gallery()

    g_cg.locked_button = "gallery/locked.png"

    g_cg.button('cg_1')
    g_cg.unlock_image('cg_1')

    g_cg.transition = dissolve

    g_cg._gallery_page = 1

    @renpy.pure
    class GalleryPage(Action, DictEquality):
        def __init__(self, page):
            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            g_cg._gallery_page = self.page
            renpy.restart_interaction()

        def get_selected(self):
            return self.page == g_cg._gallery_page

screen gallery:

    tag menu

    # 背景图。
    add main_menu_image('title_bg_end')

    fixed:

        key "mouseup_3" action Return()

        textbutton _("返回"):
            style "return_button"

            action Return()

        grid 3 3:
            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            if g_cg._gallery_page == 1:
                add g_cg.make_button("cg_1", "gallery/cg_1.png", xalign=0.5, yalign=0.5)

                for page in range(8):
                    imagebutton idle 'gallery/empty.png' xalign 0.5 yalign 0.5
            else:
                for page in range(9):
                    imagebutton idle 'gallery/empty.png' xalign 0.5 yalign 0.5

        hbox:
            xalign 0.5
            yalign 1.0

            spacing gui.page_spacing

            textbutton "1" action GalleryPage(1)
            textbutton "2" action GalleryPage(2)