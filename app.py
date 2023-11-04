from flask import Flask, render_template, request, redirect, url_for
from googlesearch import search
from pygooglenews import GoogleNews
from youtubesearchpython import VideosSearch

app = Flask(__name__)

# Google Request get router
@app.route('/')
def home():
    return render_template('home.html')

# Google request post router
@app.route('/',methods=['POST'])
def googleResult():
    result=[]
    if request.method == 'POST':
        query=request.form['query']
        for i in search(query,num_results=5,lang='en',proxy=None,advanced=False,sleep_interval=0,timeout=5,):
            result.append(i)
        print(result)
    return render_template("home.html",result=result)

# About route page
@app.route('/about')
def about():
    return render_template('about.html')

# Search in youtube
@app.route('/youtube')
def youtubeRoute():
    return render_template("youtube.html")

# Youtube POST route
@app.route('/youtube',methods=['POST'])
def youtubeResult():
    result=[]
    if request.method == 'POST':
        query=request.form['query']
        search = VideosSearch('NoCopyrightSounds')
        s=search.result()['result']
        for item in s:
            story={
                'title': item['title'],
                'link': item['link']
            }
            result.append(story)
    return render_template("youtube.html",result=result)


# News GET route
@app.route('/news')
def newRoute():
    return render_template('news.html')

# News POST route
@app.route('/news',methods=['POST'])
def googleNewsResult():
    result=[]
    c=0
    if request.method == 'POST':
        query=request.form['query']
        gn = GoogleNews(lang = 'en')
        search = gn.search(query)
        newsitem = search['entries']
        for item in newsitem:
            story={
                'title': item.title,
                'link': item.link
            }
            result.append(story)
            c=c+1
            if c==5:
                break
    return render_template("news.html",result=result)


if __name__=="__main__":
    app.run(debug=True)

