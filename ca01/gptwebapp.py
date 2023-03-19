'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
import datetime
from flask import request,redirect,url_for,Flask, render_template
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

#index route
@app.route('/')
def index():
  ''' display a link to the general query page '''
  print('processing / route')
  return render_template('index.html')

# team page route 
@app.route('/team_5_page')
def team_5_page():
  return render_template("/team5Page.html")

# class gpt demo
@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
  ''' handle a get request by sending a form 
      and a post request by returning the GPT response
  '''
  if request.method == 'POST':
    prompt = request.form['prompt']
    answer = gptAPI.getResponse(prompt)
    return f'''
    <h1>GPT Demo</h1>
    <pre style="bgcolor:yellow">{prompt}</pre>
    <hr>
    Here is the answer in text mode:
    <div style="border:thin solid black">{answer}</div>
    Here is the answer in "pre" mode:
    <pre style="border:thin solid black">{answer}</pre>
    <a href={url_for('gptdemo')}> make another query</a>
    '''
  else:
    return '''
    <h1>GPT Demo App</h1>
    Enter your query below
    <form method="post">
      <textarea name="prompt"></textarea>
      <p><input type=submit value="get response">
    </form>
    '''

# ------------------- minsung's routes for ca01 ------------------- #
# homepage route
@app.route('/minsung_home')
def minsung_home():
  return render_template("/minsung/minsungHome.html")

# about page for get_optimize
@app.route('/get_breakfast_about')
def get_optimize_about_page():
  return render_template("/minsung/getBreakfastAbout.html")

# route to try out get_optimize
@app.route('/get_breakfast', methods = ['GET', 'POST'])
def get_optimize():
  if request.method == 'POST':
    prompt = request.form['prompt']
    answer = gptAPI.get_breakfast(prompt)
    data = { "prompt": prompt, "response": answer }
    return render_template("/minsung/getBreakfastResponse.html", data = data)
  else:
    return render_template("/minsung/getBreakfastGet.html")
    
# ----------------------------------------------------------------- #

# ------------------- Rose's routes for ca01 ------------------- #
# homepage route
@app.route('/rose_home')
def rose_home():
  return render_template("/rose/roseHome.html")

# about page for get_dessert
@app.route('/get_dessert_about')
def get_dessert_about_page():
  return render_template("/rose/getDessertAbout.html")

# route to try out get_optimize
@app.route('/get_dessert', methods = ['GET', 'POST'])
def get_dessert():
  if request.method == 'POST':
    prompt = request.form['prompt']
    answer = gptAPI.get_dessert(prompt)
    data = { "prompt": prompt, "response": answer }
    return render_template("/rose/getDessertResponse.html", data = data)
  else:
    return render_template("/rose/getDessertGet.html")
    
# ----------------------------------------------------------------- #


# ------------------- Ianna's routes for ca01 ------------------- #
# homepage route
@app.route('/ianna_home')
def ianna_home():
  return render_template("/ianna/iannaHome.html")

# about page for dinner
@app.route('/dinner_description')
def get_dinner_description():
  return render_template("/ianna/dinnerDescription.html")

# route to try out get_optimize
@app.route('/dinner_menu', methods = ['GET', 'POST'])
def dinner_menu():
  if request.method == 'POST':
    prompt = request.form['prompt']
    answer = gptAPI.getDinner(prompt)
    data = { "prompt": prompt, "response": answer }
    #display plausible dinner
    return render_template("/ianna/dinnerDish.html", data = data)
  else:
    #user types in the ingredients they have
    return render_template("/ianna/dinner_recipe.html")
    
# ----------------------------------------------------------------- #
# ------------------- shaithea routes for ca01 ------------------- #
# homepage route
@app.route('/shaithea_home')
def shaithea_home():
  return render_template("/shaithea/shaitheaHome.html")

# about page for get_lunch_recipe
@app.route('/lunch_description')
def get_lunch_description():
  return render_template("/shaithea/getLunchRecipeDescription.html")

# route to try get_lunch_recipe
@app.route('/lunch_recipe', methods = ['GET', 'POST'])
def get_lunch_recipe():
  if request.method == 'POST':
    prompt = request.form['prompt']
    answer = gptAPI.getLunch(prompt)
    data = { "prompt": prompt, "response": answer }
    return render_template("/shaithea/lunchRecipe.html", data = data)
  else:
    return render_template("/shaithea/getLunchRecipe.html")
    
# ----------------------------------------------------------------- #

if __name__=='__main__':
  # run the code on port 5001, MacOS uses port 5000 for its own service :(
  app.run(debug=True,port=5001)