from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.main import main

@main.route("/")
def landing():
    """Send logged in users to the dashboard,
        otherwise go to login screen"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('auth.login'))


@main.route("/dashboard")
@login_required  
def dashboard():
    """Show the instructor dashboard to instructors and admins, 
        student dashboard otherwise"""
    if current_user.role in ('admin', 'instructor'):
        return render_template('instructor/dashboard.html', title='Dashboard')
    return render_template('student/dashboard.html', title='Dashboard')

