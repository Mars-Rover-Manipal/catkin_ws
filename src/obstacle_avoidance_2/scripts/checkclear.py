import rospy 
import numpy as np
from sensor_msgs.msgs import Imu
from tf.transformations import euler_from_quaternion
#needs to ne tuned
clear_thresh=2
def diff(op1,op2,start,end):
	sin_comps= op1*sines[start:end]-op2*sines[start:end]
	cos_comps=op1*coses[start:end]-op2*coses[start:end]
	mag=(np.sum(sin_comps)**2+np.sum(cos_comps))**0.5
	return mag

def check_clear(cardiod):
	#47.5 degrees on both sides 
	arr_len=len(cardiod)
	limit_ind=int(47.5*arr_len/275)
	b1_cheek=cardiod[0:limit_ind]
	b2_cheek=cardiod[arr_len-limit_ind:arr_len]
	#ori_card=original cardio
	d1=diff(ori_card[0:limit_ind],b1_cheek,0,limit_ind)
	d2=diff(ori_card[arr_len-limit_ind:arr_len],b2_cheek,arr_len-limit_ind,arr_len)
	if(d1<clear_thresh and d2<clear_thresh):
		return True
	return False