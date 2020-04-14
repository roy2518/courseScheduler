"""empty message

Revision ID: 763ca667f505
Revises: ca5d0c55d22c
Create Date: 2020-03-29 01:17:15.729557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '763ca667f505'
down_revision = 'ca5d0c55d22c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('class',
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
    sa.ForeignKeyConstraint(['subject'], ['department.name'], ),
    sa.PrimaryKeyConstraint('subject', 'num')
    )
    op.create_table('courseoff',
    sa.Column('subject', sa.String(length=256), nullable=False),
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
    sa.ForeignKeyConstraint(['subject', 'course_num'], ['class.subject', 'class.num'], ),
    sa.PrimaryKeyConstraint('subject', 'course_num', 'type', 'id')
    )
    op.create_table('corequisite',
    sa.Column('main_subject', sa.String(length=32), nullable=False),
    sa.Column('main_num', sa.Integer(), nullable=False),
    sa.Column('main_type', sa.String(length=32), nullable=False),
    sa.Column('sup_subject', sa.String(length=32), nullable=False),
    sa.Column('sup_num', sa.Integer(), nullable=False),
    sa.Column('sup_type', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['main_subject', 'main_num', 'main_type'], ['courseoff.subject', 'courseoff.course_num', 'courseoff.type'], ),
    sa.ForeignKeyConstraint(['sup_subject', 'sup_num', 'sup_type'], ['courseoff.subject', 'courseoff.course_num', 'courseoff.type'], ),
    sa.PrimaryKeyConstraint('sup_subject', 'sup_num', 'sup_type', name='_sup_uc')
    )
    op.drop_table('courseofftest')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courseofftest',
    sa.Column('course_name', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('course_type', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('time', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('course_name', 'course_type', 'course_id', name='courseofftest_pkey')
    )
    op.drop_table('corequisite')
    op.drop_table('courseoff')
    op.drop_table('class')
    op.drop_table('department')
    # ### end Alembic commands ###
