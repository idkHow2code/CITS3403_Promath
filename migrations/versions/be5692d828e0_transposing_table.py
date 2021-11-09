"""Transposing table

Revision ID: be5692d828e0
Revises: bfcf4bd01a35
Create Date: 2021-05-19 01:21:31.334670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be5692d828e0'
down_revision = 'bfcf4bd01a35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transposing_quiz',
    sa.Column('QuizID', sa.Integer(), nullable=False),
    sa.Column('Module', sa.Text(), nullable=True),
    sa.Column('Question', sa.Text(), nullable=True),
    sa.Column('Answer', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('QuizID')
    )
    op.drop_table('Test')
    op.drop_table('img')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('img',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('img', sa.TEXT(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('mimeType', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('img')
    )
    op.create_table('Test',
    sa.Column('TestID', sa.INTEGER(), nullable=False),
    sa.Column('QuestionNo', sa.INTEGER(), nullable=False),
    sa.Column('Question_ID', sa.INTEGER(), nullable=True),
    sa.Column('User_Input', sa.FLOAT(), nullable=True),
    sa.ForeignKeyConstraint(['Question_ID'], ['TestQuestion.QuestionID'], ),
    sa.PrimaryKeyConstraint('TestID')
    )
    op.drop_table('transposing_quiz')
    # ### end Alembic commands ###
