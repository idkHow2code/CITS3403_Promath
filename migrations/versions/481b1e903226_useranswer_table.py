"""UserAnswer table

Revision ID: 481b1e903226
Revises: 03631835ca3b
Create Date: 2021-05-18 18:06:32.155527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '481b1e903226'
down_revision = '03631835ca3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_answers',
    sa.Column('UserTestID', sa.Integer(), nullable=False),
    sa.Column('User_ID', sa.Integer(), nullable=True),
    sa.Column('Question_No', sa.Integer(), nullable=True),
    sa.Column('Question_ID', sa.Integer(), nullable=True),
    sa.Column('User_Input', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['Question_ID'], ['TestQuestion.QuestionID'], ),
    sa.ForeignKeyConstraint(['User_ID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('UserTestID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_answers')
    # ### end Alembic commands ###