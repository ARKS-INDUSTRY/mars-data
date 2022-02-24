import urllib.request
import requests
from tkinter import *
from tkinter.messagebox import *

api = "pIrdFhGHvCOBVwFYeOXvw5PFAxBAUZN2zyCPhPfY"
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers"
root = Tk()
root.title("Mars Mission")
root.geometry("550x600")
def mars_images(camera, rover, sol):
   url = f"{base_url}/{rover}/photos?sol={sol}&camera={camera}&api_key={api}"
   data = requests.get(url)
   data = data.json()
   img_list = data["photos"]
   img_url_list = []
   for i in range(len(img_list)):
      img_url = data["photos"][i]["img_src"]
      img_url_list.append(img_url)
   return img_url_list


def save_img(img_list):
   count = 0
   for i in img_list:
      count +=1
      filename = f"data/{count}.jpeg"
      urllib.request.urlretrieve(i, filename)

#imgl = mars_images("rhaz", "spirit","100")
#save_img(imgl)
heading = Label(root, text="Mars Mission! To the moon", font=("helvetica", 30))
heading.pack(pady=10)
def main_tab():
   main_frame = Frame(root)
   main_frame.pack()
   rover_list = ["opportunity", "curiosity", "spirit"]
   label_rover = Label(main_frame, text="Select rover: ")
   label_rover.pack(pady=10)
   default = StringVar()
   default.set("curiosity")
   cam_selection = OptionMenu(main_frame,default, *rover_list)
   cam_selection.pack(pady=10)
   sol_label = Label(main_frame, text="enter a proper sol of the rover: ")
   sol_label.pack(pady=10)
   sol_entry = Entry(main_frame, width=30)
   sol_entry.pack(pady=10)
   try:
      sol = int(sol_entry.get())
   except:
      showerror("Sol error", "Please enter numbers\n")
   rover = default.get()
   if rover == rover_list[0]:
      cam_list = ["FHAZ", "RHAZ", "MAST", "CHEMCAM",
                  "MAHLI", "MARDI", "NAVCAM"]
   elif rover == rover_list[1]:
      cam_list = ["FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"]
   else:
      cam_list = ["FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"]

root.mainloop()



