Hi guys,

I got some requests to share my source code for visualizing the random forest trees, so here you go:) To see the HTML file directly, please go [here](frontend/app/templates/index.html). I added some descriptions below for you and for myself when I forget everything tomorrow.

**Description**

To start running/hosting the API, navigate to the **run.py** folder and run it through command line. Because somewhere in the code we specified port equals 5000, we can now open a brower and type in *localhost:5000* to see the API.

What happens under the hood is that **run.py** starts by importing the entire **app/** folder. The reason why the **app/** folder is treated as an import-able module is that it contains an **\_\_init\_\_.py** file; any folder with an **\_\_init\_\_.py** file is recognized by Python as a Python module just like any other modules we import.

The **\_\_init\_\_.py** file is automatically run when imported, as a result, at this point, we have a Flask() object assigned to the name *application*. A few nano-seconds later, when the line *application.run()* is run, Python knows to run the function I defined right under this decorator: *@app.route("/")*. This function with decorator is rendering/showing my **app/templates/index.html** file. I wrote this function in **app/py_version_classifier.py**. The **app/py_version_classifier.py** file is imported when the **\_\_init\_\_.py** file was run;  any single Python script file - unlike a folder - can be imported as a module no problem if they are placed under the same folder.

So far, I explained the Python flask codes which are based on Kyle's [iris app](https://github.com/thisismetis/sf17_ds6/tree/master/resources/flask/iris-app).

The frontend tree codes are mostly in **app/templates/index.html**. They are based on Mike Bostock’s [collapsible indented tree](https://bl.ocks.org/mbostock/1093025) and the [d3 slider](http://thematicmapping.org/playground/d3/d3.slider/). I don't know much about these codes; one tip though, is that assigning different **#id**'s to the slider svg and the tree svg, respectively, was very helpful when it comes to costimizing one svg but not the other.

The AJAX POST request works like this:
- The **contentType** is boilerplate. It just says my data are in the JSON format.
- **url: "/draw_tree"** is how AJAX knows to go to my Python function defined right under this decorator: *@app.route("/draw_tree")* and run that function. Any function parameter required is passed in in a JSON format using **data: "{\"treeparams\": ["+treeNum+"]}"**. To elaborate, it is passing a JSON dictionary into my Python function; this dictionary contains one key called *treeparams* and one value which is a list. My list happens to only have one value which is *treeNum*. The actual *treeNum* value is created when I drag my D3 slider around on the browser.
- If my Python function ran successfully, then **success: function (data) { .. }** will get executed. *data* is whatever the Python function returns which has to be in a JSON format. In my case, I am using *data* to update my D3 tree graph.
- If my Python function ran with errors, then **error: function (result) { .. }** will get executed.

The live demo I showed yesterday is now on YouTube [here](https://www.youtube.com/watch?v=D8_yesxONsM).

**Key files**  
&ensp;&ensp;[frontend/app/templates/index.html](frontend/app/templates/index.html)   
&ensp;&ensp;[frontend/run.py](frontend/run.py)  
&ensp;&ensp;[frontend/app/py_version_classifier.py](frontend/app/py_version_classifier.py)  
&ensp;&ensp;[frontend/models/model.ipynb](frontend/models/model.ipynb)  
&ensp;&ensp;[frontend/models/clean.ipynb](frontend/models/clean.ipynb)  
&ensp;&ensp;[frontend/models/clean2.ipynb](frontend/models/clean2.ipynb)  
&ensp;&ensp;[McNulty_Huang20170517.pdf](McNulty_Huang20170517.pdf)

Enjoy!
