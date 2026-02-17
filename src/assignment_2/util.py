def average(student_info,query):
    avg=0
    for key, value in student_info.items():
        if key==query:
            avg=sum(value)/len(value)
    return round(avg,2)