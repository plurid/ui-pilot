# two use cases, run the model:
# (i)  to replicate behavior
# (ii) in command mode

# replicate mode    input video          (e.g. video of pressing a button)
# command mode      input text/voice     (e.g. "press that button")


# desired state
# a model which is able to recognize the day-to-day user interface
# (MacOS, Windows, Linux, maybe iOS, Android)
# and take meaningful actions
# (press buttons, scroll, drag and drop, modify text, e.g. filenames)


# training:
# from the dataset (recordings of interface usage)
# -> observe -> act -> reward/punish ->


# output
# keyboard sequence - ks (keydown/keyup: a-down, a-up, shift-down, b-down, b-up, shift-up writes "aB")
# mouse sequence - ms (mouse movement to (x,y), mouse click down/up, mouse right click)

# given a frame (observation) infer what's the next action (ks or ms)


# questions
# what kind of frames sequence? 60fps?
# what resolution? how to make it resolution-agnostic?
# what is the reward? e.g. starting frame standard desktop, command "make a new folder on desktop"
# there should be a check_task_completion function
# maybe have a loop that questions the user: is the task done?
# state-action-question:
#   yes: end
#   no: state-action-question
