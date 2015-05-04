#coding:utf-8
import urllib2
import re

def copy(url, rep):
	req = urllib2.Request(url)   
	content = urllib2.urlopen(req, timeout=15).read()
	pattern = re.compile(rep)
	this = pattern.findall(content)
	return this
	
if __name__ == '__main__':
	host = 'http://s.hc360.com/?w=%BA%DA%C1%FA%BD%AD&mc=enterprise'
	f = open('a.txt','a')
	i=0
	for x in xrange(1,500):
		try:
			print x
			message = copy(host+'&e='+str(x), r'<h3><a data-exposurelog="([^"]+)"')
			for x in message:
				x = 'http://' + x + '.b2b.hc360.com/shop/company.html'
				m = copy(x, r'<title>([^\<]+)</title>')
				print str(i)+' '+m[0]
				if len(m[0]) == 18:
					continue
				pattern = re.compile(r'([\d]+)')
				this = pattern.findall(m[0])
				if this:
					pass
				else:
					continue
				i=i+1
				try:
					f.write(x+' '+m[0])
					f.write('\n')
				except IOError:
					print 'IOError'
					f = open('a.txt','a')
				else:
					pass
			
		except Exception, e:
			continue
	f.close()
		