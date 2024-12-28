import os, sys
from TelegramBot import TelegramBot
from scheduler import Scheduler

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pb2_module/subscription'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pb2_module/user'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pb2_module/proxy'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pb2_module/country'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pb2_module/key'))


if __name__ == '__main__':
    tb = TelegramBot()
    scheduler = Scheduler([
        tb.cron_subscriptions_info
    ])
    scheduler.schedule_jobs()
    tb.start()
