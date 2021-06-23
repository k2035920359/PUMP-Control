
# coding: utf-8

# In[ ]:


from pynq.overlays.base import BaseOverlay
base = BaseOverlay("base.bit")

from pynq.lib import Pmod_PWM

pwm = Pmod_PWM(base.PMODA,0)

import time

# Generate a 10 us clocks with 50% duty cycle
period=10
duty=50
pwm.generate(period,duty)

# Sleep for 4 seconds and stop the timer
time.sleep(4)
pwm.stop()

import time

# Generate a 20 us clocks with 25% duty cycle
period=20
duty=25
pwm.generate(period,duty)

# Sleep for 5 seconds and stop the timer
time.sleep(5)
pwm.stop()


# In[ ]:





# In[ ]:





# In[ ]:




