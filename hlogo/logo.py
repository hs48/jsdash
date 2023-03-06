import os
def logo(thickness=4):
	c = "H"
	s = "<html lang='en'><head> <script src='{{url_for('static', filename='/about/about.js')}}' type='module'></script></head><body>"
	for i in range(thickness):
		s+= "<pre>" + (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)+"</pre>"
	for i in range(thickness+1):
		s+="<pre>" + (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)+"</pre>"
	for i in range((thickness+1)//2):
		s+= "<pre>" + (c*thickness*5).center(thickness*6)+"</pre>"
	for i in range(thickness+1):
		s+= "<pre>" + (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)+"</pre>"
	for i in range(thickness):
		s+= "<pre>" + ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)+"</pre>"
	
	ending= "<br><h2 id='about'>The about page <br></h2><div id='H_logo'> {s}</div></body></html>"
	s+=ending
	#parent_dir = os.path.dirname(os.getcwd())
	#tem_path = os.path.join(parent_dir, '/templates/about.html')
	tem_path = r'C:\Users\Bonzo\anaconda3\envs\analysis\templates\about.html'
	with open(tem_path, 'w') as fp:
		fp.write(s)