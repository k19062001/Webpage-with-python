#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
app=Flask(__name__)
@app.route("/")
def hometry():
    return "learning Success!!"
@app.route("/<name>")
def user(name):
    return f"Hello!! {name}"
if __name__=="__main__":
    app.run()


# In[ ]:




