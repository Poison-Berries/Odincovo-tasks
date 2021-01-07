import os, pathlib
from random import randint

FLAG="PB{w3lL_u_found_GLaDOS}"

FLAG1="PB{Ap3rtur3 Sc13nc3 H@ndh3ld P0rt@l D3v1c3 s0 c00l}"
FLAG2="PB{p0tat03s_wi11_ki11_us!!!}"
FLAG3="PB{Turr3ts_@re_s0_cut3)))}"
FLAG4="PB{d1d_u_r3m3mb3r_cub3_c0mp@n1on?}"
FLAG5="PB{h3h_wh3r3_1s_B3tty?!}"
FLAG6="PB{R3fl3cti0n-G31}"
FLAG7="PB{0h_th3s3_e@ster_eggs_@r3_2_c0mpl1c@t#d}"
FLAG8="PB{0h_u_know?_it_quite_difficult to denerate this flags}"
FLAG9="Okay_just_random_stuff"

depth = 0
folder_depth = 3
FLAG_spawned = False

def create_path():
  global depth
  global folder_depth
  
  url = randint(1, 9)
  with open('FLAG','w') as f:
      f.write(eval('FLAG'+str(url)) + '\n')
  
  if(folder_depth > depth):
    os.makedirs("1Forward")
    os.chdir("1Forward")
    depth += 1
    create_path()
  else:
    depth -= 1
    os.chdir("..")
    return 0
    
  if(folder_depth > depth):
    os.makedirs("2Backward")
    os.chdir("2Backward")
    depth += 1
    create_path()
  else:
    depth -= 1
    os.chdir("..")
    return 0
  
  if(folder_depth > depth):
    os.makedirs("3Left")
    os.chdir("3Left")
    depth += 1
    create_path()
  else:
    depth -= 1
    os.chdir("..")
    return 0
  
  if(folder_depth > depth):
    os.makedirs("4Right")
    os.chdir("4Right")
    depth += 1
    create_path()
  else:
    depth -= 1
    os.chdir("..")
    return 0
  
  depth -= 1
  os.chdir("..")
  return 0

def spawn_FLAG():
  for i in range(0, folder_depth-1):
    path = randint(1, 5)
    
    if(path==1):
      os.chdir("1Forward")
    elif(path==2):
      os.chdir("2Backward")
    elif(path==3):
      os.chdir("3Left")
    elif(path==4):
      os.chdir("4Right")
    
    print(path)
  choice = randint(0, 1)
  
  if(choice == 0):
    with open('FLAG','w') as f:
      f.write(FLAG)
  else:
    path = randint(1, 5)
    
    if(path==1):
      os.chdir("1Forward")
    elif(path==2):
      os.chdir("2Backward")
    elif(path==3):
      os.chdir("3Left")
    elif(path==4):
      os.chdir("4Right")
    
    print(path)
    with open('FLAG','w') as f:
      f.write(FLAG + '\n')

os.makedirs("Test-ground")
os.chdir("Test-ground")
create_path()

os.chdir("Test-ground")
spawn_FLAG()
