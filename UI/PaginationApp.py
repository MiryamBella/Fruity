import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

class PaginationApp:
	def __init__(self, items, page_size):
		self.items = items
		self.page_size = page_size
		self.current_page = 1
		self.treeview = []
		self.page_buttons = []
		self.update_treeview()

	def update_treeview(self):
		self.treeview.clear()
		# Get items for the current page
		start_index = (self.current_page - 1) * self.page_size
		end_index = start_index + self.page_size
		#current_page_items
		self.treeview = self.items[start_index:end_index]

		# # Insert items into the treeview
		# for item in current_page_items:
		# 	self.treeview.append(item)

	# def create_pagination_buttons(self):
	# 	max_pages = -(-len(self.items) // self.page_size) # Ceiling division
	#
	# 	for page_number in range(1, max_pages + 1):
	# 		button = ttk.Button(self.master, text=str(page_number),
	# 					command=lambda num=page_number: self.goto_page(num))
	# 		button.pack(side=tk.LEFT, padx=5)
	# 		self.page_buttons.append(button)
	#
	# 	self.highlight_current_page()

	def goto_page(self, page_number, page_size):
		self.current_page = page_number
		self.page_size = page_size
		self.update_treeview()
		return self.treeview

	def prev_page(self):
		if self.current_page > 1:
			self.current_page -= 1
			self.update_treeview()

	def next_page(self):
		# Ceiling division
		max_pages = -(-len(self.items) // self.page_size)
		if self.current_page < max_pages:
			self.current_page += 1
			self.update_treeview()

# # Example usage
# root = tk.Tk()
#
# # Create a list of numbers from 1 to 100
# all_numbers = list(range(1, 101))
#
# # Set the number of items per page
# page_size = 10
# app = PaginationApp(root, all_numbers, page_size)
#
# root.mainloop()
