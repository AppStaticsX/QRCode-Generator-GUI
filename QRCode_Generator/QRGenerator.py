from PIL import Image, ImageTk
import customtkinter as ctk
import qrcode

qr = qrcode.QRCode(version=40)

SMALL_FONT_STYLE = ("Ubuntu Mono", 14, "bold")
DEFAULT_FONT_STYLE = ("Freeman", 14)
TOP_LABLE_FONT_STYLE = ("Anton", 16, "bold")

PURE_DARK = "#000000"
LABEL_COLOR = "#FFFFFF"
WARN_COLOR = "#FF0000"
BORDER_COLOR = "#919191"
BTN_HOVER = "#919191"


#set appearance of application
ctk.set_appearance_mode("dark")


#load images from "ImageResources" folder
bold_image = ctk.CTkImage(Image.open("ImageResources\\bold.png"), size=(20,20))
italic_image = ctk.CTkImage(Image.open("ImageResources\\italic.png"), size=(20,20))
upper_image = ctk.CTkImage(Image.open("ImageResources\\upper.png"), size=(20,20))
lower_image = ctk.CTkImage(Image.open("ImageResources\\lower.png"), size=(20,20))
underline_image = ctk.CTkImage(Image.open("ImageResources\\underline.png"), size=(20,20))
strike_image = ctk.CTkImage(Image.open("ImageResources\\strikethrough.png"), size=(20,20))
delete_image = ctk.CTkImage(Image.open("ImageResources\\del.png"), size=(20,20))
generate_image = ctk.CTkImage(Image.open("ImageResources\\gen.png"), size=(20,20))
save_image = ctk.CTkImage(Image.open("ImageResources\\save.png"), size=(20,20))


