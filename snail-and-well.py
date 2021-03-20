#!/usr/bin/env python
# coding: utf-8

# <img src="https://bit.ly/2VnXWr2" width="100" align="left">

# # The Snail and the Well
# 
# A snail falls at the bottom of a 125 cm well. Each day the snail rises 30 cm. But at night, while sleeping, slides 20 cm because the walls are wet. How many days does it take for the snail to escape the well?
# 
# **Hint**: The snail gets out of the well when it surpasses the 125cm of height.
# 
# ## Tools
# 
# 1. Loop: **while**
# 2. Conditional statements: **if-else**
# 3. Function: **print()**
# 
# ## Tasks
# 
# #### 1. Assign the challenge data to variables with representative names: `well_height`, `daily_distance`, `nightly_distance` and `snail_position`.

# In[2]:


#assigning data to variables with representative names. DD

#distance from top of well to the bottom of well
well_height = 125 
#distance snail climbs up each day
daily_distance = 30 
#distance snail slips each night due to wet surface
nightly_distance = 20 
#snail is at the bottom on the first day
snail_position = 0 


# #### 2. Create a variable `days` to keep count of the days that pass until the snail escapes the well. 
# 

# In[3]:


days = 1 #considering first day as day 1 when snaily embarks on the climb


# #### 3. Find the solution to the challenge using the variables defined above. 

# In[4]:


#print("Snaily at rock bottom.")

distance_difference = daily_distance - nightly_distance

snail_position += distance_difference

while snail_position < well_height:
    snail_position += distance_difference
    days = days + 1
    #print("Snaily still climbing...")
    
#print("Snaily climbed and is out in ", days,"!!!")
    
    


# #### 4. Print the solution.

# In[5]:


if snail_position < well_height:
    print("Snaily still climbing...")
elif snail_position == well_height:
    print("Snaily almost there")
else:
    print("Snaily made it to the top on the ", days,"th day!!!")


# ## Bonus
# The distance traveled by the snail each day is now defined by a list.
# ```
# advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
# ```
# On the first day, the snail rises 30cm but during the night it slides 20cm. On the second day, the snail rises 21cm but during the night it slides 20cm, and so on. 
# 
# #### 1. How many days does it take for the snail to escape the well?
# Follow the same guidelines as in the previous challenge.
# 
# **Hint**: Remember that the snail gets out of the well when it surpasses the 125cm of height.

# In[6]:


advance_cm = [30,21,33,77,44,45,23,45,12,34,55]
days = 0
climb_acc = 0
well_height_a = well_height + 1

#while (i < len(advance_cm)): 
for i in advance_cm:
    climb_acc += i - 20
    left_acc = 125 - climb_acc
    days = days + 1
    #i += 1
    #while climb_acc < well_height_a:
    #print("Still climbing!",left_acc,"cm more to go!")    
    if climb_acc < well_height:
        print("Still climbing!",left_acc,"cm more to go!")
    elif climb_acc > well_height:
        print("Snaily out of the well!!", climb_acc," cm climbed in", days, "days")
        
        #while climb_acc < well_height_a:
            #print("Done and dusted!", climb_acc," cm climbed in", days, "days")
    else:
        print("Snaily has already escaped, and on this", days, "th day he just kept moving")

    
        
    #print("test", days, climb_acc)


# #### 2. What is its maximum displacement in one day? And its minimum? Calculate the displacement using only the travel distance of the days used to get out of the well. 
# **Hint**: Remember that displacement means the total distance risen taking into account that the snail slides at night.  

# In[7]:


displacement_acc_list = []
#distance travelled is total (irrespective of direction), displacement is the shortest distance traveled.
#assuming here that the question and hint means displacement = advance_cm - slide_cm
for i in advance_cm:
        displacement_per_day = i-20
        displacement_acc_list.append(displacement_per_day)
        
print(displacement_acc_list) #displacement list printing

list_only_in_well = displacement_acc_list[:6]
list_only_in_well

print("Maximum displacement: ",max(list_only_in_well))
print("Minimum displacement: ",min(list_only_in_well))


# #### 3. What is its average progress? Take into account the snail slides at night.

# In[8]:


#Assumption: Progess is gain in terms of old_position vs new_postion,displacement and/or left_to_climb
#since we have been dealing with displacement, proceeding with average progress in terms of displacement as it also accounts for sliding at night

average_progress_during_well = sum(list_only_in_well)/len(list_only_in_well)
average_progress_overall = sum(displacement_acc_list)/len(displacement_acc_list)

print("Average progress while climbing up the well: ", average_progress_during_well)
print("Average progress overall: ", average_progress_overall)


# #### 4. What is the standard deviation of its displacement? Take into account the snail slides at night.

# In[9]:


import math

#for the population list (including distance traveled by snaily after the great escape)
list_1 = []
for i in displacement_acc_list:
    diff_mean_obs = i - average_progress_overall
    diff_mean_obs_sq = diff_mean_obs**2
    list_1.append(diff_mean_obs_sq)

sum_1 = sum(list_1)
div_obs_no = sum_1/len(list_1)
stdev_1 = math.sqrt(div_obs_no)



#for the observations (before snaily's great escape)
list_2 = []
for i in list_only_in_well:
    diff_mean_obs_dw = i - average_progress_during_well
    diff_mean_obs_sq_dw = diff_mean_obs_dw**2
    list_2.append(diff_mean_obs_sq_dw)

sum_2 = sum(list_2)
div_obs_no_dw = sum_2/len(list_2)
stdev_2 = math.sqrt(div_obs_no_dw)




# In[10]:


print("standard deviation of displacement (population): ",stdev_1)
print("standard deviation of displacement (only observations during well): ",stdev_2)


# In[ ]:




