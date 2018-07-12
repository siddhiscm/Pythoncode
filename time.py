import time
localtime = time.asctime( time.localtime(time.time()) )
print "current time :", localtime
time.sleep(5)
while (time>60):
	localtime = time.asctime( time.localtime(time.time()) )
	print "current time :", localtime
	print "i am waiting 5 sec"
	
