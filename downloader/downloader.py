from shutil import copy
q_1 = input("Write the path to the place you want to install Paint App v5.6. Add \ to the end of the path.")
q_1_a = q_1
q_2 = input("Write the path to the place you want to save images to. Include \ at the end of the path.")
i_s_p = q_2
d = input("Write the path to the Paint App v5.6 downloader. Dont add \ to the end of the path.")
d_n = d
info = open("info.TXT","w")
info.write(f"{q_1_a}\n")#Paint App path
info.write(f"{i_s_p}\n")#save image path
info.write(f"{d_n}\n")#path to where the downloader is or was if they deleted it doesent really matter
copy(d_n,i_s_p), exit()



