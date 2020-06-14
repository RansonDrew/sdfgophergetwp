import requests
import datetime
import textwrap

def swaphtml(intext):
     outtext = intext.replace('&#8217;',"'")
     outtext = outtext.replace('&#8230;',"...")
     outtext = outtext.replace('&#8220;','"')
     outtext = outtext.replace('&#8221;','"')
     outtext = outtext.replace('<p>','')
     outtext = outtext.replace('</p>','')
     return outtext

def fmttextpost(intext,txtwidth):
     orgparatext = intext.splitlines(keepends=True)
     newtxt = []
     for graf in orgparatext:
          graf = swaphtml(graf)
          graf = textwrap.fill(graf,txtwidth)
          newtxt.append(graf)
     a = '\n'
     finaltxt = a.join(newtxt)
     return finaltxt

def getwpposts():
     response = requests.get('https://drewfowler.com/wp-json/wp/v2/posts/?categories=8')
     posts = response.json()
     return posts

def printwpposts(wpposts):
     for wppost in wpposts:
	     postdt = datetime.datetime.strptime(wppost.get('date'), '%Y-%m-%dT%H:%M:%S')
	     print('Post title:',swaphtml(wppost.get('title').get('rendered')))
	     print('Post date:',postdt)
	     print('Post content:', swaphtml(wppost.get('content').get('rendered')))

myPosts = getwpposts()
printwpposts(myPosts)
