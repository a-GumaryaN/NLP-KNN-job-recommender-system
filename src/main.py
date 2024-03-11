from jobs_data import *
from resume_data import *

job_sample=18891

def jaccard_knn_researcher(job_index):
    matched_data=[]
    job_requirements=set(jobs.requirements[job_index])

    for index in resume.index:
        skills=set(resume.skills[index])

        matched_items=job_requirements.intersection(skills)

        matching_value= ( len(matched_items) / len(job_requirements) ) * 100

        data={"matching_value":matching_value,"resume_index":index}
        matched_data.append(data)

    return matched_data

matched_data=jaccard_knn_researcher(job_sample)
matched_data=pd.DataFrame(matched_data)
matched_data=matched_data.sort_values("matching_value",ascending=False)

print(matched_data)

print(jobs.Title[4])
print(resume.skills[0])