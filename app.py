from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    short_answer = TextAreaField('Short-form Answer', validators=[DataRequired()])
    long_answer = TextAreaField('Long-form Answer', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[('very-satisfied', 'Very Satisfied'), ('satisfied', 'Satisfied'), ('neutral', 'Neutral'), ('unsatisfied', 'Unsatisfied'), ('very-unsatisfied', 'Very Unsatisfied')], validators=[DataRequired()])
    recommend = RadioField('Would you recommend this course to others?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    improvements = TextAreaField('Suggestions for Improvement')
