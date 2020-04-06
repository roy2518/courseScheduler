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


@app.route('/schedule')
def schedule():
	courses = db.session.query(models.Schedule).all()
	j = []
	for course in courses:
		temp_dict = {}
		temp_dict['subject'] = course.subject
		temp_dict['course_num'] = course.course_num
		temp_dict['type'] = course.type
		temp_dict['id'] = course.id
		temp_dict['net_id'] = course.net_id
		temp_dict['sched_num'] = course.sched_num
		j.append(temp_dict)
	return jsonify(j)

@app.route('/schedule/<netid>/<schedule_number>', methods=['GET', 'POST'])
def schedules(netid, schedule_number):
	if request.method == 'GET':
		courses = db.session.query(models.Schedule).filter(models.Schedule.net_id == netid).filter(models.Schedule.sched_num == schedule_number).all()
		j = []
		for course in courses:
			temp_dict = {}
			temp_dict['subject'] = course.subject
			temp_dict['course_num'] = course.course_num
			temp_dict['type'] = course.type
			temp_dict['id'] = course.id
			temp_dict['net_id'] = course.net_id
			temp_dict['sched_num'] = course.sched_num
			j.append(temp_dict)
		return jsonify(j)
	elif request.method == 'POST':
		if request.is_json:
			data = request.get_json()
			##key_dict = dict(net_id=netid, schedule_num=schedule_number, subject=data['subject'], course_num=data['course_num'], course_type=data['type'], course_id=data['id'])
			newCourse = models.Schedule(netid, schedule_number, data['subject'], data['course_num'], data['type'], data['id'])
			##db.session.execute('INSERT INTO Schedule VALUES(:net_id, :schedule_num, :subject, :course_num, :course_type, :course_id)', key_dict)
			db.session.add(newCourse)
			db.session.commit()			
			course = {'net_id': netid, 'sched_num': schedule_number, 'subject': data['subject'], 'course_num': data['course_num'], 'type': data['type'], 'id': data['id']}
			return jsonify({'course': course})
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
