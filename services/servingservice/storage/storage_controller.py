from skipper_lib.events.event_receiver import EventReceiver
from app.storage_service import StorageService
import os


def main():
    event_receiver = EventReceiver(username=os.getenv('RABBITMQ_USER', 'skipper'),
                                   password=os.getenv('RABBITMQ_PASSWORD', 'welcome1'),
                                   host=os.getenv('RABBITMQ_HOST', '127.0.0.1'),
                                   port=os.getenv('RABBITMQ_PORT', 5672),
                                   queue_name=os.getenv('QUEUE_NAME', 'skipper_storage'),
                                   service=StorageService,
                                   service_name=os.getenv('SERVICE_NAME', 'serving_model'),
                                   logger=os.getenv('LOGGER_RECEIVER_URL',
                                                    'http://127.0.0.1:5001/api/v1/skipper/logger/log_receiver'))


if __name__ == "__main__":
    main()
