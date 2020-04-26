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
    return render_template('courseOff.html', courseoffs=courseoffs)

@app.route('/schedule/<netid>', methods=['GET', 'POST'])
def schedule(netid):
	if request.method == 'GET':
		##courses = db.session.execute('SELECT * FROM Schedule NATURAL JOIN CourseOff WHERE Schedule.net_id = :net_id', dict(net_id=netid))
		courseoffs = db.session.query(models.CourseProf, models.Class, models.CourseOff,models.Professor,models.Schedule).filter(models.CourseOff.subject == models.CourseProf.subject, models.CourseOff.course_num == models.CourseProf.course_num, models.CourseOff.type == models.CourseProf.type, models.CourseOff.id == models.CourseProf.id).filter(models.CourseProf.subject == models.Class.subject, models.CourseProf.course_num == models.Class.num).filter(models.CourseProf.prof_id == models.Professor.id).filter(models.Schedule.net_id == netid).filter(models.Schedule.subject == models.CourseOff.subject).filter(models.Schedule.course_num == models.CourseOff.course_num).filter(models.Schedule.type == models.CourseOff.type).filter(models.Schedule.id == models.CourseOff.id)
		j = []
		schedules = {}
		for course in courseoffs:
			if course.Schedule.sched_num in schedules.keys():
				schedules[course.Schedule.sched_num].append(format_course(course))
			else:
				schedules[course.Schedule.sched_num] = [format_course(course)]
		for temp in schedules.keys():
			j.append({"sched_num": temp, "courses": schedules[temp]})
		return jsonify(j)
	elif request.method == 'POST':
		sched_num = db.session.query(db.func.max(models.Schedule.sched_num)).scalar()
		if request.is_json:
			return_courses = addCourses(request.get_json(), netid, sched_num + 1)
			db.session.commit()
			return jsonify({'sched_num': sched_num + 1, 'courses': return_courses})
		else:
			return jsonify(status='Request was not JSON')


def addCourses(courses, netid, schedule_number):
	return_courses = []
	data = courses['courses']
	for postCourse in data:
		newCourse = models.Schedule(netid, schedule_number, postCourse['subject'], postCourse['course_num'], postCourse['type'], postCourse['id'])
		db.session.add(newCourse)
		return_courses.append({'subject': postCourse['subject'], 'course_num': postCourse['course_num'], 'type': postCourse['type'], 'id': postCourse['id']})
	return return_courses	

def format_course(courseoff):
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
	return dict
	
@app.route('/schedule/<netid>/<schedule_number>', methods=['GET', 'PUT', 'DELETE'])
def schedules(netid, schedule_number):
	if request.method == 'GET':
		##courses = db.session.execute('SELECT * FROM Schedule NATURAL JOIN CourseOff WHERE Schedule.net_id = :net_id AND Schedule.sched_num = :sched_num', dict(net_id=netid, sched_num=schedule_number))
		courseoffs = db.session.query(models.CourseProf, models.Class, models.CourseOff,models.Professor,models.Schedule).filter(models.CourseOff.subject == models.CourseProf.subject, models.CourseOff.course_num == models.CourseProf.course_num, models.CourseOff.type == models.CourseProf.type, models.CourseOff.id == models.CourseProf.id).filter(models.CourseProf.subject == models.Class.subject, models.CourseProf.course_num == models.Class.num).filter(models.CourseProf.prof_id == models.Professor.id).filter(models.Schedule.net_id == netid).filter(models.Schedule.subject == models.CourseOff.subject).filter(models.Schedule.course_num == models.CourseOff.course_num).filter(models.Schedule.type == models.CourseOff.type).filter(models.Schedule.id == models.CourseOff.id).filter(models.Schedule.sched_num == schedule_number)
		j = []
		for course in courseoffs:
			j.append(format_course(course))
		return jsonify({'courses': j})
	elif request.method == 'PUT':
		if request.is_json:
			db.session.execute('DELETE FROM Schedule WHERE net_id=:net_id AND sched_num=:sched_num', dict(net_id=netid, sched_num=schedule_number))
			db.session.commit()
			return_courses = addCourses(request.get_json(), netid, schedule_number)
			db.session.commit()
			return jsonify({'courses': return_courses})
	elif request.method == 'DELETE':
		db.session.execute('DELETE FROM Schedule WHERE net_id=:net_id AND sched_num=:sched_num', dict(net_id=netid, sched_num=schedule_number))
		db.session.commit()
		return jsonify(status='Deleted successfully')
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
	coreq = db.session.query(models.CourseOff, models.Corequisite).filter(models.CourseOff.subject == models.Corequisite.sup_subject, models.CourseOff.course_num == models.Corequisite.sup_num, models.CourseOff.type == models.Corequisite.sup_type)
	course_num = request.args.get('course_num', default = -1, type = int)
	mon = request.args.get('mon', default = "none", type = str)
	tues = request.args.get('tues', default = "none", type = str)
	wed = request.args.get('wed', default = "none", type = str)
	thur = request.args.get('thur', default = "none", type = str)
	fri = request.args.get('fri', default = "none", type = str)
	subject = request.args.get('subject', default = 'none', type = str)
	type = request.args.get('type', default = 'none', type = str)
	id = request.args.get('id', default = -1, type = int)
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
	if (type != 'none'):
		courseoffs = courseoffs.filter(models.CourseOff.type == type)
	if (id != -1):
		courseoffs = courseoffs.filter(models.CourseOff.id == id)
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
		temp = coreq.filter(models.Corequisite.main_subject == courseoff.CourseOff.subject, models.Corequisite.main_num == courseoff.CourseOff.course_num, models.Corequisite.main_type == courseoff.CourseOff.type)
		coreq_dict = {}
		for co in temp:
			co_dict = {}
			co_dict ["subject"] = co.Corequisite.sup_subject
			co_dict ["num"] = co.Corequisite.sup_num
			co_type = co.Corequisite.sup_type
			co_dict ["type"] = co_type
			co_days = {'mon': co.CourseOff.mon, 'tues': co.CourseOff.tues, 'wed': co.CourseOff.wed, 'thur': co.CourseOff.thur, 'fri': co.CourseOff.fri}
			co_dict['days'] = co_days
			co_dict['start_time'] = str(co.CourseOff.start_time)
			co_dict['end_time'] = str(co.CourseOff.end_time)
			co_id = co.CourseOff.id
			co_dict['id'] = co_id
			key = co_type + str(co_id)
			coreq_dict[key] = co_dict
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
		dict['corequisites'] = coreq_dict
		j.append(dict)
	response = jsonify(j)
	response.status_code = 200
	return response

if __name__ == '__main__':
    app.run()
