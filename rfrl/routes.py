from . import api
from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@bp.route('/get_referral', methods=['GET'])
def get_referral():
    cards = api.get_credit_cards()
    referral_links = api.get_referral_links()
    return render_template('get_rfrl.html', cards=cards, referral_links=referral_links)

@bp.route('/give_referral', methods=['GET'])
def give_referral():
    cards = api.get_credit_cards()
    return render_template('give_rfrl.html', cards=cards)