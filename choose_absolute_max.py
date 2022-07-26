import pandas as pd

df_ref = pd.read_csv("smina_results_best_poses.csv")
df_all_result = pd.read_csv("all_results_smina_pubchem.csv")


target_scores = [] 
target_entry = [] 
ref_scores= [] 
ref_entry = [] 

for i in range(len(df_all_result)):
    entry = df_all_result.iloc[i]["Entry"]
    score = float(df_all_result.iloc[i]["Score"])
    entry = entry.replace(".log", "")
    split_entry = entry.split("_")
    ref_row = df_ref.loc[df_ref["reference_Entry"].astype(str) == split_entry[0]]
    ref_score = float(ref_row["TopScore"])

    if abs(ref_score) <= abs(score):
        target_scores += [score]
        ref_scores += [ref_score]
        target_entry += [split_entry[1]] 
        ref_entry += [split_entry[0]] 

print(target_entry)
print(len(ref_scores), len(target_scores), len(target_entry), len(ref_entry))
df_result = pd.DataFrame()
df_result["RefEntry"] = ref_entry
df_result["RefScore"] = ref_scores
df_result["MolEntry"] = target_entry
df_result["MolScore"] = target_scores
df_result.to_csv("target.csv")
