from donation.models import Pledge
from donation_portal.eaacelery import app
from .eaaxero import import_bank_transactions, import_trial_balance as import_trial_balance_non_delayed
from .emails import send_bank_transfer_instructions, send_partner_charity_reports


@app.task()
def send_bank_transfer_instructions_task(pledge_id):
    send_bank_transfer_instructions(Pledge.objects.get(id=pledge_id))


@app.task()
def process_bank_transactions():
    print("Processing bank transactions...")
    import_bank_transactions()
    # Everything else with receipts happens automatically. See donation.models.BankTransaction.save()
    import_trial_balance_non_delayed()


@app.task()
def import_trial_balance():
    import_trial_balance_non_delayed()


@app.task()
def send_partner_charity_reports_task():
    send_partner_charity_reports(test=False)
