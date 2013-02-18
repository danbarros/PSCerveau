import numpy as np
import pylab as pl

def draw_bar(start, end, img_shape, thickness):

    start = np.asarray(start).ravel()
    end = np.asarray(end).ravel()
    
    grid=np.mgrid[0.:1.:1. / img_shape[0], 0.:1.:1. / img_shape[1]]
    grid=grid.reshape(2, -1)
    R = np.ones((2,2))
    R[:, 0] = end - start
    norm = np.sqrt(R[1][0]*R[1][0]+R[0][0]*R[0][0])
    R[0][1]=R[1][0]/norm
    R[1][1]=-R[0][0]/norm
    new_grid=np.dot(np.linalg.inv(R), np.subtract(grid,start[:, np.newaxis]))
    img=np.zeros(img_shape)
    img=((new_grid[0]>=0.)*(new_grid[0]<=1.)*(np.abs(new_grid[1])<=thickness/2)).reshape(img_shape).astype(np.float64)
    return img

def signatures_to_letter(signature, img_shape, thickness): 
	result = np.zeros(img_shape)
	signature = signature.ravel()
	if(signature[0]):
		result=result+draw_bar((0,0),(.5,0),img_shape, thickness) 
	if(signature[1]): 
		result=result+draw_bar((.5,0),(1,0),img_shape, thickness) 
	if(signature[2]): 
		result=result+draw_bar((0,.5),(.5,.5),img_shape, thickness) 
	if(signature[3]): 
		result=result+draw_bar((.5,.5),(1,.5),img_shape, thickness) 
	if(signature[4]): 
		result=result+draw_bar((0,1),(.5,1),img_shape, thickness) 
	if(signature[5]): 
		result=result+draw_bar((.5,1),(1,1),img_shape, thickness) 
	if(signature[6]): 
		result=result+draw_bar((0,0),(0,.5),img_shape, thickness) 
	if(signature[7]): 
		result=result+draw_bar((0,.5),(0,1),img_shape, thickness) 
	if(signature[8]): 
		result=result+draw_bar((.5,0),(.5,.5),img_shape, thickness) 
	if(signature[9]): 
		result=result+draw_bar((.5,.5),(.5,1),img_shape, thickness) 
	if(signature[10]): 
		result=result+draw_bar((1,0),(1,.5),img_shape, thickness) 
	if(signature[11]): 
		result=result+draw_bar((1,.5),(1,1),img_shape, thickness) 
	if(signature[12]): 
		result=result+draw_bar((0,0),(.5,.5),img_shape, thickness) 
	if(signature[13]): 
		result=result+draw_bar((0,1),(.5,.5),img_shape, thickness) 
	if(signature[14]): 
		result=result+draw_bar((1,0),(.5,.5),img_shape, thickness) 
	if(signature[15]): 
		result=result+draw_bar((1,1),(.5,.5),img_shape, thickness) 
	return result

