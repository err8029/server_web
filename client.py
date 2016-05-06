import requests
import sys

class Service():

    def __init__(self,url):
        self.url = url

    def get(self, resource):
	resp = requests.get(self.url+"/"+resource)
        if resp.status_code != 200:
            raise Exception('GET /tasks/ %s' % (resp.status_code))
	return resp.json()

    def getn(self,resource,n):
	return self.get(resource)[:n]

    def post(self,input_data,resource):
        post_content = requests.post(self.url+"/"+resource,data=input_data)
        if post_content.status_code != 201:
            raise Exception('POST /tasks/ %s' % (post_content.status_code))
        if post_content.status_code == 201:
            print "uploaded correctly"
      



if __name__ == "__main__":

    
    newservice=Service("http://jsonplaceholder.typicode.com")
    resources = ["posts","comments"]
    for r in resources:
    	data=newservice.get(r)
    print data

    input_data = {
            "userId": sys.argv[1],
            "id": sys.argv[2],
            "title": sys.argv[3],
            "body": sys.argv[4]
    }
    newservice.post(input_data,"posts")

