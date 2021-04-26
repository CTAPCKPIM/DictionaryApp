#-*-coding:cp1251-*-

import tkinter as tk

class Dictionary():
    def __init__ (self):
        self.root = tk.Tk()
        self.root['bg'] = 'green3'
        self.root.title('Dictionary')
        self.font = ("Terminal 16 bold") # main < FONT >
        self.font_two = ("Terminal 26 bold") # word < FONT >
        self.root.geometry('700x354')
        #FRAMES
        self.frame_one = tk.Frame (self.root, bg = 'black', width = 700, height = 200) # creat < FRAME ONE >
        self.frame_two = tk.Frame (self.root, bg = 'black', width = 700, height = 100) # creat < FRAME TWO >
        self.frame_three = tk.Frame (self.root, bg = 'black', width = 700, height = 50) # creat < FRAME THREE >
        #WIDGETS
        self.label_name = tk.Label(self.frame_one, text = "Find / Add word..", bg = 'black', fg = 'green3', font = self.font) # creat < MAIN LABEL>
        self.word = tk.Label(self.frame_two, text = "_ _ _ _ _ _", bg = 'black', fg = 'green3', font = self.font_two) # for < WORDS >
        self.num_word = tk.Label (self.frame_two, text = "", bg = 'black', fg = 'green3', font = self.font_two)
        self.sum = tk.Label (self.frame_two, text = ":", bg = 'black', fg = 'green3', font = self.font_two)
        self.input_win = tk.Entry (self.frame_one, bg = 'green3', width = 35, fg = 'black', font = self.font) # creat < ENTRY WIND...>
        self.search = tk.Button (self.frame_one, text = "Search", font = self.font, bg = 'black', fg = 'green3', activebackground = 'green3',
                                     activeforeground = 'black', width = 8, command = self.search) # butt < SERACH >!!!
        self.clear = tk.Button (self.frame_one, text = "Clear", font = self.font, bg = 'black', fg = 'green3', activebackground = 'green3',
                                     activeforeground = 'black', width = 8, command = self.clear) # butt < CLEAR >
        self.show = tk.Button (self.frame_three, text = "Show all", font = self.font, bg = 'black', fg = 'green3', activebackground = 'green3',
                                     activeforeground = 'black', width = 8, command = self.root_second) # butt < SHOW ALL >
        self.main_close = tk.Button (self.frame_three, text = 'X', font = self.font, bg = 'black', fg = 'green3', activebackground = 'green3',
                                          activeforeground = 'black', command =  self.root.destroy)

        
        self.frame_one.pack() #pack < FARME ONE >
        self.label_name.place(x = 259, y = 35) # pack < MAIN LABEL>
        self.input_win.place(x = 159, y = 85) # pack <INPUT WIND...>
        self.search.place( x = 222, y = 140) # pack butt < SERACH >
        self.clear.place( x = 382, y = 140) # pack butt < CLEAR >
            
        self.frame_two.pack(pady = 2) #pack < FARME TWO >
        self.word.place(x = 315, y = 30)  # pack label  < WORDS >
        self.num_word.place(x = 225, y = 30)
        self.sum.place(x = 280, y = 30)
            
        self.frame_three.pack() #pack < FARME THREE >
        self.show.place(x = 300, y = 10)# pack butt < SHOW ALL >
        self.main_close.place(x = 660, y = 10)
        

    def search (self):
        
        try:
            self.show['state'] = 'normal'
            self.us_word = self.input_win.get() #output < ENTRY >
            self.us_word_list = self.us_word.split()
            
            with open('Dictionary.txt', 'r+') as self.file:#
                self.found = self.file.read()
                for self.i in self.us_word_list:
                    if self.i in self.found: 
                        self.word['text'] = self.us_word
            
                '''
                if self.us_word in self.found: #self.us_word
                    #for self.i in self.us_word_list:
                        #print('\nelement: ', self.us_word, '\n======\n')
                        self.word['text'] = self.us_word
                 '''
                 
                
                if self.i not in self.found: # creat < MINI-WINDOW ONE>  
                    self.mini_win = tk.Tk()
                    self.mini_win['bg'] = 'black'
                    self.mini_win.geometry("330x130+380+300")
                    self.mini_win.title('Question')
                    self.inform = tk.Label (self.mini_win, text = "Word not found, want to add?", font = self.font, bg = 'black', fg = 'green3')
                    self.butt_yes = tk.Button (self.mini_win, text = "Yes", font = self.font, bg = 'black', fg = 'green3', width = 3, command = self.ok)
                    self.butt_no = tk.Button (self.mini_win, text = "No", font = self.font, bg = 'black', fg = 'green3', width = 3, command = self.mini_win.destroy)
                    #PACKS
                    self.inform.place(x = 9, y = 25)
                    self.butt_yes.place(x = 115, y = 70)
                    self.butt_no.place(x = 180, y = 70)
        except AttributeError:
            self.word['text'] = "Nothing.."
        '''
        self.show['state'] = 'normal'
        self.us_word = self.input_win.get() #output < ENTRY >
        self.us_word_list = self.us_word.split()
            
        with open('Dictionary.txt', 'r+') as self.file:#
            self.found = self.file.read()
            for self.i in self.us_word_list:
                if self.i in self.found: 
                    self.word['text'] = self.us_word
                    
                
                if self.us_word in self.found: #self.us_word
                    #for self.i in self.us_word_list:
                        #print('\nelement: ', self.us_word, '\n======\n')
                        self.word['text'] = self.us_word
                 
                
                
            if self.i not in self.found: # creat < MINI-WINDOW ONE>  
                self.mini_win = tk.Tk()
                self.mini_win['bg'] = 'black'
                self.mini_win.geometry("330x130+380+300")
                self.mini_win.title('Question')
                self.inform = tk.Label (self.mini_win, text = "Word not found, want to add?", font = self.font, bg = 'black', fg = 'green3')
                self.butt_yes = tk.Button (self.mini_win, text = "Yes", font = self.font, bg = 'black', fg = 'green3', width = 3, command = self.ok)
                self.butt_no = tk.Button (self.mini_win, text = "No", font = self.font, bg = 'black', fg = 'green3', width = 3, command = self.mini_win.destroy)
                    #PACKS
                self.inform.place(x = 9, y = 25)
                self.butt_yes.place(x = 115, y = 70)
                self.butt_no.place(x = 180, y = 70)
            '''
        
                   
    def ok(self):
        with open('Dictionary.txt', 'r') as self.file:# open < FILE for READ >
            self.found_el = self.file.read()
            for i in self.us_word_list:
                with open('Dictionary.txt', 'a') as self.file: # open < FILE for WRITE >
                    if i not in self.found_el:
                        self.file.write(i + '\n') # < WRITE >
                        self.word['text'] = self.us_word
        self.mini_win.destroy()
                #print(" | ", self.us_word) # !!!
                #self.num_word['text'] = self.ind_two
        
    def clear (self):
        self.input_win.delete(0, 'end') # clear < ENTRY >

    def root_second (self): # creat < WINDOW >
        self.show['state'] = 'disabled'
        self.root_words = tk.Tk()
        self.root_words['bg'] = 'green3'
        self.root_words.title("All words")
        self.root_words.geometry("800x550")
        font = ("Terminal 16 bold") # main < FONT >
        font_two = ("Terminal 24 bold") # word < FONT >
        #FRAMES
        self.frame_two_one= tk.Frame (self.root_words, bg = 'black', width = 800, height = 500) # frame on <SECOND WIND>
        self.frame_two_two= tk.Frame (self.root_words, bg = 'black', width = 800, height = 50) # frame on <SECOND WIND>
        #WITGETS
        self.del_all = tk.Button (self.frame_two_two, text = 'Delete all', font = font, bg = 'black', fg = 'green3', activebackground = 'green3',
                                          activeforeground = 'black', command = self.dell_all_words) # delete < all words >
        self.close = tk.Button (self.frame_two_two, text = 'X', font = font, bg = 'black', fg = 'green3', activebackground = 'green3',
                                          activeforeground = 'black', command =  self.close_sec_win) # destroy < WIND >
        self.scrollbar = tk.Scrollbar(self.frame_two_one) # creat < SCROLL BAR >
        self.wind_list = tk.Listbox (self.frame_two_one, bg = 'black', fg = 'green3', width = 130, height = 26, yscrollcommand = self.scrollbar.set,
                                     font = self.font, selectbackground = 'green3', selectforeground = 'black') # cr.<LISTBOX>
        def read_file():
            with open('Dictionary.txt', 'r') as self.file: # < OPEN >
                for i in self.file: # read < ALL WORDS in FILE >
                    self.wind_list.insert('end', i) # output in < SECOND WINDOW >
        read_file()
        #PACKS
        self.frame_two_one.pack(pady = 2)
        self.wind_list.pack(side='left', fill='both')
        self.scrollbar.pack(side = 'right', fill = 'y')
        self.frame_two_two.pack()
        self.del_all.place(x = 340, y = 8)
        self.close.place(x = 760, y = 8)

    def close_sec_win (self):
        self.root_words.destroy()
        self.show['state'] = 'normal'

    def dell_all_words (self): # open < MINI-WINDOW TWO >
        self.file = open('Dictionary.txt', 'w')
        self.mini_win_2 = tk.Tk()
        self.mini_win_2['bg'] = 'black'
        self.mini_win_2.geometry("330x130+380+300")
        self.mini_win_2.title('Message')
        self.inform_ = tk.Label (self.mini_win_2, text = "All words have been erased,", font = self.font,
                                 bg = 'black', fg = 'green3').place(x = 14, y = 25)
        self.inform_2 = tk.Label (self.mini_win_2, text = "please re-enter.", font = self.font,
                                 bg = 'black', fg = 'green3').place(x = 69, y = 50)
        self.butt_OK = tk.Button (self.mini_win_2, text = "Okey", font = self.font, bg = 'black', fg = 'green3', width = 5,
                                  command = self.close_menu_words).place(x = 135, y = 85)
        self.word['text'] = "_ _ _ _ _ _"
        self.input_win.delete(0, 'end') # clear < ENTRY >
        self.file.close()

    def close_menu_words (self):
        self.show['state'] = 'normal'
        self.mini_win_2.destroy()
        self.root_words.destroy()


    def __call__ (self):
        tk.mainloop()

App = Dictionary()()
App

if __name__ == '__main__':
    print("DictionaryApp.py")
