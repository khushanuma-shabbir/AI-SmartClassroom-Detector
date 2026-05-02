import csv
from datetime import datetime
from pathlib import Path

class AttendanceLogger:
    def __init__(self, log_dir='attendance_logs'):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
    def log_attendance(self, student_count):
        """Save attendance record to CSV"""
        timestamp = datetime.now()
        date_str = timestamp.strftime('%Y-%m-%d')
        time_str = timestamp.strftime('%H:%M:%S')
        
        log_file = self.log_dir / f'attendance_{date_str}.csv'
        
        # Create file with headers if it doesn't exist
        file_exists = log_file.exists()
        
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Date', 'Time', 'Student Count'])
            writer.writerow([date_str, time_str, student_count])
        
        return str(log_file)
    
    def get_today_logs(self):
        """Retrieve today's attendance logs"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        log_file = self.log_dir / f'attendance_{date_str}.csv'
        
        if not log_file.exists():
            return []
        
        logs = []
        with open(log_file, 'r') as f:
            reader = csv.DictReader(f)
            logs = list(reader)
        
        return logs
