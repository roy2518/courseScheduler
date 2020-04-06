from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import ForeignKey, UniqueConstraint, ForeignKeyConstraint, PrimaryKeyConstraint


class Department(db.Model):
    __tablename__ = 'department'
    name = db.Column(db.String(256), primary_key=True)

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<name {}>'.format(self.name)
class Class(db.Model):
    __tablename__ = 'class'
    subject = db.Column(db.String(256))
    num = db.Column(db.Integer)
    unit = db.Column(db.Float(2,1), nullable = False)
    alp = db.Column(db.Boolean, nullable = False)
    cz = db.Column(db.Boolean, nullable = False)
    ns = db.Column(db.Boolean, nullable = False)
    qs = db.Column(db.Boolean, nullable = False)
    ss = db.Column(db.Boolean, nullable = False)
    cci = db.Column(db.Boolean, nullable = False)
    ei = db.Column(db.Boolean, nullable = False)
    sts = db.Column(db.Boolean, nullable = False)
    fl = db.Column(db.Boolean, nullable = False)
    r = db.Column(db.Boolean, nullable = False)
    w = db.Column(db.Boolean, nullable = False)
    rating = db.Column(db.Float(2,1))
    desc = db.Column(db.String(256))
    __table_args__ = (PrimaryKeyConstraint('subject', 'num'), ForeignKeyConstraint(['subject'], ['department.name']))
    def __init__(self, subject, num, unit, alp, cz, ns, qs, ss, cci, ei, sts, fl, r, w, rating, desc):
        self.subject = subject
        self.num = num
        self.unit = unit
        self.alp = alp
        self.cz = cz
        self.ns = ns
        self.qs = qs
        self.ss = ss
        self.cci = cci
        self.ei = ei
        self.sts = sts
        self.fl = fl
        self.r = r
        self.w = w
        self.rating = rating
        self.desc = desc
    def __repr__(self):
        return '<subject {}>'.format(self.subject)
class Corequisite(db.Model):
    __tablename__ = 'corequisite'
    main_subject = db.Column(db.String(256), nullable = False)
    main_num= db.Column(db.Integer, nullable = False)
    main_type = db.Column(db.String(256), nullable = False)
    sup_subject = db.Column(db.String(256), nullable = False)
    sup_num = db.Column(db.Integer, nullable = False)
    sup_type = db.Column(db.String(256), nullable = False)
    __table_args__ = (PrimaryKeyConstraint('sup_subject', 'sup_num', 'sup_type'), ForeignKeyConstraint (['main_subject', 'main_num'], ['class.subject', 'class.num']), ForeignKeyConstraint (['sup_subject', 'sup_num'], ['class.subject', 'class.num']))
    def __init__(self, main_subject, main_num, main_type, sup_subject, sup_num, sup_type):
        self.main_subject = main_subject
        self.main_num = main_num
        self.main_type = main_type
        self.sup_subject = sup_subject
        self.sup_num = sup_num
        self.sup_type = sup_type
    def __repr__(self):
        return '<sup_subject {}>'.format(self.sup_subject)
class CourseOff(db.Model):
    __tablename__ = 'courseoff'
    subject = db.Column(db.String(256))
    course_num = db.Column(db.Integer)
    type = db.Column(db.String(256))
    id = db.Column(db.Integer)
    mon = db.Column(db.Boolean, nullable = False)
    tues = db.Column(db.Boolean, nullable = False)
    wed = db.Column(db.Boolean, nullable = False)
    thur = db.Column(db.Boolean, nullable = False)
    fri = db.Column(db.Boolean, nullable = False)
    start_time = db.Column(db.Time, nullable = False)
    end_time = db.Column(db.Time, nullable = False)
    __table_args__ = (ForeignKeyConstraint(['subject', 'course_num'], ['class.subject', 'class.num']), PrimaryKeyConstraint('subject', 'course_num', 'type', 'id'))

    def __init__(self, main_subject, course_num, type, id, mon, tues, wed, thur, fri, start_time, end_time):
        self.subject = subject
        self.course_num = course_num
        self.type = type
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.mon = mon
        self.tues = tues
        self.wed = wed
        self.thur = thur
        self.fri = fri
    def __repr__(self):
        return '<subject {}>'.format(self.subject)
class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))

    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return '<id {}>'.format(self.id)
class CourseProf(db.Model):
    __tablename__ = 'courseprof'
    subject = db.Column(db.String(256))
    course_num = db.Column(db.Integer)
    type = db.Column(db.String(256))
    id = db.Column(db.Integer)
    prof_id = db.Column(db.Integer)
    rating = db.Column(db.Float(2,1))
    __table_args__ = (PrimaryKeyConstraint('subject', 'course_num', 'type', 'id', 'prof_id'), ForeignKeyConstraint(['subject', 'course_num', 'type', 'id'], ['courseoff.subject', 'courseoff.course_num', 'courseoff.type', 'courseoff.id']), ForeignKeyConstraint(['prof_id'], ['professor.id']))

    def __init__(self, subject, course_num, type, id, prof_id, rating):
        self.subject = subject
        self.course_num = course_num
        self.type = type
        self.id = id
        self.prof_id = prof_id
        self.rating = rating
    def __repr__(self):
        return '<subject {}>'.format(self.subject)

class Schedule(db.Model):
    __tablename__ = 'schedule'
    net_id = db.Column(db.String(256))
    sched_num = db.Column(db.Integer)
    subject = db.Column(db.String(256))
    course_num = db.Column(db.Integer)
    type = db.Column(db.String(256))
    id = db.Column(db.Integer)
    
    __table_args__ = (PrimaryKeyConstraint('net_id', 'sched_num', 'subject', 'course_num', 'type'), ForeignKeyConstraint(['subject', 'course_num', 'type', 'id'], ['courseoff.subject', 'courseoff.course_num', 'courseoff.type', 'courseoff.id']))

    def __init__(self, net_id, sched_num, subject, course_num, type, id):
        self.net_id = net_id
        self.sched_num = sched_num
        self.subject = subject
        self.course_num = course_num
        self.type = type
        self.id = id
    def __repr__(self):
        return '<net_id {}>'.format(self.net_id)
