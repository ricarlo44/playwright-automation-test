import json

def generate_report():
    #generate report data
    dt = {
        "timestamp": "2026-7-18 22-52-20",
        "status": "PASSED",
        "summary": "module.py::test_case"
    }
    #open json file
    #in writing mode
    with open("report.json", "w") as file:
        #write data to json file
        json.dump(dt, file)