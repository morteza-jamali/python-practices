# Source Link : https://edabit.com/challenge/3Ekam9jvbNKHDtx4K
# Level : Medium

import math

def line_length(f_point , s_point):
  delta_x = s_point[0] - f_point[0]
  delta_y = s_point[1] - f_point[1]

  return round(math.sqrt(delta_x**2 + delta_y**2) , 2)