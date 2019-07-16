import os

from flask import Flask
from flask import request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    def todo_view(mtodos):
	       the_view = 'List of my todos' +'<br>'
	       for i in mtodos:
		   the_view += ( i + '<br>' )
	       the_view += 'the list ends here'
	       return the_view 
    #http://127.0.0.1:5000/todos?name=ravi
    def get_name(name):
	if(name=='shivang'):
	       return ["sleep again",'Go for run','listen kshay kumar music'] 
	elif(name=='Manish'):
	       return ['parents','freshness','study','exercise','be ready for work','breakfst','go for work']
	elif(name=='depo'):
		return ['cofee','Go for run','listen kshay kumar music']
	elif(name=='Sanket'):
		return ['parents','freshness','study','exercise','be ready for work','breakfst']
	elif(name=='adam'):
		return ['play cricket','Go for run','listen kshay kumar music']
	else:
		return ["name is not in list"]
    @app.route('/todos')
    def todos():
	name=request.args.get('name')
	print("______________")
	print(name)
	print("______________")
	
	my_todos=get_name(name)
	return todo_view(my_todos)
	  
  
    return app


