from flask import Flask, render_template, redirect, request, url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired
import pymongo
from bson import ObjectId

# kpop collection from mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/", retryWrites = False)
db = client["c4e"]
kpop_collection = db["kpop_idol"]

app = Flask(__name__)

app.config["SECRET_KEY"] = "someone that I know"

# class Logout(FlaskForm):
#     submit = SubmitField(u'Log out')

class LoginForm(FlaskForm):
    username = StringField(u'Username', validators=[DataRequired()])
    password = PasswordField(u'Password', validators=[DataRequired()])
    submit = SubmitField(u"Sign in")

class CreateForm(FlaskForm):
    stage_name = StringField(u'Stage Name', validators=[DataRequired()])
    full_name = StringField(u'Full Name', validators=[DataRequired()])
    group = StringField(u'Group', validators=[DataRequired()])
    submit = SubmitField(u'Create')


class EditForm(FlaskForm):
    stage_name = StringField(u'Stage Name', validators=[DataRequired()])
    full_name = StringField(u'Full Name', validators=[DataRequired()])
    group = StringField(u'Group', validators=[DataRequired()])
    submit = SubmitField(u'Update')


@app.route("/", methods = ["GET", "POST"])
def homepage():
    form = LoginForm(request.form)
    if request.method == "POST": 
        if form.validate_on_submit():
            username = request.form.get("username", "", type=str)
            password = request.form.get("password", "", type=str)
            if request.form['username'] != 'admin' or request.form['password'] != "admin":
                return 'Invalid Credentials. Please try again.'
            else:
                return redirect(url_for("kpop"))
    return render_template("html_form.html", form=form)
       
        
@app.route("/kpop")
def kpop():
    idols = kpop_collection.find({})
    return render_template("kpop.html", idols_data = idols)
    # return render_template("kpop1.html", idols_data = idols)

@app.route("/idol/<stage_name>")
def my_info(stage_name):
    idol = kpop_collection.find_one({"stage_name": stage_name})
    return render_template("detail.html", idol=idol)

# create form
@app.route('/create', methods = ['GET', 'POST'])
def create():
    form = CreateForm(request.form)
    # log_out = Logout(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            stage_name = request.form.get('stage_name', '', type=str)
            full_name = request.form.get('full_name', '', type=str)
            group = request.form.get('group', '', type=str)
            artist = {'stage_name': stage_name, 'full_name': full_name, 'group': group}
            kpop_collection.insert_one(artist)
            return redirect(url_for('kpop'))
    return render_template('create_idol.html', form = form)

# delete form
@app.route('/delete/<stage_name>')
def delete(stage_name):
    # if session.get('username') is None:
    #     return redirect(url_for('homepage'))
    kpop_collection.delete_one({'stage_name': stage_name})
    return redirect(url_for('kpop'))

@app.route('/edit/<stage_name>', methods = ['GET', 'POST'])
def edit(stage_name):    
    form = EditForm(request.form)
    # log_out = Logout(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            stage_name = request.form.get('stage_name', '', type=str)
            full_name = request.form.get('full_name', '', type=str)
            group = request.form.get('group', '', type=str)
            artist = {'stage_name': stage_name, 'full_name': full_name, 'group': group}
            kpop_collection.update_one(artist)
            return redirect(url_for('kpop'))
    return render_template('edit_idol.html', form = form, stage_name= stage_name)


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('homepage'))

app.run(debug=True)

