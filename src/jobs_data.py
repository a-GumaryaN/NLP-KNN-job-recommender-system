import pandas as pd
from nnp_extractor import NNP
from nnp_extractor import array_nnp_extractor
from pathlib import Path
import ast

processed_job_data="./data/job_data.csv" #processed job data path
jobs_dataset="./data/data-job-posts.csv" #jobs data path

jobs_data = Path(processed_job_data)

if jobs_data.is_file():

    print("jobs processed data exist")

    jobs=pd.read_csv(processed_job_data)

    def string_to_list(input_string):
        return ast.literal_eval(input_string)
    
    jobs.requirements=jobs.requirements.apply(string_to_list)
    
else:
    print("process jobs data")

    jobs=pd.read_csv(jobs_dataset)

    jobs.RequiredQual.fillna(jobs.JobDescription,inplace=True)

    def job_cleaner(requirement):
        requirement=str(requirement)
        requirement=requirement.replace(";","")
        requirement=requirement.replace("'","")
        requirement=requirement.replace("- ","")
        requirement=requirement.split("\r\n")
        return requirement

    jobs.RequiredQual=jobs.RequiredQual.apply(job_cleaner)
    jobs["requirements"]=jobs.RequiredQual.apply(array_nnp_extractor)
    jobs.to_csv(processed_job_data)