import argparse
import pandas as pd

if __name__=="__main__":
    arg_parser = argparse.ArgumentParser(
        prog = 'clean.py',          # program name
        # description = 'The script for data cleansing'       # function description
        )

    arg_parser.add_argument('args',nargs=3)
    args = arg_parser.parse_args()

    contact_info_file = args.args[0]
    other_info_file = args.args[1]
    output_file = args.args[2]

#print(args)

    if not contact_info_file or not other_info_file or not output_file:
        print("No argument found. Attach -h as the argument to view the help info")
        exit(1)


 #(1) merge the two input data files based on the ID of each respondent.
    contact_info=pd.read_csv(contact_info_file)
    other_info=pd.read_csv(other_info_file)
    df = pd.merge(contact_info,other_info,left_on="respondent_id",right_on="id")

#(2) drop any rows with missing values.
    df.dropna(inplace=True)

#(3) drop rows if the job value contains ‘insurance’ or ‘Insurance’.
    df.drop(df[df['job'].str.lower().str.contains('insurance')].index,inplace=True)

#(4) write the cleaned data to the file specified by the output_file argument.
    df.to_csv(output_file)

    print("Shape of the output file: "+str(df.shape))