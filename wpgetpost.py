import requests
import datetime

def swaphtml(intext):
     outtext = intext.replace('&#8217;',"'")
     outtext = outtext.replace('&#8230;',"...")
     outtext = outtext.replace('&#8220;','"')
     outtext = outtext.replace('&#8221;','"')
     return outtext

response = requests.get('https://drewfowler.com/wp-json/wp/v2/posts/?categories=8')
posts = response.json()

for post in posts:
	postdt = datetime.datetime.strptime(post.get('date'), '%Y-%m-%dT%H:%M:%S')
	print('Post title:',swaphtml(post.get('title').get('rendered')))
	print('Post date:',postdt)
	print('Post content:', swaphtml(post.get('content').get('rendered')))
