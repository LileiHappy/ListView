from tkinter import Frame
from tkinter import Label
from tkinter import PhotoImage
from tkinter.ttk import Progressbar
from tkinter.ttk import Style
from vo.poetry import Poetry
from resource.colors import theme


class PoetryListViewItemView(Frame):

    def __init__(self, container_view, item: Poetry, *args, **kwargs):
        super().__init__(container_view, *args, **kwargs)
        if 'width' in kwargs.keys():
            self.__width = kwargs['width']
        if 'height' in kwargs.keys():
            self.__height = kwargs['height']
        self.__main_frame = Frame(self, width=self.__width, height=self.__height - 16, background=theme,
                                  highlightthickness=0)
        self.__main_frame.pack(fill='x', expand=True)
        self.__main_frame.pack_propagate(False)
        self.__create_progressbar_view(item.recite_progress())
        self.__create_main_view(item)

    def __create_progressbar_view(self, progress):
        style = Style()
        style.theme_use('clam')
        style.configure('my.Horizontal.TProgressbar', troughcolor='white', background=theme)
        self.__progress_bar = Progressbar(self, style='my.Horizontal.TProgressbar', orient='horizontal', length=100,
                                          mode='determinate')
        self.__progress_bar.pack(fill='x', expand=True)
        self.__progress_bar['value'] = progress

    def __create_main_view(self, item):
        self.__create_image_view(item.art_picture_path())
        self.__create_detail_view(item)
        self.__create_main_text_view(item)
        self.__create_address_date_view(item)

    def __create_image_view(self, art_picture_path):
        image_container_view = Frame(self.__main_frame, width=self.__height, height=self.__height, highlightthickness=0,
                                     borderwidth=0)
        image_container_view.pack_propagate(False)
        image_container_view.pack(side='left', padx=(0, 10))
        self.__image = PhotoImage(master=self, file=art_picture_path)
        # self.__scale_image = image.subsample(4, 4)
        self.__art_picture = Label(image_container_view, image=self.__image, width=self.__height, height=self.__height,
                                   highlightthickness=0, borderwidth=0, background=theme)
        self.__art_picture.pack()

    def __create_detail_view(self, item):
        top_container_view = Frame(self.__main_frame, background=theme)
        top_container_view.pack(side='top', fill='x', expand=True)
        # title_subtitle_container_view = Frame(top_container_view)
        # title_subtitle_container_view.pack()
        # self.__title = Label(title_subtitle_container_view, text=item.title())
        # self.__title.pack(side='left', ipadx=0, padx=0)
        self.__title = Label(top_container_view, text=item.title_subtitle(), background=theme)
        self.__title.pack()
        # self.__subtitle = Label(title_subtitle_container_view, text=item.subtitle())
        # self.__subtitle.pack(side='left', ipadx=0, padx=0)
        self.__author = Label(top_container_view, text=item.author(), background=theme)
        self.__author.pack(side='right')

    def __create_main_text_view(self, item):
        middle_container_view = Frame(self.__main_frame, background=theme)
        middle_container_view.pack(fill='x', expand=True)
        # self.__introduce = Label(middle_container_view, text=item.introduce())
        # self.__introduce.pack()
        self.__main_text = Label(middle_container_view, text=item.introduce_main_text(), background=theme)
        self.__main_text.pack()

    def __create_address_date_view(self, item):
        bottom_container_view = Frame(self.__main_frame, background=theme)
        bottom_container_view.pack(side='bottom', fill='x', expand=True)
        self.__date = Label(bottom_container_view, text=item.publish_time(), background=theme)
        self.__date.pack(side='right', padx=0)
        self.__address = Label(bottom_container_view, text=item.address(), background=theme)
        self.__address.pack(side='right', padx=(0, 10))

    def update_view(self, item):
        self.__title.configure(text=item.title_subtitle())
        # self.__title.configure(text=item.title())
        # self.__subtitle.configure(text=item.subtitle())
        self.__author.configure(text=item.author())
        # self.__introduce.configure(text=item.introduce())
        # self.__main_text.configure(text=item.main_text())
        self.__main_text.configure(text=item.introduce_main_text())
        self.__address.configure(text=item.address())
        self.__date.configure(text=item.publish_time())
        self.__progress_bar['value'] = item.recite_progress()
        self.update_idletasks()
