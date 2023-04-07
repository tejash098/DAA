def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    end_time = -1
    for activity in activities:
        if activity[0] >= end_time:
            selected_activities.append(activity)
            end_time = activity[1]
    
    return len(selected_activities)
activities = [(1, 3), (2, 5), (5, 7), (6, 8), (8, 10), (9, 12)]
print("Maximum number of non-overlapping activities:", activity_selection(activities))
