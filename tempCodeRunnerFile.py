y = self.msg_box()
        self.trigger = 0 #used later for differentiating the the final pages for these options
        if y=="yes":
            self.destroy_window()
            self.main_screen_3()
        else:
            print("No")