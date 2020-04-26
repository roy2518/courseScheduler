"""empty message

Revision ID: 6788cdc9a732
Revises: 9488b1a3a165
Create Date: 2020-03-29 03:20:18.688405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6788cdc9a732'
down_revision = '9488b1a3a165'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departmentdos',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('professortres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classdos',
    sa.Column('subject', sa.String(length=32), nullable=False),
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('unit', sa.Float(precision=2, asdecimal=1), nullable=False),
    sa.Column('alp', sa.Boolean(), nullable=False),
    sa.Column('cz', sa.Boolean(), nullable=False),
    sa.Column('ns', sa.Boolean(), nullable=False),
    sa.Column('qs', sa.Boolean(), nullable=False),
    sa.Column('ss', sa.Boolean(), nullable=False),
    sa.Column('cci', sa.Boolean(), nullable=False),
    sa.Column('ei', sa.Boolean(), nullable=False),
    sa.Column('sts', sa.Boolean(), nullable=False),
    sa.Column('fl', sa.Boolean(), nullable=False),
    sa.Column('r', sa.Boolean(), nullable=False),
    sa.Column('w', sa.Boolean(), nullable=False),
    sa.Column('rating', sa.Float(precision=2, asdecimal=1), nullable=True),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['subject'], ['departmentdos.name'], ),
    sa.PrimaryKeyConstraint('subject', 'num')
    )
    op.create_table('corequisitedos',
    sa.Column('main_subject', sa.String(length=32), nullable=False),
    sa.Column('main_num', sa.Integer(), nullable=False),
    sa.Column('main_type', sa.String(length=32), nullable=False),
    sa.Column('sup_subject', sa.String(length=32), nullable=False),
    sa.Column('sup_num', sa.Integer(), nullable=False),
    sa.Column('sup_type', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['main_subject', 'main_num'], ['classdos.subject', 'classdos.num'], ),
    sa.ForeignKeyConstraint(['sup_subject', 'sup_num'], ['classdos.subject', 'classdos.num'], ),
    sa.PrimaryKeyConstraint('sup_subject', 'sup_num', 'sup_type')
    )
    op.create_table('courseoffdos',
    sa.Column('subject', sa.String(length=32), nullable=False),
    sa.Column('course_num', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=8), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mon', sa.Boolean(), nullable=False),
    sa.Column('tues', sa.Boolean(), nullable=False),
    sa.Column('wed', sa.Boolean(), nullable=False),
    sa.Column('thur', sa.Boolean(), nullable=False),
    sa.Column('fri', sa.Boolean(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['subject', 'course_num'], ['classdos.subject', 'classdos.num'], ),
    sa.PrimaryKeyConstraint('subject', 'course_num', 'type', 'id')
    )
    op.create_table('courseprofdos',
    sa.Column('subject', sa.String(length=32), nullable=False),
    sa.Column('course_num', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=8), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prof_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(precision=2, asdecimal=1), nullable=True),
    sa.ForeignKeyConstraint(['prof_id'], ['professortres.id'], ),
    sa.ForeignKeyConstraint(['subject', 'course_num', 'type', 'id'], ['courseoffdos.subject', 'courseoffdos.course_num', 'courseoffdos.type', 'courseoffdos.id'], ),
    sa.PrimaryKeyConstraint('subject', 'course_num', 'type', 'id', 'prof_id')
    )
    op.drop_table('professor')
    op.drop_table('courseoff')
    op.drop_table('courseprof')
    op.drop_table('class')
    op.drop_table('professordos')
    op.drop_table('corequisite')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('corequisite',
    sa.Column('main_subject', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('main_num', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('main_type', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('sup_subject', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('sup_num', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sup_type', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['main_subject', 'main_num'], ['class.subject', 'class.num'], name='corequisite_main_subject_main_num_fkey'),
    sa.ForeignKeyConstraint(['sup_subject', 'sup_num'], ['class.subject', 'class.num'], name='corequisite_sup_subject_sup_num_fkey'),
    sa.PrimaryKeyConstraint('sup_subject', 'sup_num', 'sup_type', name='_sup_uc')
    )
    op.create_table('professordos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='professordos_pkey')
    )
    op.create_table('class',
    sa.Column('subject', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('num', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('unit', sa.REAL(), autoincrement=False, nullable=False),
    sa.Column('alp', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('cz', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('ns', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('qs', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('ss', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('cci', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('ei', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('sts', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('fl', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('r', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('w', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('rating', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('desc', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('subject', 'num', name='class_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('courseprof',
    sa.Column('subject', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('course_num', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(length=8), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('prof_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('rating', sa.REAL(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['prof_id'], ['professor.id'], name='courseprof_prof_id_fkey'),
    sa.ForeignKeyConstraint(['subject', 'course_num', 'type', 'id'], ['courseoff.subject', 'courseoff.course_num', 'courseoff.type', 'courseoff.id'], name='courseprof_subject_course_num_type_id_fkey'),
    sa.PrimaryKeyConstraint('subject', 'course_num', 'type', 'id', 'prof_id', name='courseprof_pkey')
    )
    op.create_table('courseoff',
    sa.Column('subject', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('course_num', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(length=8), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('mon', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('tues', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('wed', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('thur', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('fri', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('start_time', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('end_time', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['subject', 'course_num'], ['class.subject', 'class.num'], name='courseoff_subject_course_num_fkey'),
    sa.PrimaryKeyConstraint('subject', 'course_num', 'type', 'id', name='courseoff_pkey')
    )
    op.create_table('professor',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='professor_pkey')
    )
    op.drop_table('courseprofdos')
    op.drop_table('courseoffdos')
    op.drop_table('corequisitedos')
    op.drop_table('classdos')
    op.drop_table('professortres')
    op.drop_table('departmentdos')
    # ### end Alembic commands ###