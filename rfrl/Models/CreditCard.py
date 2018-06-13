
class CreditCard():

    __init__(self):
        self.picture_link = None
        self.credit_scores = []
        self.referral_limit = None
        self.earn_per_referral = None
        self.sign_up_bonus = None
        self.minimum_spend = None
        self.bank_name = None
    
    def get_average_credit_score():
        return sum(self.credit_scores)/len(self.credit_scores)
    
    def get_lowest_credit_score():
        return min(score for score in self.credit_scores)
    
    