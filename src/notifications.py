import subprocess

def notify_user(title, message):
    """
    Sends a native Linux desktop notification using notify-send.
    
    Args:
        title (str): The bold heading of the notification.
        message (str): The body text of the notification.
    """
    try:
        # We use a list for the command to prevent shell injection vulnerabilities
        subprocess.run(["notify-send", title, message], check=True)
    except FileNotFoundError:
        # Fallback if the user is in a headless environment or missing libnotify
        print(f"🔔 Notification: {title} - {message}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to send desktop notification: {e}")