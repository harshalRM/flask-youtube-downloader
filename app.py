from flask import Flask, render_template, request, send_file, redirect, url_for
from pytube import YouTube


app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form.get('url')
        link = YouTube(url)
        print(link.title)
        opt = request.form.get('resolution')
        print(opt)
        download_path = link.streams.get_by_resolution(opt).download()
        fname = download_path.split("//")[-1]
        return send_file(fname, as_attachment=True)
    return render_template("layout.html")
  

if __name__ == '__main__':
    app.run(debug=True,port=5000)