"""
Main code
"""


import pandas as pd
import matplotlib.pyplot as plt


def read_resume(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def check_variable(resume: pd.DataFrame) -> dict:
    variable_list = [
        "employment_holes",
        "volunteer",
        "worked_during_school",
        "special_skills",
    ]
    result = {}
    for var in variable_list:
        result[var] = resume[var].value_counts().to_dict()
    return result
    # for i in range(4):
    #     print(resume[variable_list[i]].value_counts())
    #     print("=======================")


# plot
def plot_data(data: dict):
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
    fig.subplots_adjust(hspace=0.5)

    for ax, (label, values) in zip(axes.ravel(), data.items()):
        ax.bar(values.keys(), values.values(), color=["blue", "green"])
        ax.set_title(label)
        ax.set_ylabel("Count")
        ax.set_xticks([0, 1])

    plt.show()


def cal_variable(file_path: str):
    resume = read_resume(file_path)
    data = check_variable(resume)
    for label, counts in data.items():
        print(f"{label}: {counts}")
        print("=======================")
    plot_data(data)


if __name__ == "__main__":
    resume_file_path = "Jiechen_Li_Mini_8_Rust/resume.csv"
    cal_variable(resume_file_path)


# data = {
#     "employment_holes": {0: 2688, 1: 2182},
#     "volunteer": {0: 2866, 1: 2004},
#     "worked_during_school": {1: 2725, 0: 2145},
#     "special_skills": {0: 3269, 1: 1601},
# }

# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
# fig.subplots_adjust(hspace=0.5)

# for ax, (label, values) in zip(axes.ravel(), data.items()):
#     ax.bar(values.keys(), values.values(), color=["blue", "green"])
#     ax.set_title(label)
#     ax.set_ylabel("Count")
#     ax.set_xticks([0, 1])

# plt.show()


# def main():
#     resume = read_resume(
#         "/Users/castnut/Desktop/706_Data_Engineering/Mini_Project/resume.csv"
#     )
#     check_variable(resume)


# main()
