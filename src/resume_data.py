import pandas as pd
from nnp_extractor import NNP
from nnp_extractor import array_nnp_extractor
from pathlib import Path
import sys

processed_resume_data="./data/resume_data.csv" #processed resume data path
resume_dataset="./data/UpdatedResumeDataSet.csv" #input resume data path

resume_data = Path(processed_resume_data)

if resume_data.is_file():
    print("resume processed data exist")
    resume=pd.read_csv(processed_resume_data)
    
else:
    print("start resume data process")

    resume=pd.read_csv(resume_dataset)

    def resume_cleaner(skills):
        skills=skills.replace("*","")
        skills=skills.replace("-","")
        skills=skills.replace("â\x80¢","")
        skills=skills.split("\r\n")
        return skills

    resume["skills"]=resume.Resume.apply(resume_cleaner)

    resume.Resume=resume.Resume.apply(resume_cleaner)
    resume["skills"]=resume.Resume.apply(array_nnp_extractor)
    resume.to_csv(processed_resume_data)