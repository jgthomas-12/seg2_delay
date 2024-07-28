from seg2_files.seg2load import seg2_load
import numpy as np
import os

def modify_delay(traces, header, delay_key='DELAY', new_delay_value=0):
    if delay_key in header ['tr']:
      header['tr'][delay_key] = [new_delay_value] * len(header['tr'][delay_key])
    return traces, header

def seg2_save(file_path, traces, header):
  with open(file_path, 'wb') as f:
    for key, value in header.items():
      if key == 'tr':
        continue
      f.write(f"{key}: {value}\n".encode())

    for key, values in header['tr'].items():
      f.write(f"{key}: {','.join(map(str, values))}\n".encode())

    for trace in traces:
      f.write(trace.tobytes())

seismic_file_path = '1001.dat'

traces, header = seg2_load(seismic_file_path)

print("Original Header:", header)
print("Traces shape:", traces.shape)

new_delay_value = 0
traces, header = modify_delay(traces, header, new_delay_value=new_delay_value)

print("Modified Header:", header)

home_directory = "/Users/jessethomas/Desktop/Collier /SEG-2/seg_2_modified"

modified_seismic_file_path = os.path.join(home_directory,"1001_modified.dat")
seg2_save(modified_seismic_file_path, traces, header)

print(f"Modified seismic file saved to {modified_seismic_file_path}")