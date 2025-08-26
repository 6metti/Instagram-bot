import time
import random
import logging

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')
logger = logging.getLogger(__name__)

def human_delay(min_sec=2, max_sec=5):
    """یک تأخیر تصادفی بین min_sec و max_ثانیه ایجاد می‌کند تا رفتار انسانی تقلید شود."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def log_message(message):
    """یک پیام را با timestamp در لاگ ثبت می‌کند."""
    logger.info(message)
