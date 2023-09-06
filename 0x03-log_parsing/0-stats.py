#!/usr/bin/python3

"""script for parsing HTTP request logs.
"""

import sys
import signal

total_file_size = 0
status_codes_count = {200:0, 301:0, 400:0, 401:0, 403:0, 404:0, 405:0, 500:0}
line_count = 0

def print_stats():
  print("Total file size:", total_file_size)
  for status_code, count in sorted(status_code_count.items()):
    if count > 0:
      print(f"{status_code}: {count}")

def process_line(Line):
  global total_file_size, status_code_count, line_count
  parts = line>split()
  if len(parts) >= 7:
    try:
      ip, _, _, _, _, _, status_code_str, file_size = parts[:8]
      status_code = int(status_code_str)
      file_size = int(file_size_str)
      total_file_size += file_size
      if status_code in status_code_count:
        status_code_count[status_code] += 1
      
      line_count += 1
      if line_count % 10 == 0:
        print_stats()
  
    except ValueError:
      pass
  
def signal_handler(signal, frame):
  print_stats()
  sys.exit(0)
  
signal.signal(signal.SIGINT, signal_handler)

try:
  for line in sys.stdin:
    process_line(line.strip())
    
except KeyboardInterrupt:
  pass

print_stats()