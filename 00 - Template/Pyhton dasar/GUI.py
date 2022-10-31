# membuat window
import tkinter # GUI python (make 1)
main_window = tkinter.Tk() # (make 2)
# main_window.mainloop() # akan memunculkan window / tkinter 

# fungsi
def event_tekan():
    label2 = tkinter.Label(main_window, text="aku ditekan ^_^")
    label2.pack()


label = tkinter.Label(main_window, text="halo, saya adalah \n GUI sederhana dengan \n menggunakan python")
tombol = tkinter.Button(main_window, text="tekan akuh", command = event_tekan)

label.pack() # akan menampilkan tulisan
tombol.pack() # akan menampilkan tombol
main_window.mainloop() # akan memunculkan window (make 3)