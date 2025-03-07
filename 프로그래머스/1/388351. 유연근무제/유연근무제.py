def convert_time_to_min(time):
    return time//100*60 + time%100

def solution(schedules, timelogs, startday):
    answer = 0
    
    for idx, timelog in enumerate(timelogs):
        day = startday
        scheduled_min = convert_time_to_min(schedules[idx]) + 10
        can_reward = True
        for time in timelog:
            if day in [6,7]:
                day = (day % 7) + 1
                continue
            time_min = convert_time_to_min(time)
            if time_min > scheduled_min:
                can_reward = False
                break
            day = (day % 7) + 1
        if can_reward:
            answer += 1 
    return answer