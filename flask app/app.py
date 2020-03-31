from flask import Flask, render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
import models

@app.route('/')
def hello():
    courseoffs = db.session.query(models.CourseOff).all()
    print (courseoffs)
    return render_template('courseOff.html', courseoffs=courseoffs)


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
		dict['start_time'] = str(courseoff.start_time)
		dict['end_time'] = str(courseoff.end_time)
		j.append(dict)
	#print (j)
	return jsonify(j)

if __name__ == '__main__':
    app.run()