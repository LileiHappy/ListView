from tkinter import Tk
from poetry_listview_adapter import PoetryListViewAdapter
from list_view import ListView
from vo.poetry import Poetry
from poetry_extractor import extract
from threading import Timer
from resource.colors import theme
import os

DELAY_UPDATE_DURATION = 5


class PoetryListView:

    def __init__(self):
        self.__root = Tk()
        self.__window_width = 0
        self.__window_height = 0
        self.__list_view = None
        self.__adapter = None
        self.__poetry_list: [Poetry] = []

    def __fetch_screen_size(self):
        return self.__root.winfo_screenwidth(), self.__root.winfo_screenheight()

    def calculate_display_info(self):
        screen_width, screen_height = self.__fetch_screen_size()
        self.__window_width = int(screen_width * 3 / 4)
        self.__window_height = int(screen_height * 3 / 4)
        display_start_point_x = (screen_width - self.__window_width) >> 1
        display_start_point_y = (screen_height - self.__window_height) >> 1
        display_info = (self.__window_width, self.__window_height, display_start_point_x, display_start_point_y)
        return display_info

    def display_in_center(self, display_info):
        self.__root.title('PoetryListView')
        self.__root.geometry('{}x{}+{}+{}'.format(display_info[0], display_info[1], display_info[2], display_info[3]))

    def create_view(self):
        item_width = int(self.__window_width * 3 / 4)
        self.__adapter = PoetryListViewAdapter(item_width=item_width, item_height=226, data=self.__poetry_list)
        self.__list_view = ListView(self.__root, self.__adapter, width=item_width, height=self.__window_height,
                                    background=theme)

    def layout(self):
        self.__list_view.pack(fill='both', expand=True)

    def prepare_data(self):
        poetries = extract()
        for index in range(10000):
            self.__poetry_list.append(poetries[index % 10])

    def show_listview(self):
        self.__adapter.update()

    def update(self, index):
        if index < 0 or index > len(self.__poetry_list) - 1:
            return
        self.__poetry_list[index].set_recite_progress(100)
        self.__adapter.update_view(index)

    def update_refresh(self):
        for index in range(1000):
            self.__poetry_list[index].set_recite_progress(66)
        self.__adapter.update()

    def remove_refresh(self):
        for index in range(9990):
            self.__poetry_list.pop()
        self.__adapter.set_data(self.__poetry_list)

    def add_refresh(self, poetry):
        self.__adapter.add_item(poetry)

    def add_all_refresh(self, poetries):
        self.__adapter.add_items(poetries)

    def show(self):
        self.__root.mainloop()

    def destroy(self):
        self.__root.destroy()


def main():
    poetry_listview = PoetryListView()
    display_info = poetry_listview.calculate_display_info()
    poetry_listview.display_in_center(display_info)
    poetry_listview.create_view()
    poetry_listview.layout()
    poetry_listview.prepare_data()
    poetry_listview.show_listview()

    timer_refresh = Timer(DELAY_UPDATE_DURATION, poetry_listview.update_refresh)
    timer_refresh.start()

    timer_remove = Timer(DELAY_UPDATE_DURATION << 1, poetry_listview.remove_refresh)
    timer_remove.start()

    timer_refresh_one = Timer((DELAY_UPDATE_DURATION << 1) + DELAY_UPDATE_DURATION, poetry_listview.update, (0,))
    timer_refresh_one.start()

    poetry = Poetry('少年行', '李白', '五陵年少金市东\n银鞍白马度春风\n落花踏尽游何处\n笑入胡姬酒肆中', '时间不详',
                    '旧时燕地', recite_progress=99, art_picture_path=os.path.join('resource', 'pic{}.png'.format(2)))
    timer_add_one = Timer(DELAY_UPDATE_DURATION << 2, poetry_listview.add_refresh, (poetry,))
    timer_add_one.start()

    timer_add_refresh = Timer((DELAY_UPDATE_DURATION << 2) + DELAY_UPDATE_DURATION, poetry_listview.add_all_refresh,
                              ([poetry, poetry],))
    timer_add_refresh.start()

    poetry_listview.show()


if __name__ == '__main__':
    main()
