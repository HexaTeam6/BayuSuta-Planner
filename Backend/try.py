#from flask import Flask, request
#from flew import takeoff
#app = Flask(__name__)

#@app.route('/', methods=["GET","POST"])
#def index():
#    errors = ""
#    if request.method == "POST":
#        takeoff_input = request.form["takeoff_command"]
#         if takeoff_input != "takeoff":
#             errors += "<p>input takeoff command properly</p>\n"
#         if takeoff_input == "takeoff":
#             result = takeoff("nono")
#             return '''
#             <html>
#                     <body>
#                     {result}
#                         <p>Input takeoff command:</p>
#                         <form method="post" action=".">
#                             <p><input name="takeoff_command" /></p>
#                             <p><input type="submit" value="start" /></p>
#                         </form>
#                     </body>
#                 </html>
#             '''.format(result=result)
#     return '''
#     <html>
#             <body>
#             {errors}
#                 <p>Input takeoff command:</p>
#                 <form method="post" action=".">
#                     <p><input name="takeoff_command" /></p>
#                     <p><input type="submit" value="start" /></p>
#                 </form>
#             </body>
#         </html>
#     '''.format(errors=errors)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('echo.html')
 
@app.route("/echo", methods=['POST'])
def echo(): 
    return render_template('echo.html', text=request.form['text'])
 
 
if __name__ == "__main__":
    app.run(debug=True)