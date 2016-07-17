from polls.models import *
import operator
import random

#separate the user votes into two categories: (1)most recent (2)previous history
def categorizeResponses(all_responses):
    latest_responses = []
    previous_responses = []
    
    if len(all_responses) > 0:
        #the first response must be the most recent 
        latest_responses.append(all_responses[0])   
    
    others = all_responses[1:]
    
    #the outer loop goes through all the responses
    for response1 in others:
        if response1.user == None:
            continue
        
        add = True
        #check if the user has voted multiple times
        for response2 in latest_responses:
            if response1.user.username == response2.user.username:
                add = False
                previous_responses.append(response1)
                break

        #this is the most recent vote
        if add:
            latest_responses.append(response1)   
    
    return (latest_responses, previous_responses)

# ALLOCATION ALGORITHM FUNCTIONS HERE:
def allocation(question):
    allocation_order = question.allocationvoter_set.all()
    # the latest and previous responses are from latest to earliest
    (latest_responses, previous_responses) = categorizeResponses(question.response_set.reverse())

    if question.poll_algorithm == 1:
        #SD early first
        allocation_serial_dictatorship(list(reversed(latest_responses)), early_first = 1)
    elif question.poll_algorithm == 2:
        #SD late first
        allocation_serial_dictatorship(latest_responses, early_first = 0)
    elif question.poll_algorithm == 3:
        if len(allocation_order) != 0:
            allocation_manual(allocation_order, latest_responses)
        else:
            allocation_random_assignment(latest_responses)

# Serial dictatorship algorithm to allocate items to students for a given question.
# It takes as an argument the response set to run the algorithm on.
# The order of the serial dictatorship will be decided by increasing
# order of the timestamps on the responses for novel questions, and reverse
# order of the timestamps on the original question for follow-up questions.
def allocation_serial_dictatorship(responses, early_first = 1):
    #make sure there is at least one response    
    if len(responses) == 0:
        return
    
    item_set = responses[0].question.item_set.all()
    student_response_order = responses
    
    # it's a follow-up question, so run it in reverse order of timestamp from original question
    if responses[0].question.follow_up != None:
        response_set = []
        # in order to run the algorithm without modifying data, we query each response in this set and store a copy
        for r in student_response_order:
            response_set.append(r)

        # we set the timestamp value to be equal to timestamp of the original question and sort it in reverse order
        for r in responses:
            temp = r.question.follow_up.response_set.filter(user = r.user)[0] # this assumes the same user set responded to questions 1 and 2
            r.timestamp = temp.timestamp
        if early_first:
            response_set.sort(key = operator.attrgetter('timestamp'), reverse = True)
        else: 
            response_set.sort(key = operator.attrgetter('timestamp'), reverse = False)
        student_response_order = response_set
    items = []
    # here we acquire copies of each item to use for allocation
    for item in item_set:
        items.append(item)

    # the ordering of students is already set, so this loop only needs to do the allocation one by one
    for user_response in student_response_order:
        voter, created = AllocationVoter.objects.get_or_create(question=user_response.question, user=user_response.user)
        if created == True:
            voter.save()      

        highest_rank = len(items)
        myitem = items[0]
        prefs = user_response.dictionary_set.all()[0]
        # here we find the item remaining that this user ranked the highest
        for item in items:
            if prefs.get(item) < highest_rank:
                highest_rank = prefs.get(item)
                myitem = item
        print ("Allocating item " + myitem.item_text + " to user " + user_response.user.username)
        # now we allocate that item to this user and remove that item from consideration for other students
        user_response.allocation = myitem
        user_response.save()
        items.remove(myitem)
    return

# the poll owner can specify an order to allocate choices to voters
def allocation_manual(allocation_order, responses):
    #make sure there is at least one response    
    if len(responses) == 0:
        return        

    item_set = responses[0].question.item_set.all()
    items = []
    response_set = []

    for item in item_set:
        items.append(item)
        
    for order_item in allocation_order:
        question = order_item.question
        user = order_item.user
        response = question.response_set.reverse().filter(user=user)[0]
        order_item.response = response
        order_item.save()
        response_set.append(response)
    
    for user_response in response_set:
        highest_rank = len(items)
        myitem = items[0]
        prefs = user_response.dictionary_set.all()[0]
        # here we find the item remaining that this user ranked the highest
        for item in items:
            if prefs.get(item) < highest_rank:
                highest_rank = prefs.get(item)
                myitem = item
        print ("Allocating item " + myitem.item_text + " to user " + user_response.user.username)
        # now we allocate that item to this user and remove that item from consideration for other students
        user_response.allocation = myitem
        user_response.save()
        items.remove(myitem)
    return
# This is a toy algorithm present for testing certain system functionality. It will simply allocate a random item
# to each user in the response set.
def allocation_random_assignment(responses):
    #make sure there is at least one response    
    if len(responses) == 0:
        return    

    item_set = responses[0].question.item_set.all()
    student_response_order = responses
    items = []

    for item in item_set:
        items.append(item)

    for student_response in student_response_order:
        index = random.randrange(len(items))
        myitem = items[index]
        student_response.allocation = myitem
        student_response.save()
        items.remove(myitem)
    return