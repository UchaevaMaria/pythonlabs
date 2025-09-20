import re

def anal_log(log: str):
    # IPv4 (без проверки диапазона)
    ip_pattern = r"\d{1,3}(?:\.\d{1,3}){3}"
    ips = re.findall(ip_pattern, log)

    # Временные метки YYYY-MM-DD HH:MM:SS
    ts_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    timestamps = re.findall(ts_pattern, log)

    # UPPERCASE слова (латиница + кириллица)
    upper_pattern = r"\b[A-ZА-ЯЁ]{2,}\b"
    uppers = re.findall(upper_pattern, log)

    # Email (простой вариант)
    email_pattern = r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(email_pattern, log)

    # Замена email
    sanitized = re.sub(email_pattern, "[EMAIL PROTECTED]", log)

    return {
        "ips": ips,
        "timestamps": timestamps,
        "upper_words": uppers,
        "emails": emails,
        "sanitized": sanitized
    }


if __name__ == "__main__":
    log = """
    2023-01-15 10:30:45 INFO User with email user@example.com logged from IP 192.168.1.1
    2023-01-15 10:31:12 ERROR Connection failed to 8.8.8.8 from admin@company.org
    2023-01-15 10:32:05 WARNING High memory usage detected by MONITORING system
    2023-01-15 10:33:20 INFO Backup completed successfully by BACKUP_SERVICE
    2023-01-15 10:34:00 DEBUG Received request from 10.0.0.5, user: support@domain.net
    SERVER RESTARTED at 2023-01-15 10:35:00 due to CRITICAL ERROR
    """

    result = anal_log(log)
    print("IPv4:", result["ips"])
    print("Timestamps:", result["timestamps"])
    print("UPPERCASE words:", result["upper_words"])
    print("Emails:", result["emails"])
    print("\nSanitized log:\n", result["sanitized"])