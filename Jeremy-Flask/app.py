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
			return_courses = []
			data = request.get_json()['courses']
			for postCourse in data:
				newCourse = models.Schedule(netid, schedule_number, postCourse['subject'], postCourse['course_num'], postCourse['type'], postCourse['id'])
				db.session.add(newCourse)
				return_courses.append({'subject': postCourse['subject'], 'course_num': postCourse['course_num'], 'type': postCourse['type'], 'id': postCourse['id']})
			db.session.commit()
			return jsonify({'courses': return_courses})
		else:
			return jsonify(status='Request was not JSON')


"""
	courseoffs = db.session.query(models.CourseOff)
	course_num = request.args.get('course_num', default = -1, type = int)
	subject = request.args.get('subject', default = 'blank', type = str)
	if (course_num != -1):
		courseoffs = courseoffs.filter(models.CourseOff.course_num == course_num)
	if (subject != 'blank'):
		courseoffs = courseoffs.filter(models.CourseOff.subject == subject)

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
	response = jsonify(j)
	response.status_code = 200
	return response
	"""
@app.route('/courseoff/', methods=['GET'])
def course_off():
	courseoffs = db.session.query(models.CourseProf, models.Class, models.CourseOff,models.Professor).filter(models.CourseOff.subject == models.CourseProf.subject, models.CourseOff.course_num == models.CourseProf.course_num, models.CourseOff.type == models.CourseProf.type, models.CourseOff.id == models.CourseProf.id).filter(models.CourseProf.subject == models.Class.subject, models.CourseProf.course_num == models.Class.num).filter(models.CourseProf.prof_id == models.Professor.id)
	course_num = request.args.get('course_num', default = -1, type = int)
	mon = request.args.get('mon', default = "none", type = str)
	tues = request.args.get('tues', default = "none", type = str)
	wed = request.args.get('wed', default = "none", type = str)
	thur = request.args.get('thur', default = "none", type = str)
	fri = request.args.get('fri', default = "none", type = str)
	subject = request.args.get('subject', default = 'none', type = str)
	professor = request.args.get('professor', default = 'none', type = str)
	before_start = request.args.get('beforestart', default = 'none', type = str)
	after_start = request.args.get('afterstart', default = 'none', type = str)
	before_end = request.args.get('beforeend', default = 'none', type = str)
	after_end = request.args.get('afterend', default = 'none', type = str)
	alp = request.args.get('alp', default = 'none', type = str)
	cz = request.args.get('cz', default = 'none', type = str)
	ns = request.args.get('ns', default = 'none', type = str)
	qs = request.args.get('qs', default = 'none', type = str)
	ss = request.args.get('ss', default = 'none', type = str)
	cci = request.args.get('cci', default = 'none', type = str)
	ei = request.args.get('ei', default = 'none', type = str)
	sts = request.args.get('sts', default = 'none', type = str)
	fl = request.args.get('fl', default = 'none', type = str)
	r = request.args.get('r', default = 'none', type = str)
	w = request.args.get('w', default = 'none', type = str)
	if (course_num != -1):
		courseoffs = courseoffs.filter(models.CourseOff.course_num == course_num)
	if (subject != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.subject == subject)
	if (mon != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.mon == mon)
	if (tues != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.tues == tues)
	if (wed != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.wed == wed)
	if (thur != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.thur == thur)
	if (fri != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.fri == fri)
	if (professor != 'none'):
		courseoffs = courseoffs.filter(models.Professor.name.contains(professor))
	if (before_start != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.start_time <= before_start)
	if (after_start != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.start_time >= after_start)
	if (before_end != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.end_time <= before_end)
	if (after_end != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.end_time >= after_end)
	if (alp != 'none'):
		courseoffs = courseoffs.filter(models.Class.alp == alp)
	if (cz != 'none'):
		courseoffs = courseoffs.filter(models.Class.cz == cz)
	if (ns != 'none'):
		courseoffs = courseoffs.filter(models.Class.ns == ns)
	if (qs != 'none'):
		courseoffs = courseoffs.filter(models.Class.qs == qs)
	if (ss != 'none'):
		courseoffs = courseoffs.filter(models.Class.ss == ss)
	if (cci != 'none'):
		courseoffs = courseoffs.filter(models.Class.cci == cci)
	if (ei != 'none'):
		courseoffs = courseoffs.filter(models.Class.ei == ei)
	if (sts != 'none'):
		courseoffs = courseoffs.filter(models.Class.sts == sts)
	if (fl != 'none'):
		courseoffs = courseoffs.filter(models.Class.fl == fl)
	if (r != 'none'):
		courseoffs = courseoffs.filter(models.Class.r == r)
	if (w != 'none'):
		courseoffs = courseoffs.filter(models.Class.w == w)
	j = []
	for courseoff in courseoffs:
		dict = {}
		dict['subject'] = courseoff.Class.subject
		dict['course_num'] = courseoff.CourseOff.course_num
		dict['type'] = courseoff.CourseOff.type
		dict['id'] = courseoff.CourseOff.id
		days = {'mon': courseoff.CourseOff.mon, 'tues': courseoff.CourseOff.tues, 'wed': courseoff.CourseOff.wed, 'thur': courseoff.CourseOff.thur, 'fri': courseoff.CourseOff.fri}
		dict['days'] = days
		attributes = {'alp': courseoff.Class.alp, 'cz': courseoff.Class.cz, 'ns': courseoff.Class.ns, 'qs': courseoff.Class.qs, 'ss': courseoff.Class.ss, 'cci': courseoff.Class.cci, 'ei': courseoff.Class.ei, 'sts': courseoff.Class.sts, 'fl': courseoff.Class.fl, 'r': courseoff.Class.r, 'w': courseoff.Class.w}
		dict['attributes'] = attributes
		dict['start_time'] = str(courseoff.CourseOff.start_time)
		dict['end_time'] = str(courseoff.CourseOff.end_time)
		if ( courseoff.Class.description != None):
			dict['description'] = courseoff.Class.description.lower().title()
		else:
			dict['description'] = courseoff.Class.description
		dict['professor'] = courseoff.Professor.name
		dict['class_rating'] = float(courseoff.Class.rating)
		dict['prof_rating'] = float(courseoff.CourseProf.rating)
		j.append(dict)
	response = jsonify(j)
	response.status_code = 200
	return response

if __name__ == '__main__':
    app.run()
