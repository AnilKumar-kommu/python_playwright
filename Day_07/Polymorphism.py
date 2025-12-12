# Base class
class Notification:
    def send_notification(self):
        raise NotImplementedError("Subclass must implement this method")


# Derived class 1: Email Notification
class EmailNotification(Notification):
    def send_notification(self):
        print("📧 Sending Email Notification to user@example.com...")


# Derived class 2: SMS Notification
class SMSNotification(Notification):
    def send_notification(self):
        print("📱 Sending SMS Notification to +91-9876543210...")


# Derived class 3: Push Notification
class PushNotification(Notification):
    def send_notification(self):
        print("🔔 Sending Push Notification to mobile device...")


# Function using polymorphism
def notify_user(notification: Notification):
    # The same method name behaves differently based on the object type
    notification.send_notification()


# Real-time scenario: different types of notifications
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

# Sending all notifications using the same function
notify_user(email)
notify_user(sms)
notify_user(push)
