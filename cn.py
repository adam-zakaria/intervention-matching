from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('all-MiniLM-L6-v2')

# load the spreadsheets 
df_pd = pd.read_excel('program descriptions.xlsx')
df_i = pd.read_excel('interventions.xlsx')

# Remove columns with nans
df_pd = df_pd.dropna(axis=1)

# a column to iterate through
column_name = 'program descriptions'

sentences0 = []
sentences1 = []

for cell in df_pd[column_name]:
    sentences0.append(cell)

for index, row in df_i.iterrows():
    for cell in row:
        sentences1.append(cell)

#Encode all sentences
embeddings0 = model.encode(sentences0)
embeddings1 = model.encode(sentences1)

#Compute cosine similarity between all pairs
cos_sim = util.cos_sim(embeddings0, embeddings1)

#Add all pairs to a list with their cosine similarity score
all_sentence_combinations = []
for i in range(len(cos_sim)-1):
    for j in range(i+1, len(cos_sim)):
        all_sentence_combinations.append([cos_sim[i][j], i, j])

#Sort list by the highest cosine similarity score
all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)

print("Top-5 most similar pairs:")
for score, i, j in all_sentence_combinations[0:5]:
    print("{} \t {} \t {:.4f}".format(sentences0[i], sentences1[j], cos_sim[i][j]))
