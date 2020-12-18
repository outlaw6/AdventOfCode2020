def drawRectangle(h,w,c='o'):
	# Draw a Rectangle
	# with given dimensins and specified character
	# c = 'char'
	for times in range(h):
		print(str(c) * w)


if __name__ == '__main__':

	print(drawRectangle(3,4,'x'))
	drawRectangle(10,10,)