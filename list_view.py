from tkinter import Frame
from tkinter import Canvas
from tkinter import Scrollbar


class ListView(Frame):
    def __init__(self, container_view, adapter, *args, **kwargs):
        super().__init__(container_view, *args, **kwargs)
        if 'width' in kwargs.keys():
            self.__width = kwargs['width']
        if 'height' in kwargs.keys():
            self.__height = kwargs['height']
        if 'background' in kwargs.keys():
            self.__background = kwargs['background']
        self.__adapter = adapter
        self.__create_view()
        self.__configure()
        self.__layout()
        self.__bind_event()
        self.__boundary_relaxation_threshold = 1
        self.__visible_items_index_mapping = {}
        self.__canvas_item_index_mapping = {}
        self.__adapter.set_data_changed_notifier(self.update_item_view)
        self.__item_count = adapter.get_count()
        self.__item_height = adapter.get_item_height(0)
        self.__update_scroll_region()
        self.__invalidate_view()

    def __create_view(self):
        self.__canvas = Canvas(self, width=self.__width, highlightthickness=0, background=self.__background)
        self.__scroll_bar = Scrollbar(self, orient='vertical', command=self.__intercept_scroll_may)

    def __intercept_scroll_may(self, *args):
        self.__canvas.yview(*args)
        self.__invalidate_view()

    def __configure(self):
        self.__canvas.configure(yscrollcommand=self.__scroll_bar.set)

    def __layout(self):
        self.__canvas.pack(side='left', fill='y', expand=True)
        self.__scroll_bar.pack(side='right', fill='y')

    def __bind_event(self):
        self.__canvas.bind('<Configure>', self.__canvas_configure)
        self.__canvas.bind_all('<MouseWheel>', self.__on_mouse_wheel)

    def __canvas_configure(self, event):
        self.__update_scroll_region()
        self.__invalidate_view()

    def __on_mouse_wheel(self, event):
        if event.delta > 0:
            self.__canvas.yview_scroll(-1, 'units')
        elif event.delta < 0:
            self.__canvas.yview_scroll(1, 'units')
        self.__invalidate_view()

    def __on_scroll(self, event):
        self.__invalidate_view()

    def __update_scroll_region(self):
        total_height = self.__item_height * self.__item_count
        self.__canvas.configure(scrollregion=(0, 0, 1, total_height))

    def __invalidate_view(self):
        if self.__item_count <= 0:
            return
        visible_start_index, visible_end_index = self.__get_visible_items_index_range()
        delete_index_bottom = max(0, visible_start_index - 1)
        delete_index_up = min(visible_end_index + 1, self.__item_count - 1)
        self.__delete_item_view_out_range(delete_index_bottom, delete_index_up)
        self.__update_visible_items(visible_start_index, visible_end_index)
        # self.after(self.__DELAY_UPDATE_DURATION, self.__check_update)

    def __get_visible_items_index_range(self):
        visible_top_y = self.__canvas.canvasy(0)
        visible_bottom_y = visible_top_y + self.__height
        visible_start_index = max(0, int(visible_top_y / self.__item_height) - self.__boundary_relaxation_threshold)
        visible_end_index = min(int(visible_bottom_y / self.__item_height) + self.__boundary_relaxation_threshold,
                                self.__item_count - 1)
        return visible_start_index, visible_end_index

    def __delete_item_view_out_range(self, index_top, index_bottom):
        for index in list(self.__visible_items_index_mapping.keys()):
            if index < index_top or index >= index_bottom:
                try:
                    self.__visible_items_index_mapping[index].destroy()
                    self.__canvas.delete(self.__canvas_item_index_mapping[index])
                    del self.__visible_items_index_mapping[index]
                except Exception as e:
                    print('error index ', index, ' error info: ', e)

    def __update_visible_items(self, start_index, end_index):
        for index in range(start_index, end_index + 1):
            if index in self.__visible_items_index_mapping:
                self.__visible_items_index_mapping[index].update_view(self.__adapter.get_item(index))
                continue
            y = index * self.__item_height
            item_view = self.__adapter.create_item_view(self.__canvas, index)
            item_id = self.__canvas.create_window((0, y), window=item_view, anchor='nw')
            self.__canvas_item_index_mapping[index] = item_id
            self.__visible_items_index_mapping[index] = item_view

    def __check_update(self):
        if not self.__canvas.winfo_ismapped():
            return
        self.__invalidate_view()

    def update_item_view(self, index):
        if index == -1:
            self.__item_count = self.__adapter.get_count()
            self.__update_scroll_region()
            self.__invalidate_view()
            return
        visible_index_top, visible_index_bottom = self.__get_visible_items_index_range()
        if index < visible_index_top or index > visible_index_bottom:
            return
        self.__visible_items_index_mapping[index].update_view(self.__adapter.get_item(index))

    def set_data(self, data):
        self.__adapter.set_data(data)
        self.__item_count = len(data)
        self.__invalidate_view()

    def get_count(self):
        return self.__adapter.get_count()

    def get_item_view_id(self, index):
        return self.__adapter.get_item_id(index)

    def get_item(self, index):
        return self.__adapter.get_item(index)
