'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''

import openai

class GPT():
  ''' make queries to gpt from a given API '''
  def __init__(self,apikey):
    ''' store the apikey in an instance variable '''
    self.apikey=apikey
      # Set up the OpenAI API client
    openai.api_key = apikey #os.environ.get('APIKEY')

    # Set up the model and prompt
    self.model_engine = "text-davinci-003"

  def getResponse(self,prompt):
    ''' Generate a GPT response '''
    completion = openai.Completion.create(
      engine=self.model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.8,
    )
    response = completion.choices[0].text
    return response
  
  ''''
  create() params
  max_tokens: maximum number of tokens to generate in the completion;
  n: how many completions to generate for each prompt;
  stop: up to 4 sequences where API will stop generating further tokens;
  temperature: 0-2, higher values make output more random, lower makes it more deterministic;
  '''

  # ------------------- minsung ------------------- #
  def get_breakfast(self, prompt):
    modified_prompt = "Give me a creative breakfast dish name and a breakfast recipe using only the following ingredients: " + prompt
    completion = openai.Completion.create(
      engine = self.model_engine,
      prompt = modified_prompt,
      max_tokens = 1024,
      n = 1,
      stop = None,
      temperature = .5
    )
    response = completion.choices[0].text
    return response
  # ----------------------------------------------- #
  # ----------------------------------------------- #
  def getLunch(self, prompt):
    modified_prompt = "please give me a lunch recipe with a unique name (use a pun if possible) using only the following ingredients, thank you!:  " + prompt
    completion = openai.Completion.create(
      engine = self.model_engine,
      prompt = modified_prompt,
      max_tokens = 1024,
      n = 1,
      stop = None,
      temperature = .5
    )
    response = completion.choices[0].text
    return response
  # ----------------------------------------------- #
  # ----------------------------------------------- #
  def getDinner(self, prompt):
    modified_prompt = "create a dinner dish using these ingredients: " + prompt
    completion = openai.Completion.create(
      engine = self.model_engine,
      prompt = modified_prompt,
      max_tokens = 1024,
      n = 1,
      stop = None,
      temperature = .5
    )
    response = completion.choices[0].text
    return response

if __name__=='__main__':
  '''
  '''
  import os
  g = GPT(os.environ.get("APIKEY"))
  print(g.getResponse("what does openai's GPT stand for?"))
  print(g.getResponse("make a recipie with shrimp and noodles"))