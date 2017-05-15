import sys

sys.stdout.write("test-before\n")
sys.stdout.flush()
sys.stdout.write("fail"*1024*65)
sys.stdout.write("\n")
sys.stdout.flush()
sys.stdout.write("test-after\n")
sys.stdout.flush()
