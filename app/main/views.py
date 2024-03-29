from flask import (render_template, request, redirect, url_for, abort)
from . import main
from .forms import AddPitch, DelPitch, FeedbackForm
from ..models import User, Comments, Feedback
from flask_login import login_required, current_user
from .. import db, photos


@main.route("/")
@login_required
def index():
    return render_template('home.html')


@main.route("/add", methods=["GET", "POST"])
@login_required
def add_pitch():
    form = AddPitch()
    print('pre validation')
    if form.validate_on_submit():
        print('submitting')

        comment = form.comment.data
        category = form.category.data

        new_comment = Comments(comment_section=comment, categories=category)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.pitch_list'))

    return render_template('add.html', form=form)


@main.route('/pitchlist')
def pitch_list():

    comments = Comments.query.all()
    return render_template('pitchlist.html', comments=comments)


@main.route('/delete', methods=['GET', 'POST'])
def del_pitch():

    form = DelPitch()

    if form.validate_on_submit():
        id = form.id.data
        comment = Comments.query.get(id)
        db.session.delete(comment)
        db.session.commit()

        return redirect(url_for('main.pitch_list'))
    return render_template('delete.html', form=form)


@main.route("/profile/<int:id>/update/pic", methods=["POST"])
def update_pic(id):
    user = User.query.filter_by(id=id).first()
    if "photo" in request.files:
        filename = photos.save(request.files["photo"])
        path = f"photos/{filename}"
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for("main.update",
                            id=id))


@main.route("/feedback/<int:comment_id>", methods=['GET', 'POST'])
@login_required
def feedback(comment_id):

    form = FeedbackForm()

    if form.validate_on_submit():
        feedback = form.feedback.data

        new_feedback = Feedback(feedback_section=feedback, user_id=current_user.id, comments_id=comment_id)
        db.session.add(new_feedback)
        db.session.commit()

    all_feedback = Feedback.query.filter_by(comments_id=comment_id).all()
    title = 'feedback'
    return render_template("feedback.html", all_feedback=all_feedback, title=title, form=form)


@main.route("/category/<cname>")
def category(cname):
    posts = Comments.query.filter_by(categories=cname).all()
    title = cname

    return render_template("category.html",
                           title=title,
                           posts=posts)


@main.route("/about")
def about():
    title = "About Pitches ?"
    return render_template("about.html",
                           title=title)
