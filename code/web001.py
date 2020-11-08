import pyzenith
from flask import Flask,flash,render_template
from flask import request,session,g,redirect,url_for,abort

app=Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.secret_key = '123456'
app.config.update(SECRET_KEY='123456')

def connect_db():
    """Connects to the specific database."""
    host='127.0.0.1'
    username='PAO'
    password='Gauss147258'
    port='1888'
    conn=pyzenith.connect(host,username,password,port)
    return conn

#home page
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('login1.html')
#login page 
@app.route('/login', methods=['GET','POST'])
def login():
    # 需要从request对象读取表单内容：
    error = None
    print(request)
    if request.method == 'POST':
        user_id=int(request.form['username'])
        print(user_id)
        session['user_id']=user_id
        password=request.form['password']
        print(password)
        db=connect_db()
        c=db.cursor()
        user='''
        Select password from staffs where staff_id='%d'
        '''%user_id
        try:
            c.execute(user)
            pas=c.fetchall()[0][0]
            if pas==password:
                print("succed!")
                flash("succed!")
                if user_id==203:
                    return render_template('hr_index.html')
                else:
                    manager='''
                    Select staff_id from staffs where manager_id='%d'
                    '''%user_id
                    c.execute(manager)
                    try:
                        row1=c.fetchall()[0][0]
                        print(row1)
                        return render_template('man_index.html')
                    except:
                        print("staff")
                        return render_template('staff_index.html')
            else:
                flash("密码错误,请重新输入...")
                return render_template('login1.html')
            c.close()
            db.close()

        except:
            flash("账号错误，请重新输入...")
            c.close()
            db.close()
            return render_template('login1.html')
#退出
@app.route('/logout', methods=['GET','POST'])
def logout():
    flash('退出成功！')
    session.pop('user_id',None)
    return render_template('login1.html')

#修改密码
@app.route('/pwd', methods=['GET','POST'])
def pwd():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    if request.method=='POST':
        if request.form['pwd']==request.form['pwd1']:
            db = connect_db()
            cur = db.cursor()
            sql = "update staffs set password="+"'"+request.form['pwd']+"'"+" where staff_id="+str(session['user_id'])
            print(sql)
            cur.execute(sql)
            db.commit()
            db.close()
            flash('修改密码成功，请重新登录')
            session.pop('user_id',None)
            return render_template('login1.html')
        else :
            flash('两次密码不相同，请重新输入')
            return render_template('pwd.html')
    return render_template('pwd.html')

@app.route('/staff_index',methods=['GET','POST'])
def staff_index():
    return render_template('staff_index.html')

@app.route('/man_index',methods=['GET'])
def man_index():
    return render_template('man_index.html')

@app.route('/hr_index',methods=['GET'])
def hr_index():
    return render_template('hr_index.html')

#个人信息
@app.route('/staff_inf',methods=['GET','PSOT'])
def staff_inf():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    user_id=session['user_id']
    db=connect_db()
    c=db.cursor()
    staff='''
    select staff_id, concat(first_name,' ',last_name), email, phone_number, hire_date,employment_id, salary, manager_id, section_id from staffs where staff_id=%d
    '''%user_id
    c.execute(staff)
    u=c.fetchall()
    print(u)
    c.close()
    db.close()
    return render_template('staff_inf.html',u=u)

#员工信息
@app.route('/staffs_inf',methods=['GET','PSOT'])
def staffs_inf():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    user_id=session['user_id']
    db=connect_db()
    c=db.cursor()
    staff='''
    select staff_id, concat(first_name,' ',last_name), email, phone_number, hire_date,employment_id, salary, manager_id, section_id from staffs order by staff_id
    '''
    c.execute(staff)
    u=c.fetchall()
    c.close()
    db.close()
    return render_template('hr_staffs.html',u=u)

#部门信息
@app.route('/section_inf',methods=['GET','POST'])
def section_inf():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    db=connect_db()
    c=db.cursor()
    section='''
    select * from sections
    '''
    c.execute(section)
    u=c.fetchall()
    c.close()
    db.close()
    return render_template('section.html',u=u)
#部门地址
@app.route('/hr_places',methods=['GET','POST'])
def hr_places():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    db=connect_db()
    c=db.cursor()
    sql='''
    select * from places
    '''
    c.execute(sql)
    u=c.fetchall()
    c.close()
    db.close()
    return render_template('hr_places.html',u=u)

#薪资水平
@app.route('/salary',methods=['GET','POST'])
def salary():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    db=connect_db()
    c=db.cursor()
    sql='''
    select section_id,max(salary),min(salary),avg(salary) from staffs group by  section_id
    '''
    c.execute(sql)
    u=c.fetchall()
    c.close()
    db.close()
    return render_template('salary.html',u=u)



#部门员工信息
@app.route('/session_inf',methods=['GET','POST'])
def session_inf():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    else:
        user_id=session.get('user_id')
        db=connect_db()
        c=db.cursor()
        section='''
        select section_id from staffs where staff_id='%d'
        '''%user_id
        c.execute(section)
        section_id=int(c.fetchall()[0][0])
        Man1='''
        select * from staffs where section_id='%d' order by staff_id
        '''%section_id
        c.execute(Man1)
        inf1=c.fetchall()
        c.close()
        db.close()
        return render_template('man_section.html',u=inf1)
#部门薪资水平
@app.route('/man_salary',methods=['GET','POST'])
def man_salary():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    db=connect_db()
    c=db.cursor()
    user_id=session.get('user_id')
    section='''
    select section_id from staffs where staff_id='%d'
    '''%user_id
    c.execute(section)
    section_id=int(c.fetchall()[0][0])
    sql='''
    select max(salary),min(salary),avg(salary) from staffs where section_id='%d'
    '''%section_id
    c.execute(sql)
    u=c.fetchall()
    c.close()
    db.close()
    return render_template('man_salary.html',u=u)

#修改号码
@app.route('/phone', methods=['GET','POST'])
def phone():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    if request.method=='POST':
        if request.form['num']==request.form['num1']:
            db = connect_db()
            cur = db.cursor()
            sql = "update staffs set phone_number="+"'"+request.form['num']+"'"+" where staff_id="+str(session['user_id'])
            print(sql)
            cur.execute(sql)
            db.commit()
            db.close()
            flash('修改成功')
            return render_template('staff_index.html')
        else :
            flash('两次输入不同，请重新输入')
            return render_template('phone.html')
    else:
        return render_template('phone.html')
@app.route('/hr_resection',methods=['GET','POST'])
def hr_resection():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    if request.method=='POST':
        try:
            db=connect_db()
            c=db.cursor()
            section_id=request.form['num']
            new_name=request.form['num1']
            sql="update sections set section_name="+"'"+new_name+"'" +"where section_id="+str(section_id)
            c.execute(sql)
            c.close()
            db.close()
            flash('修改成功')
        except:
            flash('输入错误')
    return render_template("hr_resection.html")

@app.route('/hr_query',methods=['GET','POST'])
def hr_query():
    if not session.get('user_id'):
        flash('请先登录，再访问页面...')
        return redirect(url_for('login'))
    if request.method=='POST':
        db=connect_db()
        c=db.cursor()
        n1=request.form['num']
        n2=request.form['num1']
        if len(n2)==0:
            sql="select * from staffs where staff_id="+str(n1)
            c.execute(sql)
            res=c.fetchall()
            flash(res)
        else:
            sql1="select * from staffs where first_name="+n2
            c.execute(sql1)
            res=c.fetchall()
            flash(res)
        c.close()
        db.close()
    return render_template("hr_query.html")


if __name__=='__main__':
    app.run()
