from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    interest = db.Column(db.String(200))

class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lead_id = db.Column(db.String(50))
    supplier_name = db.Column(db.String(100))

@app.route('/')
def home():
    return "Backend Running"

@app.route('/create-lead', methods=['POST'])
def create_lead():

    data = request.get_json()

    new_lead = Lead(
        lead_id=f"LEAD-{Lead.query.count() + 1}",
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        interest=data['interest']
    )

    db.session.add(new_lead)
    db.session.commit()

    return jsonify({
        "message": "Lead created successfully",
        "lead_id": new_lead.lead_id
    })  

@app.route('/leads', methods=['GET'])
def get_leads():

    leads = Lead.query.all()

    output = []

    for lead in leads:
        output.append({
            "lead_id": lead.lead_id,
            "name": lead.name,
            "email": lead.email,
            "phone": lead.phone,
            "interest": lead.interest
        })

    return jsonify(output)

@app.route('/track-click', methods=['POST'])
def track_click():

    data = request.get_json()

    new_click = Click(
        lead_id=data['lead_id'],
        supplier_name=data['supplier_name']
    )

    db.session.add(new_click)
    db.session.commit()

    return jsonify({
        "message": "Click tracked successfully"
    })

@app.route('/clicks', methods=['GET'])
def get_clicks():

    clicks = Click.query.all()

    output = []

    for click in clicks:
        output.append({
            "lead_id": click.lead_id,
            "supplier_name": click.supplier_name
        })

    return jsonify(output)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
 