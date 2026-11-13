# Python implementation of Job-Sequencing

def job_sequencing(jobs):
    # Sort jobs by profit in descending order
    jobs = sorted(jobs, key=lambda job: job["profit"], reverse=True)

    max_deadline = max(job["deadline"] for job in jobs)
    slots = [None] * max_deadline

    total_profit = 0

    for job in jobs:
        # Find the latest available slot before deadline
        for slot in range(min(job["deadline"], max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job["id"]
                total_profit += job["profit"]
                break

    return slots, total_profit


jobs = [
    {"id": "J1", "deadline": 2, "profit": 100},
    {"id": "J2", "deadline": 1, "profit": 19},
    {"id": "J3", "deadline": 2, "profit": 27},
    {"id": "J4", "deadline": 1, "profit": 25},
    {"id": "J5", "deadline": 3, "profit": 15}
]

schedule, profit = job_sequencing(jobs)

print("Job Sequencing with Deadlines")
print("\nSelected Job Schedule:")

for index, job in enumerate(schedule):
    print(f"Slot {index + 1}: {job if job else 'Empty'}")

print("\nMaximum Profit:", profit)
