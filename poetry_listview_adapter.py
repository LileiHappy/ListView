"""
@Project : ListView
@File    : poetry_listview_adapter.py
@IDE     : PyCharm
@Author  : libai
@Email   : stayhungrystayfoolish52@gmail.com
@Date    : 2024/8/11 11:11 PM
"""

from base_listview_adapter import BaseListViewAdapter
from poetry_listview_item_view import PoetryListViewItemView


class PoetryListViewAdapter(BaseListViewAdapter):
    def __init__(self, item_width, item_height, data: [any] = None):
        self.__width = item_width
        self.__item_height = item_height
        self.__data = data
        self.__data_changed_notifier = None

    def __notify_data_changed(self, index=-1):
        if self.__data_changed_notifier:
            self.__data_changed_notifier(index)

    def set_data_changed_notifier(self, data_changed_notifier):
        self.__data_changed_notifier = data_changed_notifier

    def set_data(self, data):
        self.__data = data
        self.__notify_data_changed()

    def get_data(self):
        return self.__data

    def add_item(self, item):
        self.__data.append(item)
        self.__notify_data_changed(len(self.__data) - 1)

    def add_items(self, item_list):
        self.__data.extend(item_list)
        self.__notify_data_changed()

    def remove(self, index):
        self.__data.remove(index)
        self.__notify_data_changed()

    def clear(self):
        self.__data.clear()
        self.__notify_data_changed()

    def get_count(self):
        return len(self.__data)

    def get_item(self, index):
        return self.__data[index]

    def get_item_height(self, index):
        return self.__item_height

    def get_item_view_id(self, index):
        return index

    def create_item_view(self, container_view, index):
        music = self.__data[index]
        item_view = PoetryListViewItemView(container_view, music, width=self.__width, height=self.__item_height)
        item_view.pack_propagate(True)
        item_view.pack()
        return item_view

    def update_view(self, index):
        self.__notify_data_changed(index)

    def update(self):
        self.__notify_data_changed()
