from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Moses'

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    short_answer = TextAreaField('Short-form Answer', validators=[DataRequired()])
    long_answer = TextAreaField('Long-form Answer', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[('very-satisfied', 'Very Satisfied'), ('satisfied', 'Satisfied'), ('neutral', 'Neutral'), ('unsatisfied', 'Unsatisfied'), ('very-unsatisfied', 'Very Unsatisfied')], validators=[DataRequired()])
    recommend = RadioField('Would you recommend this course to others?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    improvements = TextAreaField('Suggestions for Improvement')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        data = (
            f"Name: {form.name.data}\n"
            f"Course: {form.course.data}\n"
            f"Short-form Answer: {form.short_answer.data}\n"
            f"Long-form Answer: {form.long_answer.data}\n"
            f"Overall Satisfaction: {form.satisfaction.data}\n"
            f"Recommend: {form.recommend.data}\n"
            f"Suggestions for Improvement: {form.improvements.data}\n\n"
        )

        file_path = 'feedback.txt'

        with open(file_path, 'a') as file:
            file.write(data)

        return redirect(url_for('feedback'))
    return render_template('Example.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

