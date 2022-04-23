#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/",methods = ["GET","POST"]) #generator
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        model = joblib.load("DBS_Prediction")
        result_final = model.predict([[rate]])
        return(render_template("index.html",result=str(result_final)[2:-2]))
    else:
        return(render_template("index.html", result='waiting'))


# In[4]:


if __name__ == "__main__":
    app.run()


# In[ ]:




