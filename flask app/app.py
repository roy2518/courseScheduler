from flask import Flask, render_template, request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os




app = Flask(__name__)
CORS(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
import models

@app.route('/')
def hello():
    courseoffs = db.session.query(models.CourseOff).all()
    print (courseoffs)
    return render_template('courseOff.html', courseoffs=courseoffs)

@app.route('/schedule/<netid>/<schedule_number>', methods=['GET', 'POST'])
def schedules(netid, schedule_number):
	if request.method == 'GET':
		courses = db.session.query(models.Schedule).filter(models.Schedule.netid == netid and models.Schedule.schedule_number == schedule_number).all()
		j = []
		for course in courses:
			dict = {}
			dict['subject'] = course.subject
			dict['course_num'] = course.course_num
			dict['type'] = course.type
			dict['id'] = course.id
			j.append(dict)
		return jsonify(j)
	elif request.method == 'POST':
		if request.is_json:
			data = request.get_json()
			new_course = db.session.execute('INSERT INTO Schedule VALUES(:net_id, :schedule_num, :subject, :course_num, :course_type, :course_id', dict(net_id=netid, schedule_num=schedule_number, subject=data['subject'], course_num=data['course_num'], course_type=data['type'], course_id=data['id'])
			print(new_course)
			##TODO: see format of new_course and then figure out return value
			return data
		else:
			return jsonify(status='Request was not JSON')

	

@app.route('/<subject>', methods=['GET'])
def course_off_subject(subject):
	courseoffs = db.session.query(models.CourseOff).filter(models.CourseOff.subject == subject).all()
	j = []
	for courseoff in courseoffs:
		dict = {}
		dict['subject'] = courseoff.subject
		dict['course_num'] = courseoff.course_num
		dict['type'] = courseoff.type
		dict['id'] = courseoff.id
		days = {'mon': courseoff.mon, 'tues': courseoff.tues, 'wed': courseoff.wed, 'thur': courseoff.thur, 'fri': courseoff.fri}
		dict['days'] = days
		dict['start_time'] = str(courseoff.start_time)
		dict['end_time'] = str(courseoff.end_time)
		j.append(dict)
	#print (j)
	return jsonify(j)

if __name__ == '__main__':
    app.run()
