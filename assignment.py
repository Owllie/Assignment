#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.debug = True;

calender_list = []

@app.route('/calender', methods = ['GET'])
def get_calender():
	return jsonify( { 'calender_list': calender_list } )


@app.route('/calender/<int:Calid>', methods = ['GET'])
def get_Task(Calid):
        for element in calender_list:
                if element['CalID'] == Calid:
                        return jsonify(element), 200
        return("not Found"), 404

@app.route('/calender/<int:Calid>', methods = ['POST'])
def create_calender(Calid):
        for element in calender_list:
                if element['CalID'] == Calid:
                         return "Already Exists\n", 409
        newCalen = {'CalID':Calid, 'Values':[]}
        calender_list.append(newCalen)
        return "Calender Created\n", 201
        
@app.route('/calender/<int:Calid>/task/<int:Taskid>', methods = ['POST'])
def create_task(Calid, Taskid):
        j=request.get_json(force=True,silent=True)
        if j is None:
                abort(400)
        task = {
        	'TaskID': Taskid,
                'title': j.get('title', ""),
                'description': j.get('description', ""),
                'start_time': j.get('start_time', ""),
                'end_time': j.get('end_time', ""),
                'repeats': j.get('repeats', 0),
                'location': j.get('location', "")
                }
        for element in calender_list:
                if element['CalID'] == Calid:
                        for ele in element['Values']:
                                if ele['TaskID'] == Taskid:
                                        return "Already Exists", 409
                        
                        element['Values'].append(task)
                        return("Addition Successful"), 201
			

@app.route('/calender/<int:Calid>', methods = ['DELETE'])
def delete_calender(Calid):
	for element in calender_list:
		if element['CalID'] == Calid:
			calender_list.remove(element)
			return "Success\n", 202
