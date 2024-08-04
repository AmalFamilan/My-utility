from collections import Counter
import pandas as pd 
import re


class TextDatasetCleaner(): 
    def __init__(self, df_path, bag_of_words=None): 
        self.bag_of_words = ["is", "was", "a", "an","there","or",
                             "are", "did", "were", "do","it","of","in", 
                             "this","that","the","to","who","what","when","where","why",
                             "for","how","get","be","has","had","have","got","go",
                             "and","us","we","if","can","not","at","so","will","but","they",
                             "he","she","on","his","her","should","would","could","by"]
        self.df = pd.read_csv(df_path, header=None) 
        # self.setup_regex()
    
    def setup_regex(self): 
        self.multi_char_search_regex = [f"\\b[{i}]\\b" for i in self.bag_of_words if len(i) < 2]
        self.single_char_search_regex = [f"\\b{i}\\b" for i in self.bag_of_words if len(i) > 1]
        self.combined_regex = "|".join(self.multi_char_search_regex)
        self.combined_regex = "|".join(self.single_char_search_regex)
    

    def clean_dataframe(self, data_column): 
        self.df = self.df.dropna() 
        new_df = self.df
        print("Original lenght", len(self.df))
        empty_list = ["NaN", "na", " "]
        indices = new_df[new_df.iloc[:, data_column].isin(empty_list)].index
        self.df = self.df.drop(indices) 

        print("After dropping NA", len(self.df))
        new_df = self.df 
        new_df.iloc[:, data_column] = new_df.iloc[:, data_column].str.lower()
        indices = new_df[new_df.iloc[:, data_column].isin(self.bag_of_words)].index
        self.df= self.df.drop(indices) 
        new_df = self.df
        print("After dropping bag of words", len(self.df))
        
        return new_df
    
    def count_words_in_csv(self):
        text = ' '.join(self.df.astype(str).apply(lambda x: ' '.join(x), axis=1)).lower()
        words = re.findall(r'\b\w+\b', text)
        word_counter = Counter(words)
        for word in self.bag_of_words:
            print(f"{word}: {word_counter[word.lower()]}")

df_path=r"D:\transformer_word_TestData\black_transformer.csv" 
cleaner = TextDatasetCleaner(df_path)
cleaner.count_words_in_csv()
df = cleaner.clean_dataframe(1)
df.to_csv(r'D:\transformer_word_TestData\cleaned_black_transformer.csv',index=False,header=None)

