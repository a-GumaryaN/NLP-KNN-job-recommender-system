from jobs_data import *
from resume_data import *

def jaccard_knn_researcher(job_index):
    matched_data=[]
    job_requirements=set(jobs.requirements[job_index][0])

    for index in resume.index:
        skills=set(resume.skills[index][0])

        matched_items=job_requirements.intersection(skills)

        matching_value= ( len(matched_items) / len(job_requirements) ) * 100

        data={"matching_value":matching_value,"resume_index":index}
        matched_data.append(data)

    return matched_data

# matched_data=jaccard_knn_researcher(18891)
# matched_data=pd.DataFrame(matched_data)
# matched_data=matched_data.sort_values("matching_value",ascending=False)
# print(matched_data)

# print(jobs.Title[18890])
# print(resume.skills[709])

# print("job title : ")
# print(jobs.Title[18891])
# print("job requirements : ")
# print(jobs.requirements[18891])
# print("job requirements in resume skills intersections : ")
# print(set(resume.skills[602][0]).intersection(jobs.requirements[18891][0]))

print(resume.shape)