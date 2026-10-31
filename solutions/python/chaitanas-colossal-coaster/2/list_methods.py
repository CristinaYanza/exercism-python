"""Functions to manage and organize queues at Chaitana's roller coaster."""

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Adds a person to the express or normal queue."""
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue

    normal_queue.append(person_name)
    return normal_queue

def find_my_friend(queue, friend_name):
    """Returns the index of a friend's name in the queue."""
    return queue.index(friend_name)

def add_me_with_my_friends(queue, index, person_name):
    """Inserts a person's name at a specific position."""
    queue.insert(index, person_name)
    return queue

def remove_the_mean_person(queue, person_name):
    """Removes a person's name from the queue."""
    queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    """Counts how many times a name appears in the queue."""
    return queue.count(person_name)

def remove_the_last_person(queue):
    """Removes and returns the last person in the queue."""
    return queue.pop()

def sorted_names(queue):
    """Returns a copy of the queue sorted alphabetically."""
    return sorted(queue)
