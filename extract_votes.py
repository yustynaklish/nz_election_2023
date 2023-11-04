import os


# files in the raw_data folder contain the raw html of election results per electorate
# the following code processes those files into a .txt of pipe delimited rows with the following structure
# electorate_name | candidate_name | candidate_votes | party_name | party_votes

def vote_results_by_electorate(raw_electorate_file):

    raw_data = open(raw_electorate_file, 'r')
 
    raw_data_array = []
    for i in raw_data:
        raw_data_array.append(i)



    for i in range(len(raw_data_array)):
        if raw_data_array[i].strip() == '<div class="page-title">':
            electorate = raw_data_array[i+2].replace('<h2>', '').replace(' - Official Result</h2>', '').strip()

    total_votes_array = []    

    for i in range(len(raw_data_array)):

        if (raw_data_array[i].strip() == '<div class="item odd">' or raw_data_array[i].strip() == '<div class="item even">') and raw_data_array[i+7].replace('<span>', '').replace('</span>', '').strip() != '<tr>' and raw_data_array[i+8].replace('<span>', '').replace('</span>', '').strip() != '<tr>':
            candidate_name = raw_data_array[i+1].replace('<span>', '').replace('</span>', '').strip() 
            candidate_vote_count = raw_data_array[i+2].replace('<span class="float-right">', '').replace('</span>', '').strip()

            party_name = raw_data_array[i+7].replace('<span>', '').replace('</span>', '').strip()
            party_vote_count = raw_data_array[i+8].replace('<span class="float-right">', '').replace('</span>', '').strip()

            total_votes_array.append(electorate + ' | ' + candidate_name + ' | ' +  candidate_vote_count + ' | ' + party_name + ' | ' +  party_vote_count + '\n')

    return total_votes_array
        

# write to clean_data
directory = os.fsencode('raw_data')

# total data in one file
clean_electorate_total_file = open('clean_data/total.txt', 'w')
clean_electorate_total_file.write(('electorate_name | candidate_name | candidate_votes | party_name | party_votes \n'))

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    raw_electorate_file = 'raw_data/' + filename

    # iterate through raw html files to get one clean file per electorate
    clean_electorate_file = 'clean_data/' + filename
    clean_electorate_file = open(clean_electorate_file, 'w')
    clean_electorate_file.write('electorate_name | candidate_name | candidate_votes | party_name | party_votes \n')


    vote_results_by_electorate_array = vote_results_by_electorate(raw_electorate_file)
    
    for i in vote_results_by_electorate_array:
        clean_electorate_file.write(i)
        clean_electorate_total_file.write(i)





    