#create class and customize the app window
class QRGenerator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("400x680")
        self.window.resizable(False, False)
        self.window.title("AppStaticsX™-QRGenerator")
        self.window.iconbitmap(r'ImageResources\\icon.ico')


        #design user interface using module called "customtkinter"
        self.top_frame = ctk.CTkFrame(self.window, width=400, fg_color="transparent")
        self.top_frame.pack()

        logo = Image.open("ImageResources\\logo.png").resize((48,48)) 
        self.logo = ImageTk.PhotoImage(logo)
        self.logo_label = ctk.CTkLabel(self.top_frame, image=self.logo, fg_color="transparent", text="")
        self.logo_label.pack(fill="x", side="left", pady =10, padx=10)

        self.app_name = ctk.CTkLabel(self.top_frame, text="QR Generator", text_color=LABEL_COLOR, font=TOP_LABLE_FONT_STYLE)
        self.app_name.pack(side="right", padx=10)

        self.empty_frame = ctk.CTkFrame(self.window, width=400, height=10, fg_color="transparent")
        self.empty_frame.pack(pady=5)

        self.btn_frame = ctk.CTkFrame(self.window, width=350, height=300, corner_radius=5, border_color=BORDER_COLOR)
        self.btn_frame.pack()

        self.btn_upper = ctk.CTkButton(self.btn_frame, height=30, width=30, image=upper_image, text="", fg_color="transparent", hover_color=BTN_HOVER, command=self.uppercase)
        self.btn_upper.pack(side="left", padx=2, pady=2)

        self.btn_lower = ctk.CTkButton(self.btn_frame, height=30, width=30, image=lower_image, text="", fg_color="transparent", hover_color=BTN_HOVER, command=self.lowercase)
        self.btn_lower.pack(side="left", padx=2, pady=2)

        self.btn_bold = ctk.CTkButton(self.btn_frame, height=30, width=30, image=bold_image, text="", fg_color="transparent", hover_color=BTN_HOVER)
        self.btn_bold.pack(side="left", padx=2, pady=2)

        self.btn_italic = ctk.CTkButton(self.btn_frame, height=30, width=30, image=italic_image, text="", fg_color="transparent", hover_color=BTN_HOVER)
        self.btn_italic.pack(side="left", padx=2, pady=2)

        self.btn_underline = ctk.CTkButton(self.btn_frame, height=30, width=30, image=underline_image, text="", fg_color="transparent", hover_color=BTN_HOVER, command=self.underline)
        self.btn_underline.pack(side="left", padx=2, pady=2)

        self.btn_strike = ctk.CTkButton(self.btn_frame, height=30, width=30, image=strike_image, text="", fg_color="transparent", hover_color=BTN_HOVER, command=self.strikethrough)
        self.btn_strike.pack(side="left", padx=2, pady=2)

        self.btn_delete = ctk.CTkButton(self.btn_frame, height=30, width=30, image=delete_image, text="", fg_color="transparent", hover_color=WARN_COLOR, command=self.clear_txt_box)
        self.btn_delete.pack(side="left", padx=20, pady=2)

        self.text_frame = ctk.CTkFrame(self.window, width=350, height=300, corner_radius=5, border_color=BORDER_COLOR)
        self.text_frame.pack(pady=0)

        self.txt_box = ctk.CTkTextbox(self.text_frame, width=325, height=100, text_color=LABEL_COLOR, font=SMALL_FONT_STYLE)
        self.txt_box.pack( pady=10, fill="both", side="top", padx=10)

        self.option_frame = ctk.CTkFrame(self.window, width=350, corner_radius=5, border_color=BORDER_COLOR, fg_color="transparent")
        self.option_frame.pack(pady=10)

        self.name_entry = ctk.CTkEntry(self.option_frame, width=180, height=30, placeholder_text="Enter QR Name", font=SMALL_FONT_STYLE)
        self.name_entry.pack(side="left", padx=20)

        self.btn_update = ctk.CTkButton(self.option_frame, height=30, width=100, image=generate_image, text="GENERATE", text_color=LABEL_COLOR, fg_color="#23ACEF", hover_color=BTN_HOVER, font=DEFAULT_FONT_STYLE, command=self.update_qr_to_qr_lable)
        self.btn_update.pack(side="left", padx=20, pady=2)

        self.qr_frame = ctk.CTkFrame(self.window, width=400, corner_radius=15, border_color=BORDER_COLOR)
        self.qr_frame.pack(pady=10)

        qr_img = Image.open("ImageResources\\logo.png").resize((350,350)) 
        self.qr = ImageTk.PhotoImage(qr_img)
        self.qr_label = ctk.CTkLabel(self.qr_frame, image=self.qr, fg_color="transparent", text="")
        self.qr_label.pack(fill="x", pady =15, padx=30)

        self.btn_save = ctk.CTkButton(self.qr_frame, height=30, width=120, image=save_image, text="SAVE AS PNG", text_color=LABEL_COLOR, fg_color="#0E8849", hover_color=BTN_HOVER, font=DEFAULT_FONT_STYLE, command=self.save_qr)
        self.btn_save.pack_forget()


    #handle save button
    def save_qr(self):
         text = self.txt_box.get("1.0", "end-1c")  # Retrieve all text from the textbox
         qrname = self.name_entry.get()
    
         if not qrname:
          self.name_entry.configure(placeholder_text="*Enter QR Name", placeholder_text_color=WARN_COLOR)
          return
    
         myqr = qrcode.make(text)
         myqr.save(qrname + ".png")


    #handle clear button
    def clear_txt_box(self):
       if self.txt_box.get("1.0", "end-1c") != "":
          self.txt_box.delete("1.0", "end-1c")


    
    #handle generate button
    def update_qr_to_qr_lable(self):
        text = self.txt_box.get("1.0", "end-1c")

        qrname = self.name_entry.get()

        if not qrname:
          self.name_entry.configure(placeholder_text="Please Name Your QRCode", placeholder_text_color=WARN_COLOR)
          return
    
    # Generate QR code
        qr = qrcode.make(text)
            
            # Resize QR code image to fit the label
        qr = qr.resize((350, 350))
            
            # Convert QR code image to PhotoImage
        qr_image = ImageTk.PhotoImage(qr)
    
    # Update QR image in the label
        self.qr_label.configure(image=qr_image)
        self.qr_label.image = qr_image  # Keep a reference to prevent garbage collection
    
    # Show the save button
        self.btn_save.pack(padx=20, pady=10)
    # Keep a reference to prevent garbage collection


    #handle uppercase button
    def uppercase(self):
        # Get the selected text in the textbox
        start_index = self.txt_box.index("sel.first")
        end_index = self.txt_box.index("sel.last")
        selected_text = self.txt_box.get(start_index, end_index)

        # Check if there is any selected text
        if selected_text:
            # Convert the selected text to uppercase
            upper_text = selected_text.upper()

            # Replace the selected text with the uppercase text
            self.txt_box.delete(start_index, end_index)
            self.txt_box.insert(start_index, upper_text)


     #handle lowercase button
    def lowercase(self):
        # Get the selected text in the textbox
        start_index = self.txt_box.index("sel.first")
        end_index = self.txt_box.index("sel.last")
        selected_text = self.txt_box.get(start_index, end_index)

        # Check if there is any selected text
        if selected_text:
            # Convert the selected text to uppercase
            lower_text = selected_text.lower()

            # Replace the selected text with the uppercase text
            self.txt_box.delete(start_index, end_index)
            self.txt_box.insert(start_index, lower_text)


    #handle italic button (not working properly)
    def italic(self):
    # Get the selected text in the textbox
     start_index = self.txt_box.index("sel.first")
     end_index = self.txt_box.index("sel.last")
    
    # Apply italic font to the selected text
     self.txt_box.tag_add("italic", start_index, end_index)
     self.txt_box.tag_config("italic", font=("Arial", 12, "italic"))


    #handle underline button
    def underline(self):
        # Get the selected text in the textbox
        start_index = self.txt_box.index("sel.first")
        end_index = self.txt_box.index("sel.last")
        
        # Apply underline to the selected text
        self.txt_box.tag_add("underline", start_index, end_index)
        self.txt_box.tag_config("underline", underline=True)

    #handle strikethrough button
    def strikethrough(self):
        # Get the selected text in the textbox
        start_index = self.txt_box.index("sel.first")
        end_index = self.txt_box.index("sel.last")
        
        # Apply strikethrough to the selected text
        self.txt_box.tag_add("strikethrough", start_index, end_index)
        self.txt_box.tag_config("strikethrough", overstrike=True)


    def bold(self):
        # Get the selected text in the textbox
        start_index = self.txt_box.index("sel.first")
        end_index = self.txt_box.index("sel.last")
        
        # Apply bold font to the selected text
        self.txt_box.tag_add("bold", start_index, end_index)
        self.txt_box.tag_config("bold", bold=True)
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    qrg = QRGenerator()
    qrg.run()