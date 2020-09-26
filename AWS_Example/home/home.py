from flask import Flask,render_template, Blueprint,request, flash, session, current_app, url_for, redirect, make_response
from AWS_Example.model import db_session,Users,Stu,jwt_required,create_access_token,set_access_cookies,unset_jwt_cookies,get_jwt_identity,jwt_manager,unset_access_cookies
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
pymysql.install_as_MySQLdb()


#configure blueprints
home_bp = Blueprint('home_bp',__name__,
                    template_folder = 'template',
                    static_folder = 'static')

#function definations
def assign_access_tokens(user_id, url):
    access_token = create_access_token(identity=user_id)
    resp = make_response(redirect(url))
    set_access_cookies(resp, access_token)
    return resp


#routes definations
@home_bp.route('/',methods = ['GET'])
def home():
    return render_template('home.html')


@home_bp.route('/signin',methods = ['GET','POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = db_session.query(Users).filter(Users.email== email, Users.password == password).first()
        list_all = db_session.query(Stu).all()
        if result:
            return assign_access_tokens(email,url_for('home_bp.homepage'))
        else:
            flash('Unable to identify the user')
            return render_template(url_for('home_bp.home'))
    else:
        flash('Following method is not alloweded.')
        return render_template('error.html')


@home_bp.route('/homepage',methods=['GET','POST'])
@jwt_required
def homepage():
    get_user = get_jwt_identity()
    db_session.remove()
    list_all = db_session.query(Stu).all()
    return render_template('signin.html',user=get_user,stu=list_all,headers = ['Student ID','First Name','Last Name','Grade'])


@home_bp.route('/add',methods = ['POST','GET'])
@jwt_required
def add():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        grade = request.form['grade']
        is_in = db_session.query(Stu).filter(Stu.first_name == first_name, Stu.last_name == last_name).first()
        if is_in:
                flash('Student already added')
        else:
            new_student = Stu(first_name = first_name,last_name = last_name, grade = grade)
            db_session.add(new_student)
            db_session.commit()
            flash('Student added successfully')
        return redirect(url_for('home_bp.homepage'))
    else:
        flash('Following method is not allowed')
        return render_template('error.html')


@home_bp.route('/delete/<int:id>',methods = ['POST','GET'])
@jwt_required
def delete(id):
    if request.method == 'POST':
        get_user = get_jwt_identity()
        to_del = db_session.query(Stu).filter(Stu.id == id ).first()
        if to_del:
                db_session.delete(to_del)
                db_session.commit()
                flash('Student deleted')
        else:
            flash('No record found')
        list_all_ = db_session.query(Stu).all()
        return redirect(url_for('home_bp.homepage'))
    else:
        flash('Following method is not allowed')
        return render_template('error.html')


@jwt_manager.expired_token_loader
def expired_token_callback(callback):
    flash('Token Expired. Please Login again')
    resp = make_response(redirect(url_for('home_bp.home')))
    unset_access_cookies(resp)
    return resp


@jwt_manager.unauthorized_loader
def invalid_token_callback(expired_token):
    flash('Missing Token. Please Login again')
    resp = make_response(redirect(url_for('home_bp.home')))
    return resp
