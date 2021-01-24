#!/usr/bin/env python
# coding: utf-8

# In[1]:


ice_cream_rating = 8
sleeping_rating = 8.5


# In[2]:


first_name = input('First Name: ')
last_name = input('Last Name: ')
my_name = first_name + ' ' + last_name


# In[3]:


from statistics import mean
happiness_rating = mean([ice_cream_rating,sleeping_rating])


# In[4]:


print('First Name:', first_name)
print('Ice Cream rating:',ice_cream_rating)
print('Happiness rating:',happiness_rating)


# The data that is presented makes sense. I would have expected that the happiness rating would be higher, however because of the values inputted, this makes sense.

# In[5]:


print('My name is',first_name,'and I give ice cream a score of',ice_cream_rating,'out of 10!')
print('I am',my_name,'and my sleeping enjoyment rating is',sleeping_rating,'/ 10!')
print('Based on the factors above, my happiness rating is',happiness_rating,'out of 10, or',happiness_rating*10,'%!')