#def signatures_to_words:
#	for m in N:
#		result=np.hstack((result,np.zeros(img_shape)))
#		if(m[0]):
#			result=result+draw_bar((0,0),(img_shape[0]/2,0),img_shape, thickness) 
#		if(m[1]): 
#			result=result+draw_bar((img_shape[0]/2,0),(img_shape[0],0),img_shape, thickness) 
#		if(m[2]): 
#			result=result+draw_bar((0,img_shape[1]/2),(img_shape[0]/2,img_shape[1]/2),img_shape, thickness) 
#		if(m[3]): 
#			result=result+draw_bar((img_shape[0]/2,img_shape[1]/2),(img_shape[0],img_shape[1]/2),img_shape, thickness) 
#		if(m[4]): 
#			result=result+draw_bar((0,img_shape[1]),(img_shape[0]/2,img_shape[1]),img_shape, thickness) 
#		if(m[5]): 
#			result=result+draw_bar((img_shape[0]/2,img_shape[1]),(img_shape[0],img_shape[1]),img_shape, thickness) 
#		if(m[6]): 
#			result=result+draw_bar((0,0),(0,img_shape[1]/2),img_shape, thickness) 
#		if(m[7]): 
#			result=result+draw_bar((0,img_shape[1]/2),(0,img_shape[1]),img_shape, thickness) 
#		if(m[8]): 
#			result=result+draw_bar((img_shape[0]/2,0),(img_shape[0]/2,img_shape[1]/2),img_shape, thickness) 
#		if(m[9]): 
#			result=result+draw_bar((img_shape[0]/2,img_shape[1]/2),(img_shape[0]/2,img_shape[1]),img_shape, thickness) 
#		if(m[10]): 
#			result=result+draw_bar((img_shape[0],0),(img_shape[0],img_shape[1]/2),img_shape, thickness) 
#		if(m[11]): 
#			result=result+draw_bar((img_shape[0],img_shape[1]/2),(img_shape[0],img_shape[1]),img_shape, thickness) 
#		if(m[12]): 
#			result=result+draw_bar((0,0),(img_shape[0]/2,img_shape[1]/2),img_shape, thickness) 
#		if(m[13]): 
#			result=result+draw_bar((0,img_shape[1]),(img_shape[0]/2,img_shape[1]/2),img_shape, thickness) 
#		if(m[14]): 
#			result=result+draw_bar((img_shape[0],0),(img_shape[0]/2,img_shape[1]/2),img_shape, thickness) 
#		if(m[15]): 
#			result=result+draw_bar((img_shape[0],img_shape[1]),(img_shape[0]/2,img_shape[1]/2),img_shape, thickness) 
#	return result
 
def char_to_signatures(S): 
	n=len(S) 
 	signature=np.zeros((n,16)) 
 	for i in np.arange(n): 
		if(S[i]=='A'): 
			signature[i]=[1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0] 
		elif(S[i]=='B'): 
			signature[i]=[0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0] 
		elif(S[i]=='C'): 
			signature[i]=[1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0] 
		elif(S[i]=='D'): 
			signature[i]=[0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0] 
		elif(S[i]=='E'): 
			signature[i]=[1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0] 
		elif(S[i]=='F'): 
			signature[i]=[1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0] 
		elif(S[i]=='G'): 
			signature[i]=[1,1,0,0,0,1,1,1,0,1,1,1,0,0,0,0] 
		elif(S[i]=='H'): 
			signature[i]=[1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0] 
		elif(S[i]=='I'): 
			signature[i]=[0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0] 
		elif(S[i]=='J'): 
			signature[i]=[0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0] 
		elif(S[i]=='K'): 
			signature[i]=[0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1] 
		elif(S[i]=='L'): 
			signature[i]=[1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0] 
		elif(S[i]=='M'): 
			signature[i]=[1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0] 
		elif(S[i]=='N'): 
			signature[i]=[1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1] 
		elif(S[i]=='O'): 
			signature[i]=[1,1,0,0,1,1,1,1,0,0,1,1,0,0,0,0] 
		elif(S[i]=='P'): 
			signature[i]=[1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0] 
		elif(S[i]=='Q'): 
			signature[i]=[1,0,0,0,1,0,1,1,1,1,0,0,0,0,0,1] 
		elif(S[i]=='R'): 
			signature[i]=[1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,1] 
		elif(S[i]=='S'): 
			signature[i]=[1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0] 
		elif(S[i]=='T'): 
			signature[i]=[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0] 
		elif(S[i]=='U'): 
			signature[i]=[1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0] 
		elif(S[i]=='V'): 
			signature[i]=[1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0] 
		elif(S[i]=='W'): 
			signature[i]=[1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1] 
		elif(S[i]=='X'): 
			signature[i]=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1] 
		elif(S[i]=='Y'): 
			signature[i]=[0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0] 
		elif(S[i]=='Z'): 
			signature[i]=[0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0] 
		else: 
			print"Probleme" 
	return signature


def test_signature():
	signature = np.array([1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0])
	display = signatures_to_letter(signature, (150,100), .1)
	display = np.minimum(display, 1)
	pl.figure()
	pl.imshow(display, interpolation="nearest")
	pl.gray()
	pl.show()

if __name__ == "__main__":
    display = signatures_to_letter(test_signature(), (150,100), .1)
    display = np.minimum(display, 1)
    pl.figure()
    pl.imshow(display, interpolation="nearest")
    pl.gray()
    pl.show()
