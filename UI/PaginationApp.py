import logging
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


class PaginationApp:
    def __init__(self, items, page_size=5):
        self.items = items
        self.page_size = page_size
        self.current_page = 1
        self.treeview = []

    # self.page_buttons = []
    # self.update_treeview()

    def update_treeview(self):
        self.treeview.clear()
        itemsLen = len(self.items)
        if (self.page_size > itemsLen):
            # it will get all the items.
            self.page_size = itemsLen
            self.current_page = 1
        # Get items for the current page
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        if end_index > itemsLen:
            end_index = itemsLen
        if (start_index >= itemsLen or end_index > itemsLen or
                start_index < 0 or end_index < 0):
            print("start index", start_index)
            print("end index", end_index)
            print("current page", self.current_page)
            print("page size", self.page_size)
            raise Exception("Error in requested page and or is size.")
        self.treeview = self.items[start_index:end_index]

    def goto_page(self, page_number, page_size):
        self.current_page = page_number
        self.page_size = page_size
        self.update_treeview()
        return self.treeview

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_treeview()
        return self.treeview

    def next_page(self):
        # Ceiling division
        max_pages = -(-len(self.items) // self.page_size)
        if self.current_page < max_pages:
            self.current_page += 1
            self.update_treeview()
        return self.treeview
