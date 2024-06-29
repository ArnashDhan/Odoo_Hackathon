from flask import Blueprint , render_template , request , flash
from flask_login import login_required , current_user
from .models import Report
from . import db
import json
views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST': 
        report = request.form.get('report')

        if len(report) < 1:
            flash('Report is too short!', category='error') 
        else:
            new_report = Report(data=report, user_id=current_user.id)  
            db.session.add(new_report) 
            db.session.commit()
            flash('Report added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-report', methods=['POST'])
def delete_report():  
    report = json.loads(request.data)  
    reportId = report['reportId']
    report = Report.query.get(report_id)
    if report:
        if report.user_id == current_user.id:
            db.session.delete(report)
            db.session.commit()

    return jsonify({})