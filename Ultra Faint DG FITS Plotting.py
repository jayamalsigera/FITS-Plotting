#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as numpy
from astropy.io import fits
from astropy.table import Table
from matplotlib.colors import LogNorm
from scipy.stats import gaussian_kde
from scipy.interpolate import *
from pylab import *
from scipy.optimize import curve_fit
import operator
from matplotlib.pyplot import *
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from astropy.utils.data import download_file


# In[3]:


event_filename = download_file('https://archive.stsci.edu/hlsps/fhufd/hlsp_fhufd_hst_acs_canesvenaticiii_multi_v2.0_cat.fits', cache=True)


# In[4]:


hdu_list = fits.open(event_filename, memmap=True)


# In[5]:


hdu_list.info()


# In[6]:


print(hdu_list[1].columns)


# In[7]:


evt_data = Table(hdu_list[1].data)


# In[8]:


x = evt_data['M606'] - evt_data['M814']


# In[9]:


y = evt_data['M814']


# In[10]:


L = sorted(zip(x,y), key=operator.itemgetter(0))


# In[11]:


xp, yp = zip(*L)


# In[12]:


data = xp,yp


# In[18]:


xy = numpy.vstack([xp,yp])
z = gaussian_kde(xy)(xy)

fig, ax = subplots()
ax.scatter(xp, yp, c=z, s=1)
ax = gca()
plt.ylim([20, 29])
plt.xlim([-1, 0.5])
ax.invert_yaxis()

show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




