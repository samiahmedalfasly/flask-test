from flask import Flask, render_template
from data import urls_list, count, minutes

app = Flask(__name__)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "img"

def get_url(url2):
    url = url2.replace("watch?v=", "embed/")
    url = url.split('?')[0]
    url = url.replace("watch", "")
    url = url.replace("/shorts", "")
    url = url.replace("/shorts", "")
    url = url.replace("https://youtu.be", "https://www.youtube.com")
    url = url.replace("https://youtube.com", "https://www.youtube.com")
    url = url.replace("https://www.youtube.com", "https://www.youtube.com/embed")
    url = url.replace("/embed/embed", "/embed")
    url = url.replace("/embed/embed", "/embed")
    url = url.replace("?feature=shared", "")
    # print("URL", url)
    return url + "?autoplay=1&loop=1&mute=1"

def get_count_loop():
    count_loop = 1
    len_urls_list = len(urls_list)
    if len_urls_list > 30 and len_urls_list <= 60:
        count_loop = 2
    elif len_urls_list > 60 and len_urls_list <= 90:
        count_loop = 3
    elif len_urls_list > 90 and len_urls_list <= 120:
        count_loop = 4
    elif len_urls_list > 120 and len_urls_list <= 150:
        count_loop = 5
    elif len_urls_list > 150 and len_urls_list <= 180:
        count_loop = 6
    elif len_urls_list > 180 and len_urls_list <= 210:
        count_loop = 7
    elif len_urls_list > 210 and len_urls_list <= 240:
        count_loop = 8
    elif len_urls_list > 240:
        count_loop = 9
    return count_loop

@app.route('/')
def index():
    count_loop = get_count_loop()
    print("count_loop", count_loop)
    return render_template('index.html', count=count_loop)

def get_url2(num=1):
    urls_listt = urls_list
    len_urls_list = len(urls_list)
    if num == 1:
        urls_listt = urls_list if len_urls_list <= 30 else urls_list[:30]
    elif num == 2:
        urls_listt = urls_list[30:] if len_urls_list <= 60 else urls_list[30:60]
    elif num == 3:
        urls_listt = urls_list[60:] if len_urls_list <= 90 else urls_list[60:90]
    elif num == 4:
        urls_listt = urls_list[90:] if len_urls_list <= 120 else urls_list[90:120]
    elif num == 5:
        urls_listt = urls_list[120:] if len_urls_list <= 150 else urls_list[120:150]
    elif num == 6:
        urls_listt = urls_list[150:] if len_urls_list <= 180 else urls_list[150:180]
    elif num == 7:
        urls_listt = urls_list[180:] if len_urls_list <= 210 else urls_list[180:210]
    elif num == 8:
        urls_listt = urls_list[210:] if len_urls_list <= 240 else urls_list[210:240]
    else:
        urls_listt = urls_list[240:]
    return [get_url(i) for i in urls_listt]

@app.route('/youtube-views/<int:num_page>')
def youtube_views(num_page=1):
    count_loop = get_count_loop()
    if count_loop < num_page:
        num_page = count_loop
    return render_template('view_youtube.html', url_list=get_url2(num_page), count=count, minutes=minutes)

@app.route('/vote_url', methods = ['POST'])
def vote_url():
    from vote3 import run_vote
    run_vote()
    return "url data: "

@app.route('/vote', methods = ['GET', 'POST'])
def vote():
    return render_template('vote.html')


if __name__ == '__main__':
    app.run(host='localhost', debug=True,)




# @app.route('/vote')
# def vote():
#     return render_template('vote.html', vote_url=vote_url)




# A very simple Flask Hello World app for you to get started with...

# from flask import Flask, render_template

# app = Flask(__name__)

# from data import urls_list, count, minutes

# def get_url(url2):
#     url = url2.replace("watch?v=", "embed/")
#     url = url.split('?')[0]
#     url = url.replace("watch", "")
#     url = url.replace("/shorts", "")
#     url = url.replace("/shorts", "")
#     url = url.replace("https://youtu.be", "https://www.youtube.com")
#     url = url.replace("https://youtube.com", "https://www.youtube.com")
#     url = url.replace("https://www.youtube.com", "https://www.youtube.com/embed")
#     url = url.replace("/embed/embed", "/embed")
#     url = url.replace("/embed/embed", "/embed")
#     url = url.replace("?feature=shared", "")
#     print("URL", url)
#     return url + "?autoplay=1&loop=1&mute=1"


# @app.route('/')
# def hello_world():
#     return render_template('index.html', url_list=get_url2(), count=count, minutes=minutes)

