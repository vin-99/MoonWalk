from apscheduler.schedulers.background import BackgroundScheduler

schedular = BackgroundScheduler()

def start_schedular(app):
    def process_orders():
        with app.app_context():
            from app.services.kitchen_processor import KitchenProcessor
            KitchenProcessor.process()

    schedular.add_job(process_orders, trigger="interval", seconds=5)
    schedular.start()